# Genus-wide One Health Pangenomics of *Yersinia*

> **Genus-wide pangenomic analysis of *Yersinia* (29 species including novel circumpolar clade, ~10,000 genomes) integrating One Health metadata, antimicrobial resistance mobilome characterization, and marker gene evaluation for genomic surveillance.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![Status](https://img.shields.io/badge/Status-Phase%209%20In%20Progress-orange)]()

---

## Major Finding

### Novel *Yersinia* Species Discovered via Pangenomic Analysis

**Candidatus *Yersinia* sp. nov. (circumpolar clade)**

A previously unknown *Yersinia* species has been formally identified through genus-wide ANI-based species delimitation:

- **15 genomes** with ANI < 95% with all 27 described *Yersinia* species
- **Intra-group ANI**: 97.61–99.99% (mean 98.82%) → single coherent species
- **Geographic distribution**: Circumpolar (Arctic Russia + Antarctica)
- **Temporal span**: 2006–2025 (19-year collection history)
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere habitats
- **Arctic subsample** (10 genomes): Russia — Sakha, Krasnoyarsk, Karelia, Franz Josef Land, Novaya Zemlya
- **Antarctic subsample** (5 genomes): 2025 expeditions — Galindez Island, Berthelot Island, Cape Tuxen, Yalour Island
- **Assembly quality**: All GCF RefSeq, contig-level
- **Formal status**: Meets ANI criterion (< 95% with described species); phenotypic characterization required per IJSEM guidelines

This discovery exemplifies the power of genus-level pangenomic approaches for identifying overlooked biodiversity in understudied branches of medically relevant taxa.

---

## Table of Contents

1. [Background](#background)
2. [Research Questions](#research-questions)
3. [Dataset](#dataset)
4. [Major Findings](#major-findings)
5. [Methods Summary](#methods-summary)
6. [Analysis Pipeline Status](#analysis-pipeline-status)
7. [Repository Structure](#repository-structure)
8. [References](#references)
9. [Data Availability](#data-availability)

---

## Background

*Yersinia* is a paradigmatic One Health genus comprising 28 described species plus the newly identified circumpolar clade, distributed across human clinical, animal, food/food chain, and environmental niches — from *Y. pestis*, causative agent of three historical pandemics, to zoonotic enteropathogens and environmental free-living species.

This study presents the first genus-wide pangenomic analysis of *Yersinia*, integrating:
- Structured One Health metadata curation
- Systematic AMR mobilome characterization
- Marker gene evaluation for surveillance utility
- Species delimitation via ANI and novel species identification
- Plasmid reconstruction and mobilome profiling

---

## Research Questions

1. Do surveillance-neglected *Yersinia* species harbor novel conjugative plasmids carrying AMR genes undetectable by current marker-based surveillance approaches?

2. Which single-gene markers (16S rRNA, *rpoB*, *gyrB*, *recA*, *atpD*, *fusA*) best capture genus-wide phylogenetic diversity for environmental and clinical surveillance?

3. Is there active inter-niche AMR gene flow across One Health interfaces, and can phylogenetic dispersal statistics (D statistic) identify genes under active horizontal transfer?

4. What previously unknown *Yersinia* diversity exists at environmental extremes (cryosphere, permafrost)?

---

## Dataset

### Summary Statistics

| Parameter | Value |
|---|---|
| Total assemblies downloaded (NCBI, May 2026) | 10,195 unique BioSamples |
| After removal of suppressed assemblies | 10,188 |
| Post-QC: CheckM2 + GUNC | **9,957 HQ genomes** |
| **Species** | **29** (28 described + 1 novel) |
| One Health classified (H + A + F + E) | 8,911 (87.4%) |
| Genome size (mean) | 4.66 Mb |
| Completeness (mean) | 100.00% |
| Contamination (mean) | 0.78% |

### Updated Species Distribution

| Species | HQ | H | A | F | E | U | % classified |
|---|---|---|---|---|---|---|---|
| *Y. enterocolitica* | 5,398 | 3,597 | 609 | 705 | 66 | 500 | 91.1% |
| *Y. pestis* | 3,626 | 277 | 3,013 | 1 | 3 | 353 | 90.3% |
| *Y. pseudotuberculosis* | 366 | 28 | 70 | 6 | 0 | 257 | 28.3% |
| *Y. ruckeri* | 209 | 1 | 191 | 0 | 3 | 15 | 92.9% |
| *Y. kristensenii* | 53 | 4 | 9 | 3 | 3 | 34 | 38.2% |
| *Y. intermedia* | 49 | 5 | 10 | 7 | 7 | 19 | 60.4% |
| *Y. mollaretii* | 37 | 4 | 5 | 0 | 0 | 28 | 24.3% |
| *Y. bercovieri* | 24 | 5 | 2 | 1 | 1 | 12 | 50.0% |
| *Y. frederiksenii* | 22 | 8 | 2 | 2 | 4 | 9 | 64.0% |
| **Ca. *Y. sp. nov.* (circumpolar)** | **15** | 0 | 0 | 0 | 15 | 0 | 100% |
| Other 18 species | 158 | — | — | — | — | — | — |
| **TOTAL** | **9,957** | 3,929 | 3,903 | 725 | 102 | 1,284 | 87.4% |

---

## Major Findings

### 1. Novel Species Discovery

**Candidatus *Yersinia* sp. nov. (circumpolar clade)** — 15 genomes, circumpolar distribution, environmental origin. See dedicated section above.

### 2. Genus Reclassifications

**11 former *Yersinia* sp.* genomes reclassified** to described species based on ANI ≥ 95%:
- 3 → *Y. bercovieri*
- 2 → *Y. entomophaga*
- 2 → *Y. vastinensis*
- 2 → *Y. rochesterensis*
- 1 → *Y. enterocolitica*
- 1 → *Y. intermedia*

### 3. Borderline Species Pairs

**Fronteras de especie taxonómicas borrosas** (ANI 95–99.98%):
- *Y. alsatica* / *Y. frederiksenii* (max ANI 99.98%)
- *Y. frederiksenii* / *Y. massiliensis* (max ANI 99.94%)

These represent putative species complexes requiring further investigation.

### 4. Antimicrobial Resistance Profiling

**AMRFinderPlus screening** (nucleotide mode) completed on all 9,957 HQ genomes:
- 9,957/9,957 genomes screened ✓
- Summary statistics pending (MOBsuite in parallel)
- Results: `09_resistome_mobilome/amrfinder/`

---

## Methods Summary

### Genome acquisition and selection

Genomes were downloaded from NCBI GenBank/RefSeq (May 2026) using `ncbi-datasets-cli`. For each unique BioSample, RefSeq assemblies (GCF) were preferred over GenBank (GCA). MAGs and atypical assemblies excluded via `--exclude-atypical`. Seven assemblies subsequently suppressed by NCBI were removed.

**Genome selection rule:** GCF > GCA per BioSample; MAGs excluded.

### One Health metadata curation (v4)

Isolation source, host, and environmental metadata retrieved from NCBI BioSample and assigned to four One Health categories using priority-based framework:

1. NCBI `source_type` pre-classification
2. Host field keywords (ENVO/MeSH)
3. Isolation source field keywords
4. `collected_by` institution field (medium confidence)

**Result:** 8,911 genomes classified (87.4%); 1,284 unclassifiable [U] due to absent public metadata.

### Quality control

- **CheckM2 v1.0.2**: completeness ≥95%, contamination ≤5% (MIMAG isolate thresholds) → 9,957 pass
- **GUNC v1.0.6** (progenomes_3): CSS ≤0.45 → 31 failures
  - 27 false positives (CheckM2 HQ; species underrepresentation in DB) → **retained**
  - 4 genuine failures → **excluded**

### Species delimitation

**skani v0.3.1** all-vs-all ANI:
- 9,957 HQ genomes analyzed
- 45,154,039 pairs at ANI ≥ 95% (species threshold)
- Species boundaries: ANI ≥ 95% [Jain et al. 2018]
- Novel species candidates: ANI < 95% with all described species, ≥ 95% within clade

### Antimicrobial resistance screening

**AMRFinderPlus v4.x** (nucleotide mode):
- All 9,957 HQ genomes screened
- No organism specification (generic *Yersinia* mode)
- Output: individual `{accession}_amr.tsv` files

### Plasmid reconstruction (in progress)

**MOBsuite v3.x** `mob_recon`:
- Running on all 9,957 HQ genomes
- Outputs: contig reports, circular sequences, plasmid classifications

---

## Analysis Pipeline Status

| Phase | Analysis | Tool(s) | Version | Status | Genomes |
|---|---|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | — | ✅ | 10,195 → 10,188 |
| 2 | Genome download | ncbi-datasets-cli | — | ✅ | 10,188 |
| 3 | Quality control | CheckM2, GUNC | 1.0.2, 1.0.6 | ✅ | 9,957 HQ |
| 4 | Standardized annotation | Bakta | 1.9.4 | 🔄 | 4,104/9,957 |
| 5 | Species delimitation (ANI) | skani | 0.3.1 | ✅ | 9,957 |
| 6 | Phylogenomics | RAxML-NG, PopPUNK, ClonalFrameML | — | ⏳ | pending |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | — | ⏳ | pending |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | — | ⏳ | pending |
| 9a | Resistome screening | AMRFinderPlus | 4.x | ✅ | 9,957 |
| 9b | Plasmid reconstruction | MOBsuite | 3.x | 🔄 | in progress |
| 9c | Genomic islands | IntegronFinder, IslandPath | — | ⏳ | pending |
| 10 | GWAS | Scoary2, Pyseer | — | ⏳ | pending |
| 11 | Phylo statistics | D statistic, ancestral reconstruction | — | ⏳ | pending |

---

## Repository Structure

```
yersinia-pangenomics/
│
├── 01_metadata/                          # Metadata acquisition and curation
│   ├── raw/                              # NCBI downloads
│   ├── filtered/                         # 10,188 unique assemblies
│   └── onehealth/                        # Curated One Health assignments (v4)
│
├── 02_genomes/                           # Genome sequences
│   ├── raw/                              # 10,188 .fna files by species (45 GB)
│   └── hq/                               # 9,957 HQ genomes post-QC
│
├── 03_qc/                                # Quality control results
│   ├── checkm2/                          # CheckM2 v1.0.2 results
│   ├── gunc/                             # GUNC v1.0.6 results
│   └── excluded_genomes.tsv              # Excluded genomes + reasons
│
├── 04_annotation/
│   └── bakta/                            # Bakta annotations (4,104/9,957 ✓)
│
├── 05_taxonomy/
│   └── skani/                            # ANI distance matrix & species analysis
│       ├── skani_allvsall.txt            # 99M pairs, 28 GB
│       ├── skani_species_level.tsv       # 45M pairs ANI >= 95%
│       ├── intraspecies_ani_stats.tsv    # Per-species ANI ranges
│       ├── borderline_species_pairs.tsv  # Putative species complexes
│       ├── yersinia_sp_reclassification.tsv
│       ├── novel_species_candidates.tsv
│       └── novel_species_formal.json     # Circumpolar clade formal description
│
├── 06_phylogeny/                         # Phylogenomics (pending)
├── 07_markers/                           # Marker evaluation (pending)
├── 08_pangenome/                         # Pangenomics (pending)
│
├── 09_resistome_mobilome/
│   ├── amrfinder/                        # AMRFinderPlus results (9,957 ✓)
│   ├── mobsuite/                         # MOBsuite reconstruction (in progress)
│   ├── platon/                           # Plasmid predictions (pending)
│   ├── icefinder/                        # ICE detection (pending)
│   ├── integron_finder/                  # Integron detection (pending)
│   └── islandpath/                       # Genomic islands (pending)
│
├── 10_gwas/                              # GWAS analyses (pending)
├── 11_phylo_stats/                       # Phylogenetic statistics (pending)
│
├── scripts/                              # Analysis scripts per phase
│   ├── 01_filter_metadata.py
│   ├── 02_onehealth_curation.py
│   ├── 03_download_genomes.sh
│   ├── 09a_run_amrfinder.sh
│   └── 09b_run_mobsuite.sh
│
├── panmob/                               # PanMob Python toolkit (in development)
├── logs/                                 # Execution logs (gitignored)
└── README.md                             # This file
```

---

## Conda Environments

| Environment | Tools | Primary use |
|---|---|---|
| `yersinia_pan` | ncbi-datasets-cli, skani, barrnap, HMMER, MAFFT | Core analyses |
| `checkm2` | CheckM2 v1.0.2 | QC |
| `gunc` | GUNC v1.0.6 | Chimerism detection |
| `bakta` | Bakta v1.9.4 | Annotation |
| `amrfinder` | AMRFinderPlus v4.x | AMR screening |
| `mobsuite` | MOBsuite v3.x | Plasmid reconstruction |
| `skani` | skani v0.3.1 | ANI calculation |

---

## Key References

1. Shaw, J. & Yu, Y.W. (2023). Rapid and accurate distance-based phylogenetic inference using skani. *Nature Methods*, 20:1500–1505.

2. Chklovski, A. et al. (2023). CheckM2: a rapid, scalable and accurate tool for assessing microbial genome quality using machine learning. *Nature Methods*, 20:1203–1212.

3. Orakov, A. et al. (2021). GUNC: detection of chimerism and contamination in prokaryotic genomes. *Genome Biology*, 22:1–19.

4. Schwengers, O. et al. (2021). Bakta: rapid and standardized annotation of bacterial genomes via a comprehensive database. *Microbial Genomics*, 7:e000685.

5. Jain, C. et al. (2018). High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries. *Nature Communications*, 9:5114.

6. Bowers, R.M. et al. (2017). Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG). *Nature Biotechnology*, 35:725–731.

7. D'Costa, V.M. et al. (2011). Antibiotic resistance is ancient. *Nature*, 477:457–461.

8. Forsberg, K.J. et al. (2012). The shared antibiotic resistome of soil bacteria and human pathogens. *Science*, 337:1107–1111.

9. Smillie, C.S. et al. (2011). Ecology drives a global network of gene exchange connecting the human microbiome. *Science*, 331:1261–1265.

10. Sheppard, S.K. et al. (2018). Convergent evolution of virulence in *Campylobacter* one decade on. *Nature Communications*, 9:2209.

11. Mather, A.E. et al. (2013). Distinguishable epidemics of multidrug-resistant *Salmonella* Typhimurium DT104 in different hosts. *Nature Communications*, 4:2606.

12. Fritz, S.A. & Purvis, A. (2010). A new measure of phylogenetic signal strength in binary traits. *Conservation Biology*, 24:1042–1051.

13. Bohme, K. et al. (2023). Scoary2: Rapid association of phenotypic multi-omics data with microbial pan-genomes. *Genome Biology*, 24:84.

14. Gautreau, G. et al. (2020). PPanGGOLiN: Depicting microbial diversity via a partitioned pangenome graph. *PLoS Computational Biology*, 16:e1007732.

---

## Data Availability

| Data | Repository | Status |
|---|---|---|
| Genome accessions | NCBI GenBank/RefSeq | Public |
| Curated One Health metadata | Zenodo | In preparation |
| ANI distance matrix | Zenodo | In preparation |
| Phylogenetic trees | TreeBASE | Pending |
| AMR gene tables | Zenodo | In preparation |
| Plasmid characterization | Zenodo | Pending |
| PanMob toolkit | GitHub + Zenodo | In development |

All genome sequences are publicly available at NCBI GenBank/RefSeq. Accession lists available in `01_metadata/filtered/`.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species, including the discovery of a novel circumpolar clade. *Manuscript in preparation.*

---

## License

MIT License — see LICENSE file.

---

## Contact

**Francisco Cabezas-Mera**  
GitHub: [@fcabezasmera](https://github.com/fcabezasmera)  
Repository: [github.com/fcabezasmera/yersinia-pangenomics](https://github.com/fcabezasmera/yersinia-pangenomics)

---

**Last updated:** May 12, 2026  
**Current status:** Phase 9b in progress (MOBsuite reconstruction)
