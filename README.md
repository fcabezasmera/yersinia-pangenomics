# Genus-wide One Health Pangenomics of *Yersinia*

> **Genus-wide pangenomic analysis of *Yersinia* (29 species including novel circumpolar clade, 9,957 genomes) integrating One Health metadata, antimicrobial resistance mobilome characterization, marker gene evaluation, and GWAS for genomic surveillance.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![Status](https://img.shields.io/badge/Status-Phase%2010%20In%20Progress-orange)]()

---

## Major Findings

### 1. Novel *Yersinia* Species Discovered — *Candidatus Yersinia* sp. nov. (circumpolar clade)

A previously unknown *Yersinia* species formally identified through genus-wide ANI-based species delimitation:

- **15 genomes**, ANI < 95% with all 29 described *Yersinia* species
- **Intra-group ANI**: 97.61–99.99% (mean 98.82%) → single coherent species
- **Geographic distribution**: Circumpolar — Arctic Russia (10 genomes, 2006–2021) + Antarctica (5 genomes, 2025)
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere habitats
- **Temporal span**: 19 years (2006–2025)
- **Assembly quality**: All GCF RefSeq, contig-level
- **Formal status**: Meets ANI criterion; phenotypic characterization required per IJSEM guidelines

### 2. Complete Marker Gene Saturation — Central Finding of Paper 1

**The circumpolar novel species is phylogenetically invisible to all single-gene surveillance approaches:**

| Marker | Distance to *Y. intermedia* | Status |
|---|---|---|
| rpoB | 0.0000 | **IDENTICAL** |
| fusA | 0.0000 | **IDENTICAL** |
| recA | 0.0029 | Cryptic |
| gyrB | 0.0038 | Cryptic |
| atpD | 0.0070 | Cryptic |

Yet genome-wide ANI between the novel clade and *Y. intermedia* is **< 75%** (below skani reporting threshold, indicating > 25% divergence). This represents complete saturation of phylogenetic signal in all marker genes evaluated — the novel species would be systematically misclassified as *Y. intermedia* by any current surveillance framework.

### 3. AMR Resistome Profiling (9,957 Genomes)

- **69 unique AMR genes** detected (AMRFinderPlus, nucleotide mode)
- **57.1%** of genomes carry ≥1 AMR gene (mean burden: 1.22 genes/genome)
- Dominant genes: blaA (54.4%), vat(F) (53.1%), blaYRC (2.2%), tet(A) (1.0%)
- blaA/vat(F) co-occurrence suggests plasmid-linked dissemination in *Y. enterocolitica*

### 4. Marker Gene Performance — 16S rRNA vs Protein-Coding Markers

| Marker | Recovery | Full-length |
|---|---|---|
| 16S rRNA | 99.2% | **65.5%** ← fragmentation problem |
| rpoB | **100.0%** | N/A |
| gyrB | **100.0%** | N/A |
| recA | **100.0%** | N/A |
| atpD | **100.0%** | N/A |
| fusA | **100.0%** | N/A |

34.5% of 16S sequences are partial in HQ genomes — protein-coding markers are more robust for surveillance in draft-quality genome collections.

---

## Table of Contents

1. [Background](#background)
2. [Research Questions](#research-questions)
3. [Dataset](#dataset)
4. [Analysis Pipeline Status](#analysis-pipeline-status)
5. [Methods Summary](#methods-summary)
6. [Repository Structure](#repository-structure)
7. [References](#references)
8. [Data Availability](#data-availability)

---

## Background

*Yersinia* is a paradigmatic One Health genus comprising 29 species (28 described + 1 novel circumpolar clade), distributed across human clinical, animal, food/food chain, and environmental niches — from *Y. pestis*, causative agent of three historical pandemics, to zoonotic enteropathogens and environmental free-living species.

Despite its medical and ecological importance, *Yersinia* lacks a systematic genus-wide pangenomic framework integrating all species, all niches, and all AMR gene classes. This study presents the first such analysis, revealing novel diversity and surveillance blind spots with direct public health implications.

---

## Research Questions

1. Do surveillance-neglected *Yersinia* species harbor AMR genes undetectable by current marker-based approaches?

2. Which single-gene markers (16S rRNA, *rpoB*, *gyrB*, *recA*, *atpD*, *fusA*) best capture genus-wide phylogenetic diversity?

3. Is there active inter-niche AMR gene flow across One Health interfaces?

4. What previously unknown *Yersinia* diversity exists at environmental extremes?

---

## Dataset

| Parameter | Value |
|---|---|
| Total assemblies downloaded | 10,195 unique BioSamples |
| After suppressed removal | 10,188 |
| Post-QC (CheckM2 + GUNC) | **9,957 HQ genomes** |
| Species | **29** (28 described + 1 novel) |
| One Health classified | 8,911 (87.4%) |
| Mean genome size | 4.66 Mb |
| Mean completeness | 100.00% |
| Mean contamination | 0.78% |

### One Health Distribution

| Niche | n | % |
|---|---|---|
| Human clinical (H) | 3,955 | 39.7% |
| Animal (A) | 3,924 | 39.4% |
| Unclassified (U) | 1,262 | 12.7% |
| Food/food chain (F) | 725 | 7.3% |
| Environmental (E) | 91 | 0.9% |

### Taxonomy Reclassifications

11 former *Yersinia* sp. genomes reclassified based on ANI ≥ 95%: *Y. bercovieri* (3), *Y. entomophaga* (2), *Y. vastinensis* (2), *Y. rochesterensis* (2), *Y. enterocolitica* (1), *Y. intermedia* (1).

Borderline species pairs: *Y. alsatica / Y. frederiksenii* (max ANI 99.98%), *Y. frederiksenii / Y. massiliensis* (max ANI 99.94%).

---

## Analysis Pipeline Status

| Phase | Analysis | Tool(s) | Status | Notes |
|---|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | ✅ | 10,195 → 10,188 assemblies |
| 2 | Genome download | ncbi-datasets-cli | ✅ | 10,188 genomes, 45 GB |
| 3 | Quality control | CheckM2 v1.0.2, GUNC v1.0.6 | ✅ | 9,957 HQ genomes |
| 4 | Standardized annotation | Bakta v1.9.4 | 🔄 | ~3,028/5,853 pending (faraday HPC) |
| 5 | Species delimitation (ANI) | skani v0.3.1 | ✅ | 29 species, 1 novel discovered |
| 6 | Phylogenomics | RAxML-NG, PopPUNK | ⏳ | Pending Bakta + PopPUNK install |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | ✅ | Critical finding: marker saturation |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | ⏳ | Pending Bakta completion |
| 9a | Resistome screening | AMRFinderPlus v4.x | ✅ | 9,957/9,957 genomes |
| 9b | Plasmid reconstruction | MOBsuite v3.x | ✅ | 9,957/9,957 genomes |
| 9c | Genomic islands | IntegronFinder, IslandPath | ⏳ | Pending |
| 10 | GWAS | Scoary2 v0.0.15 | 🔄 | Running: AMR gene × niche |
| 11 | Phylo statistics | D statistic, ancestral reconstruction | ⏳ | Pending tree + pangenome |

---

## Methods Summary

### Genome acquisition and selection

Genomes downloaded from NCBI GenBank/RefSeq (May 2026) using `ncbi-datasets-cli`. For each unique BioSample, RefSeq (GCF) assemblies preferred over GenBank (GCA). MAGs excluded via `--exclude-atypical`.

**Selection rule:** GCF > GCA per BioSample; MAGs excluded.

### One Health metadata curation (v4)

Priority-based assignment to four One Health categories (H/A/F/E) using NCBI BioSample fields: 87.4% classified; 12.7% unclassifiable [U] due to absent metadata.

### Quality control

CheckM2 v1.0.2 (completeness ≥95%, contamination ≤5%) + GUNC v1.0.6 progenomes_3 (CSS ≤0.45). 27 GUNC false positives retained (CheckM2 HQ, species underrepresented in DB); 4 genuine failures excluded.

### Species delimitation

skani v0.3.1 all-vs-all ANI (9,957 × 9,957 = 99,141,849 pairs). Species threshold: ANI ≥ 95% [Jain et al. 2018]. Novel species criterion: ANI < 95% with all described species AND ANI ≥ 95% within candidate clade.

### Marker gene evaluation

**16S rRNA**: barrnap v0.9 (kingdom bac, E-value ≤ 1e-6). Recovery: 9,882/9,957 (99.2%); full-length (≥1400 bp): 65.5%.

**Protein-coding markers** (rpoB, gyrB, recA, atpD, fusA): pyrodigal (gene prediction) + hmmsearch (Pfam HMM profiles, E-value ≤ 1e-10) + MAFFT alignment + trimal trimming. Recovery: 100% for all 5 markers.

**Phylogenetic reconstruction**: IQ-TREE2 v3.1.1 with ModelFinder (BIC criterion). Models selected on representative dataset (n=124, 5 genomes/species): rpoB: LG+I; gyrB: Q.PLANT+I+G4; recA: FLAVI+I; atpD: Q.PLANT+I+R2; fusA: LG+I+R2. UFBoot: 1,000 replicates.

**Alignment lengths (post-trimal trimming)**:
- rpoB: 1,534 → 1,404 aa (91.5% retained)
- gyrB: 911 → 802 aa (88.0%)
- recA: 365 → 353 aa (96.7%)
- atpD: 620 → 434 aa (70.0%)
- fusA: 832 → 666 aa (80.0%)

### Antimicrobial resistance screening

AMRFinderPlus v4.x in nucleotide mode (generic *Yersinia*, no organism specification). All 9,957 HQ genomes screened; results: `09_resistome_mobilome/amrfinder/`.

### Plasmid reconstruction

MOBsuite v3.x `mob_recon` on all 9,957 HQ genomes. Results: `09_resistome_mobilome/mobsuite/`.

### GWAS

Scoary2 v0.0.15, Fisher's exact test with Bonferroni correction (FWER = 0.05). Genotype matrix: AMR gene presence/absence (4 genes ≥1% prevalence). Phenotype contrasts: niche_H, niche_A, niche_F, niche_E (binary).

---

## Repository Structure

```
yersinia-pangenomics/
│
├── 01_metadata/                          # Metadata acquisition and curation
├── 02_genomes/hq/                        # HQ genome metadata (9,957 genomes)
├── 03_qc/                                # CheckM2 + GUNC results
├── 04_annotation/bakta/                  # Bakta annotations (4,104 + pending)
│
├── 05_taxonomy/skani/                    # ANI analysis
│   ├── skani_allvsall.txt                # 99M pairs, 28 GB
│   ├── skani_species_level.tsv           # 45M pairs ANI ≥ 95%
│   ├── novel_species_formal.json         # Circumpolar clade description
│   └── novel_species_candidates.tsv
│
├── 07_markers/                           # Marker gene evaluation
│   ├── barrnap/                          # 16S rRNA extraction
│   ├── hmmsearch/                        # Protein marker detection
│   ├── sequences/                        # Per-gene FASTA (9,957 × 5 genes)
│   ├── alignments_trimmed/               # MAFFT + trimal alignments
│   ├── trees/                            # IQ-TREE2 treefiles
│   ├── novel_species_CRITICAL_FINDING.txt
│   └── novel_species_marker_finding.json
│
├── 09_resistome_mobilome/
│   ├── amrfinder/                        # AMRFinderPlus (9,957 ✓)
│   └── mobsuite/                         # MOBsuite plasmid reconstruction (9,957 ✓)
│
├── 10_gwas/                              # GWAS analyses
│   ├── gene_presence_absence.tsv         # Genotype matrix
│   ├── phenotype_matrix.tsv              # One Health phenotypes
│   ├── traits_scoary2.csv                # Scoary2 traits input
│   ├── genes_scoary2.csv                 # Scoary2 genes input
│   └── scoary2_results/                  # Scoary2 output (running)
│
├── scripts/                              # Analysis scripts per phase
└── README.md                             # This file
```

---

## Conda Environments

| Environment | Tools | Use |
|---|---|---|
| `yersinia_pan` | ncbi-datasets-cli, skani, barrnap, HMMER, MAFFT, pyrodigal, IQ-TREE2 | Core analyses |
| `checkm2` | CheckM2 v1.0.2 | QC |
| `gunc` | GUNC v1.0.6 | Chimerism detection |
| `bakta` | Bakta v1.9.4 | Annotation |
| `amrfinder` | AMRFinderPlus v4.x | AMR screening |
| `mobsuite` | MOBsuite v3.x | Plasmid reconstruction |
| `skani` | skani v0.3.1 | ANI calculation |
| `scoary-2` | Scoary2 v0.0.15 | GWAS |

---

## Key References

1. Shaw, J. & Yu, Y.W. (2023). Rapid and accurate distance-based phylogenetic inference using skani. *Nature Methods*, 20:1500–1505.
2. Chklovski, A. et al. (2023). CheckM2. *Nature Methods*, 20:1203–1212.
3. Orakov, A. et al. (2021). GUNC. *Genome Biology*, 22:1–19.
4. Schwengers, O. et al. (2021). Bakta. *Microbial Genomics*, 7:e000685.
5. Jain, C. et al. (2018). High throughput ANI analysis. *Nature Communications*, 9:5114.
6. Nguyen, L.T. et al. (2015). IQ-TREE. *Molecular Biology and Evolution*, 32:268–274.
7. Kalyaanamoorthy, S. et al. (2017). ModelFinder. *Nature Methods*, 14:587–589.
8. Bohme, K. et al. (2023). Scoary2. *Genome Biology*, 24:84.
9. Gautreau, G. et al. (2020). PPanGGOLiN. *PLoS Computational Biology*, 16:e1007732.
10. Fritz, S.A. & Purvis, A. (2010). D statistic. *Conservation Biology*, 24:1042–1051.

---

## Data Availability

| Data | Repository | Status |
|---|---|---|
| Genome accessions | NCBI GenBank/RefSeq | Public |
| Curated One Health metadata | Zenodo | In preparation |
| ANI distance matrix | Zenodo | In preparation |
| Marker gene alignments + trees | Zenodo | In preparation |
| AMR gene tables | Zenodo | In preparation |
| Plasmid characterization | Zenodo | Pending |
| PanMob toolkit | GitHub + Zenodo | In development |

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

## License

MIT License — see LICENSE file.

---

**Last updated:** May 15, 2026  
**Current status:** Phase 10 running (Scoary2 GWAS) | Bakta ~52% on faraday HPC
