# Yersinia Pangenomics — One Health

## Overview
Genus-wide pangenomic analysis of *Yersinia* (28 species, ~10,000 genomes)
integrating One Health metadata, antimicrobial resistance mobilome
characterization, and marker gene evaluation for surveillance.

## Research questions
1. Do surveillance-neglected *Yersinia* species harbor novel conjugative
   plasmids carrying AMR genes undetectable by current markers?
2. Which single-gene markers best capture genus-wide phylogenetic diversity?
3. Is there active inter-niche AMR gene flow across One Health interfaces?

## Project structure
yersinia-pangenomics/
├── 01_metadata/          # NCBI metadata download and One Health curation
├── 02_genomes/           # Downloaded genomes (raw and HQ-filtered)
├── 03_qc/                # CheckM2 and GUNC quality control
├── 04_annotation/        # Bakta standardized annotation
├── 05_taxonomy/          # FastANI, GTDB-Tk, EzAAI
├── 06_phylogeny/         # RAxML-NG, IQ-TREE2, PopPUNK, ClonalFrameML
├── 07_markers/           # Marker gene evaluation (16S, rpoB, gyrB, recA, atpD, fusA)
├── 08_pangenome/         # PPanGGOLiN, RIBAP, Panaroo
├── 09_resistome_mobilome/# AMRFinderPlus, MOBsuite, Platon, IntegronFinder
├── 10_gwas/              # Scoary2, Pyseer
├── 11_phylo_stats/       # D statistic, ancestral reconstruction
├── 12_results/           # Final tables and figures
├── panmob/               # PanMob Python toolkit (developed in parallel)
└── scripts/              # Analysis scripts per phase

## Conda environments
| Environment | Tools | Status |
|---|---|---|
| `yersinia_pan` | Main environment (most tools) | Pending |
| `mob_suite` | MOBsuite + AMRFinderPlus | Available |
| `gunc` | GUNC | Pending |
| `platon` | Platon v1.7 | Pending |
| `scoary2` | Scoary2 + R | Pending |
| `pyseer` | Pyseer | Pending |

## Genome selection rule
- BioSample with GCF available → use GCF (RefSeq)
- BioSample with GCA only → use GCA (GenBank)
- MAGs and atypical assemblies → excluded (`--exclude-atypical`)

## Species dataset (NCBI, May 2026)
Total: 10,048 unique BioSamples across 28 species
Estimated post-QC (CheckM2 ≥95%/≤5% + GUNC CSS ≤0.45): ~6,000–6,200

## Tools and versions
See `scripts/00_tool_versions.sh` for complete version tracking.

## Data availability
- Raw genomes: downloaded from NCBI (accessions in `01_metadata/filtered/`)
- Curated metadata: deposited on Zenodo (DOI pending)
- Phylogenetic trees: deposited on TreeBASE (pending)
- PanMob toolkit: github.com/[username]/panmob

## Citation
Pending

## License
MIT
