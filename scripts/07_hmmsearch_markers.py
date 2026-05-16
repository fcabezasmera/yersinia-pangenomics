#!/usr/bin/env python3
"""
Extract protein marker genes (rpoB, gyrB, recA, atpD, fusA)
from 9,957 genomes using pyrodigal + hmmsearch
"""

import os
import sys
import subprocess
import tempfile
import pandas as pd
import pyrodigal
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from concurrent.futures import ProcessPoolExecutor, as_completed

# Paths
GENOME_DIR  = Path("02_genomes/raw")
HMM_DIR     = Path("07_markers/hmm_profiles")
OUT_DIR     = Path("07_markers/hmmsearch")
META        = "02_genomes/hq/metadata_hq.tsv"
THREADS_PER = 4   # hmmsearch threads per genome
MAX_WORKERS = 6   # parallel genomes

GENES = ["rpoB", "gyrB", "recA", "atpD", "fusA"]

OUT_DIR.mkdir(parents=True, exist_ok=True)
for gene in GENES:
    (OUT_DIR / gene).mkdir(exist_ok=True)

# ── Predict proteins with pyrodigal ──────────────────────────────────────────
def predict_proteins(fna_path):
    """Return list of SeqRecord (protein) for a genome."""
    records = list(SeqIO.parse(fna_path, "fasta"))
    orf_finder = pyrodigal.GeneFinder()
    orf_finder.train(*(bytes(r.seq) for r in records))

    proteins = []
    for rec in records:
        genes = orf_finder.find_genes(bytes(rec.seq))
        for j, gene in enumerate(genes):
            prot = SeqRecord(
                Seq(gene.translate()),
                id=f"{rec.id}_{j+1}",
                description=""
            )
            proteins.append(prot)
    return proteins

# ── hmmsearch for one gene ────────────────────────────────────────────────────
def run_hmmsearch(faa_tmp, gene, acc):
    hmm = HMM_DIR / f"{gene}.hmm"
    out = OUT_DIR / gene / f"{acc}.tbl"

    if out.exists() and out.stat().st_size > 0:
        return True  # already done

    cmd = [
        "hmmsearch",
        "--tblout", str(out),
        "--noali",
        "--cpu", str(THREADS_PER),
        "-E", "1e-10",
        str(hmm), faa_tmp
    ]
    result = subprocess.run(cmd, capture_output=True)
    return result.returncode == 0

# ── Process one genome ────────────────────────────────────────────────────────
def process_genome(acc, fna_path):
    try:
        # Skip if all genes already done
        done = all(
            (OUT_DIR / g / f"{acc}.tbl").exists()
            for g in GENES
        )
        if done:
            return acc, "skipped"

        # Predict proteins
        proteins = predict_proteins(fna_path)
        if not proteins:
            return acc, "no_proteins"

        # Write temp .faa
        with tempfile.NamedTemporaryFile(
            suffix=".faa", mode="w", delete=False
        ) as f:
            for p in proteins:
                f.write(f">{p.id}\n{str(p.seq)}\n")
            faa_tmp = f.name

        # hmmsearch for each marker gene
        results = {}
        for gene in GENES:
            ok = run_hmmsearch(faa_tmp, gene, acc)
            results[gene] = ok

        os.unlink(faa_tmp)
        return acc, results

    except Exception as e:
        return acc, f"ERROR: {e}"

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    meta = pd.read_csv(META, sep="\t", dtype=str)
    accessions = meta["accession"].tolist()

    # Build genome path map
    print("Building genome path index...")
    fna_map = {}
    for fna in GENOME_DIR.rglob("*.fna"):
        acc = fna.stem
        fna_map[acc] = fna

    jobs = [(acc, fna_map[acc]) for acc in accessions if acc in fna_map]
    missing = [acc for acc in accessions if acc not in fna_map]

    print(f"Genomes to process: {len(jobs)}")
    print(f"Not found in raw/: {len(missing)}")
    print(f"Workers: {MAX_WORKERS} (×{THREADS_PER} hmmsearch threads each)")
    print()

    success = 0
    errors  = 0

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(process_genome, acc, fna): acc
                   for acc, fna in jobs}

        for i, fut in enumerate(as_completed(futures), 1):
            acc, result = fut.result()
            if isinstance(result, dict):
                success += 1
            elif result == "skipped":
                success += 1
            else:
                errors += 1
                print(f"  WARN [{acc}]: {result}")

            if i % 500 == 0:
                print(f"[{i}/{len(jobs)}] done={success} errors={errors}")

    print(f"\n=== hmmsearch complete ===")
    print(f"Success: {success}")
    print(f"Errors:  {errors}")

    # Quick stats per gene
    print()
    for gene in GENES:
        n = len(list((OUT_DIR / gene).glob("*.tbl")))
        print(f"  {gene}: {n} result files")
