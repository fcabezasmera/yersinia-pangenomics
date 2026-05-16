#!/usr/bin/env python3
"""
Parse hmmsearch tblout results → extract best-hit sequences per marker gene
Output: one FASTA per gene with one representative sequence per genome
"""

import os
import re
import tempfile
import subprocess
import pandas as pd
import pyrodigal
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

GENOME_DIR = Path("02_genomes/raw")
HMM_DIR    = Path("07_markers/hmm_profiles")
TBL_DIR    = Path("07_markers/hmmsearch")
OUT_DIR    = Path("07_markers/sequences")
META       = "02_genomes/hq/metadata_hq.tsv"
EVALUE_THR = 1e-10

GENES = ["rpoB", "gyrB", "recA", "atpD", "fusA"]
OUT_DIR.mkdir(parents=True, exist_ok=True)

meta = pd.read_csv(META, sep="\t", dtype=str)
acc2sp = dict(zip(meta["accession"], meta["species"]))

# Build genome path index
print("Building genome index...")
fna_map = {f.stem: f for f in GENOME_DIR.rglob("*.fna")}
print(f"  {len(fna_map)} genomes indexed")

def parse_tblout(tbl_path):
    """Parse hmmsearch --tblout → dict {protein_id: evalue}"""
    hits = {}
    with open(tbl_path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 5:
                continue
            prot_id = parts[0]
            evalue  = float(parts[4])
            if evalue <= EVALUE_THR:
                if prot_id not in hits or evalue < hits[prot_id]:
                    hits[prot_id] = evalue
    return hits

def get_proteins(acc):
    """Run pyrodigal on genome → dict {prot_id: SeqRecord}"""
    fna = fna_map.get(acc)
    if not fna:
        return {}
    records = list(SeqIO.parse(fna, "fasta"))
    orf_finder = pyrodigal.GeneFinder()
    orf_finder.train(*(bytes(r.seq) for r in records))
    proteins = {}
    for rec in records:
        genes = orf_finder.find_genes(bytes(rec.seq))
        for j, gene in enumerate(genes):
            pid = f"{rec.id}_{j+1}"
            proteins[pid] = SeqRecord(
                Seq(gene.translate()),
                id=pid, description=""
            )
    return proteins

# ── Parse per gene ─────────────────────────────────────────────────────────────
print()
summary = {}

for gene in GENES:
    print(f"=== Processing {gene} ===")
    out_fasta = OUT_DIR / f"{gene}_all.fasta"
    
    found = 0
    not_found = 0
    no_hit = 0
    records_out = []

    for i, acc in enumerate(meta["accession"]):
        tbl = TBL_DIR / gene / f"{acc}.tbl"
        if not tbl.exists():
            not_found += 1
            continue

        # Parse hits
        hits = parse_tblout(tbl)
        if not hits:
            no_hit += 1
            continue

        # Best hit protein ID
        best_prot = min(hits, key=hits.get)
        best_eval = hits[best_prot]

        # Extract protein sequence
        proteins = get_proteins(acc)
        if best_prot not in proteins:
            no_hit += 1
            continue

        seq_rec = proteins[best_prot]
        sp = acc2sp.get(acc, "Unknown").replace(" ", "_")
        
        # Rename for phylogeny: species__accession
        seq_rec.id = f"{sp}__{acc}"
        seq_rec.description = f"e={best_eval:.2e}"
        records_out.append(seq_rec)
        found += 1

        if (i+1) % 1000 == 0:
            print(f"  [{i+1}/9957] found={found}")

    # Write FASTA
    with open(out_fasta, "w") as f:
        for r in records_out:
            f.write(f">{r.id} {r.description}\n{str(r.seq)}\n")
    
    summary[gene] = {
        "found": found, "no_hit": no_hit, "not_found": not_found
    }
    print(f"  → Found: {found} | No hit: {no_hit} | Missing tbl: {not_found}")
    print(f"  → Saved: {out_fasta}")
    print()

print("=== Summary ===")
for gene, s in summary.items():
    pct = s["found"] / 9957 * 100
    print(f"  {gene:6s}: {s['found']:5d}/9957 ({pct:.1f}%)")

