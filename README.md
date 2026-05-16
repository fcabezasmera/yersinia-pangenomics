# Genus-wide One Health Pangenomics of *Yersinia*

> **Genus-wide pangenomic analysis of *Yersinia* (29 species including novel circumpolar clade, 9,957 genomes) integrating One Health metadata, antimicrobial resistance mobilome characterization, marker gene evaluation, and GWAS for genomic surveillance.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![Status](https://img.shields.io/badge/Status-Phase%2011%20In%20Progress-orange)]()

---

## Major Findings

### 1. Novel *Yersinia* Species — *Candidatus Yersinia* sp. nov. (circumpolar clade)

A previously unknown *Yersinia* species formally identified through genus-wide ANI-based species delimitation:

- **15 genomes**, ANI < 95% with all 29 described *Yersinia* species
- **Intra-group ANI**: 97.61–99.99% (mean 98.82%) → single coherent species
- **Geographic distribution**: Circumpolar — Arctic Russia (10 genomes, 2006–2021) + Antarctica (5 genomes, 2025)
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere habitats
- **Temporal span**: 19 years (2006–2025)
- **Formal status**: Meets ANI criterion (< 95% with described species); phenotypic characterization required per IJSEM guidelines

### 2. Complete Marker Gene Saturation — Central Finding of Paper 1

**The circumpolar novel species is phylogenetically invisible to all single-gene surveillance approaches:**

| Marker | Distance to *Y. intermedia* | Status |
|---|---|---|
| rpoB | 0.0000 | **IDENTICAL** |
| fusA | 0.0000 | **IDENTICAL** |
| recA | 0.0029 | Cryptic |
| gyrB | 0.0038 | Cryptic |
| atpD | 0.0070 | Cryptic |

Genome-wide ANI between the novel clade and *Y. intermedia* is **< 75%** (> 25% divergence at genome scale). The novel species would be systematically misclassified as *Y. intermedia* by any current surveillance framework based on single-gene markers.

### 3. GWAS — 330 Significant AMR Gene–Trait Associations

Scoary2 GWAS (Fisher's exact test, Bonferroni p < 0.05) on 9,957 genomes × 69 AMR genes × 21 traits:

#### 3a. blaA Clinical Enrichment and Temporal Surge

| Trait | OR | q-value |
|---|---|---|
| niche_H (Human clinical) | 23.2 | < 1e-300 |
| niche_F (Food chain) | 22.9 | 4.2e-148 |
| region_North_America | 16.4 | 4.6e-260 |
| region_Europe | 15.0 | < 1e-300 |
| host_human | 10.8 | < 1e-300 |
| host_pig | 9.8 | 6.3e-23 |
| **era_2020plus** | **49.8** | **< 1e-300** |
| era_pre2000 | 0.02 | < 1e-300 |
| niche_A (Animal wildlife) | 0.04 | < 1e-300 |

**Interpretation**: blaA is under strong positive selection in human clinical and food chain contexts, with a 50-fold temporal increase post-2020. Markedly depleted in wildlife (rodent OR=0.01, marmot OR=0.02, fish OR≈0) and Central Asia — indicating anthropogenic selection from beta-lactam use in human medicine and food animal production.

#### 3b. blaYRC — Animal-Specific β-Lactamase

| Trait | OR | q-value |
|---|---|---|
| host_fish | 29,220 | 6.7e-302 |
| niche_A | 13.5 | 5.6e-51 |
| niche_H | 0.02 | 8.8e-40 |

**Interpretation**: blaYRC is virtually exclusive to fish hosts (*Y. ruckeri*, salmonid pathogen), representing a clearly animal-restricted AMR lineage with minimal human spillover risk.

#### 3c. South America — Novel Integron/Plasmid Cluster

| Gene | OR | Function |
|---|---|---|
| sat2 | 159.5 | Streptothricin acetyltransferase |
| dfrA1 | 147.2 | Trimethoprim resistance |
| floR | 93.5 | Phenicol resistance |
| aadA1 | 68.1 | Aminoglycoside resistance |

**Interpretation**: A co-occurring multi-drug resistance gene cluster uniquely enriched in South American isolates, suggesting a regional integron or conjugative plasmid carrying resistance to 4 antibiotic classes simultaneously. Priority target for plasmid reconstruction (MOBsuite/Platon).

#### 3d. Europe — Class 1 Integron Cluster

| Gene | OR | q-value |
|---|---|---|
| aadA12 | 17.5 | 1.1e-22 |
| catA1 | 13.7 | 3.2e-21 |
| qacEdelta1 | 7.5 | 5.0e-18 |
| sul1 | 7.1 | 3.7e-17 |

**Interpretation**: The co-enrichment of aadA12, qacEdelta1, and sul1 is the hallmark signature of class 1 integrons on IncI/IncF plasmids, consistent with previously described European *Y. enterocolitica* clinical isolates.

#### 3e. Environmental Resistome Richness — Key Surveillance Finding

| Niche | Unique AMR genes | n genomes |
|---|---|---|
| Environmental (E) | **69/69** | 91 |
| Human clinical (H) | 8/69 | 3,955 |
| Animal (A) | 8/69 | 3,924 |
| Food chain (F) | 3/69 | 725 |

Despite being the smallest niche group (n=91 genomes), environmental isolates harbor **all 69 detected AMR genes** — far exceeding clinical and animal niches. This confirms the environmental niche as a cryptic AMR reservoir invisible to current surveillance. The novel circumpolar *Yersinia* sp. nov. belongs to this niche.

### 4. Marker Gene Performance — 16S rRNA vs Protein-Coding Markers

| Marker | Recovery | Full-length (≥1,400 bp) |
|---|---|---|
| 16S rRNA | 99.2% | **65.5%** ← fragmentation problem |
| rpoB | **100.0%** | N/A |
| gyrB | **100.0%** | N/A |
| recA | **100.0%** | N/A |
| atpD | **100.0%** | N/A |
| fusA | **100.0%** | N/A |

34.5% of 16S rRNA sequences are partial in HQ-quality genomes — protein-coding markers are substantially more robust for genus-wide surveillance in draft genome collections.

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
2. Which single-gene markers best capture genus-wide phylogenetic diversity?
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

### Taxonomy

- 11 former *Yersinia* sp. genomes reclassified to known species based on ANI ≥ 95%
- Borderline species pairs: *Y. alsatica / Y. frederiksenii* (max ANI 99.98%), *Y. frederiksenii / Y. massiliensis* (max ANI 99.94%)
- 1 novel species confirmed: *Candidatus Yersinia* sp. nov. (circumpolar clade)

---

## Analysis Pipeline Status

| Phase | Analysis | Tool(s) | Status | Notes |
|---|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | ✅ | 10,195 → 10,188 |
| 2 | Genome download | ncbi-datasets-cli | ✅ | 10,188 genomes |
| 3 | Quality control | CheckM2 v1.0.2, GUNC v1.0.6 | ✅ | 9,957 HQ genomes |
| 4 | Standardized annotation | Bakta v1.9.4 | 🔄 | ~52% on faraday HPC |
| 5 | Species delimitation (ANI) | skani v0.3.1 | ✅ | 29 species, 1 novel |
| 6 | Phylogenomics | RAxML-NG, PopPUNK | ⏳ | Pending Bakta |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | ✅ | Saturation finding |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | ⏳ | Pending Bakta |
| 9a | Resistome screening | AMRFinderPlus v4.x | ✅ | 9,957/9,957 |
| 9b | Plasmid reconstruction | MOBsuite v3.x | ✅ | 9,957/9,957 |
| 9c | Priority plasmid analysis | Platon | 🔄 | GWAS priority targets |
| 10 | GWAS | Scoary2 v0.0.15 | ✅ | 330 significant associations |
| 11 | Phylo statistics | D statistic, ancestral reconstruction | 🔄 | In progress |

---

## Methods Summary

### Genome acquisition and selection

Genomes downloaded from NCBI GenBank/RefSeq (May 2026) using `ncbi-datasets-cli`. GCF > GCA per BioSample; MAGs excluded via `--exclude-atypical`.

### One Health metadata curation (v4)

Priority-based assignment to four One Health categories (H/A/F/E) using NCBI BioSample fields. 87.4% classified; 12.7% unclassifiable [U].

### Quality control

CheckM2 v1.0.2 (completeness ≥95%, contamination ≤5%) + GUNC v1.0.6 progenomes_3 (CSS ≤0.45). 27 GUNC false positives retained; 4 genuine failures excluded.

### Species delimitation

skani v0.3.1 all-vs-all ANI (99,141,849 pairs). Species threshold: ANI ≥ 95% [Jain et al. 2018]. Novel species: ANI < 95% with all described species AND ≥ 95% within candidate clade.

### Marker gene evaluation

16S rRNA: barrnap v0.9 (E-value ≤ 1e-6). Protein-coding markers (rpoB, gyrB, recA, atpD, fusA): pyrodigal + hmmsearch (Pfam HMMs, E-value ≤ 1e-10) + MAFFT + trimal. IQ-TREE2 v3.1.1 with ModelFinder (BIC). Models: rpoB LG+I; gyrB Q.PLANT+I+G4; recA FLAVI+I; atpD Q.PLANT+I+R2; fusA LG+I+R2. UFBoot 1,000 replicates.

### Antimicrobial resistance

AMRFinderPlus v4.x (nucleotide mode, 9,957 genomes). MOBsuite v3.x `mob_recon` (9,957 genomes).

### GWAS

Scoary2 v0.0.15, Fisher's exact test, Bonferroni correction (FWER = 0.05). Genotype: 69 AMR genes. Traits: One Health niche, geographic region, host group, collection era, assembly completeness (21 binary traits, ≥30 positives each).

---

## Repository Structure

```
yersinia-pangenomics/
├── 01_metadata/                    # Metadata + One Health curation
├── 02_genomes/hq/                  # HQ genome metadata (9,957)
├── 03_qc/                          # CheckM2 + GUNC results
├── 04_annotation/bakta/            # Bakta annotations
├── 05_taxonomy/skani/              # ANI analysis + novel species
├── 07_markers/                     # Marker gene evaluation
│   ├── sequences/                  # 9,957 × 5 genes FASTA
│   ├── alignments_trimmed/         # MAFFT + trimal
│   ├── trees/                      # IQ-TREE2 treefiles
│   └── novel_species_CRITICAL_FINDING.txt
├── 09_resistome_mobilome/
│   ├── amrfinder/                  # 9,957 genomes ✓
│   └── mobsuite/                   # 9,957 genomes ✓
├── 10_gwas/
│   ├── scoary2_final/              # Scoary2 output
│   ├── scoary2_significant.tsv     # 330 associations
│   └── GWAS_FINDINGS.json          # Interpreted findings
├── scripts/                        # Analysis scripts
└── README.md
```

---

## Conda Environments

| Environment | Tools | Use |
|---|---|---|
| `yersinia_pan` | skani, barrnap, HMMER, MAFFT, pyrodigal, IQ-TREE2 | Core analyses |
| `checkm2` | CheckM2 v1.0.2 | QC |
| `gunc` | GUNC v1.0.6 | Chimerism detection |
| `bakta` | Bakta v1.9.4 | Annotation |
| `amrfinder` | AMRFinderPlus v4.x | AMR screening |
| `mobsuite` | MOBsuite v3.x | Plasmid reconstruction |
| `skani` | skani v0.3.1 | ANI calculation |
| `scoary-2` | Scoary2 v0.0.15 | GWAS |

---

## Key References

1. Shaw & Yu (2023). skani. *Nature Methods*, 20:1500–1505.
2. Chklovski et al. (2023). CheckM2. *Nature Methods*, 20:1203–1212.
3. Orakov et al. (2021). GUNC. *Genome Biology*, 22:1–19.
4. Schwengers et al. (2021). Bakta. *Microbial Genomics*, 7:e000685.
5. Jain et al. (2018). ANI species boundaries. *Nature Communications*, 9:5114.
6. Nguyen et al. (2015). IQ-TREE. *Molecular Biology and Evolution*, 32:268–274.
7. Kalyaanamoorthy et al. (2017). ModelFinder. *Nature Methods*, 14:587–589.
8. Bohme et al. (2023). Scoary2. *Genome Biology*, 24:84.
9. Gautreau et al. (2020). PPanGGOLiN. *PLoS Computational Biology*, 16:e1007732.
10. Fritz & Purvis (2010). D statistic. *Conservation Biology*, 24:1042–1051.

---

## Data Availability

| Data | Repository | Status |
|---|---|---|
| Genome accessions | NCBI GenBank/RefSeq | Public |
| Curated One Health metadata | Zenodo | In preparation |
| ANI distance matrix | Zenodo | In preparation |
| Marker gene alignments + trees | Zenodo | In preparation |
| AMR gene tables + GWAS results | Zenodo | In preparation |
| PanMob toolkit | GitHub + Zenodo | In development |

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

**Last updated:** May 15, 2026  
**Current status:** Phase 10 complete (GWAS) | Phase 9c + 11 in progress | Bakta ~52% on faraday HPC
