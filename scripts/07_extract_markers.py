#!/usr/bin/env python3
"""Extract marker genes (16S, rpoB, gyrB, recA, atpD, fusA) from genomes"""

import os
import subprocess
from pathlib import Path
import pandas as pd
from Bio import SeqIO

# Setup
meta = pd.read_csv('02_genomes/hq/metadata_hq.tsv', sep='\t', dtype=str)
accessions = meta['accession'].tolist()
out_dir = Path("07_markers/barrnap")
out_dir.mkdir(parents=True, exist_ok=True)

print(f"=== Extracting 16S rRNA from {len(accessions)} genomes ===\n")

success = 0
failed = 0

for i, acc in enumerate(accessions):
    if (i + 1) % 500 == 0:
        print(f"[{i+1}/{len(accessions)}] Progress: {success} genomes with 16S extracted")
    
    # Find genome file
    fna_files = list(Path("02_genomes/raw").rglob(f"{acc}.fna"))
    if not fna_files:
        failed += 1
        continue
    
    fna = fna_files[0]
    out_gff = out_dir / f"{acc}.rrna.gff"
    out_16s = out_dir / f"{acc}_16S.fasta"
    
    # Skip if already done
    if out_16s.exists():
        success += 1
        continue
    
    # Run barrnap
    cmd = f"barrnap --quiet --kingdom bac {fna} > {out_gff} 2>/dev/null"
    os.system(cmd)
    
    # Extract 16S from GFF
    if out_gff.exists() and out_gff.stat().st_size > 0:
        try:
            # Build sequence dict from genome (handles multi-contig)
            seq_dict = SeqIO.to_dict(SeqIO.parse(fna, "fasta"))
            
            # Parse GFF for 16S
            with open(out_gff) as f:
                for line in f:
                    if line.startswith("#"):
                        continue
                    parts = line.strip().split('\t')
                    if len(parts) < 9:
                        continue
                    
                    seqid = parts[0]
                    start = int(parts[3]) - 1  # GFF is 1-indexed
                    end = int(parts[4])
                    strand = parts[6]
                    feature = parts[8]
                    
                    if "16S" in feature and seqid in seq_dict:
                        seq = seq_dict[seqid].seq[start:end]
                        if strand == "-":
                            seq = seq.reverse_complement()
                        
                        # Write 16S
                        with open(out_16s, "w") as out:
                            out.write(f">{acc}_16S\n{str(seq)}\n")
                        success += 1
                        break
        except Exception as e:
            failed += 1
            pass

print(f"\n=== 16S extraction complete ===")
print(f"Success: {success}")
print(f"Failed/Missing: {failed}")
print(f"Total: {success + failed}")

