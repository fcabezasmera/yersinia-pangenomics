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

Genome-wide ANI between the novel clade and *Y. intermedia* is **< 75%** (> 25% genome-scale divergence). The novel species would be systematically misclassified as *Y. intermedia* by any current surveillance framework.

### 3. Integrated Mobilome Architecture — Three AMR Classes

Combined GWAS + MOBsuite + Platon analysis reveals three distinct AMR mobilome architectures in *Yersinia*:

#### Class I — Active Conjugative Plasmid-Borne AMR (Highest Priority)

**blaA / vat(F) on IncFII plasmids** — actively spreading in clinical *Y. enterocolitica*:

| Trait | OR | q-value |
|---|---|---|
| niche_H (Human clinical) | 23.2 | < 1e-300 |
| niche_F (Food chain) | 22.9 | 4.2e-148 |
| region_Europe | 15.0 | < 1e-300 |
| region_North_America | 16.4 | 4.6e-260 |
| **era_2020plus** | **49.8** | **< 1e-300** |

MOBsuite: IncFII backbone detected in 16/31 priority genomes. 50-fold temporal increase post-2020 indicates active ongoing selection.

#### Class II — Chromosomally Integrated MDR (Stable, Monitor)

**South American MDR cluster** (sat2/dfrA1/floR/aadA1) in Brazilian pig *Y. enterocolitica*:

| Gene | Function | OR (SA) |
|---|---|---|
| sat2 | Streptothricin acetyltransferase | 159.5 |
| dfrA1 | Trimethoprim resistance | 147.2 |
| floR | Phenicol resistance | 93.5 |
| aadA1 | Aminoglycoside resistance | 68.1 |

Platon analysis: AMR contigs show low RDS (0.2–4.6) confirming **chromosomal location**. Co-resident circular 41 kb plasmid (RDS=11.7, no AMR) supports a **hit-and-run mechanism**: historical plasmid-mediated transfer followed by stable chromosomal integron formation. Persistent MDR in pig populations but not actively spreading horizontally.

**European class 1 integron cluster** (aadA12/qacEdelta1/sul1/catA1):

| Gene | OR (Europe) | q-value |
|---|---|---|
| aadA12 | 17.5 | 1.1e-22 |
| catA1 | 13.7 | 3.2e-21 |
| qacEdelta1 | 7.5 | 5.0e-18 |
| sul1 | 7.1 | 3.7e-17 |

Hallmark signature of class 1 integrons on IncI/IncF plasmids in European clinical *Y. enterocolitica*.

#### Class III — Intrinsic Chromosomal Resistance (Low Priority)

**blaYRC in *Y. ruckeri*** — chromosomal intrinsic beta-lactamase:

- GWAS OR = 29,220 in fish hosts (extreme host specificity)
- Platon: chromosomal location (RDS 0.2–2.4, no plasmid signal)
- MOBsuite: Col(Ye4449) non-conjugative plasmids dominant
- **Classification**: intrinsic resistance, not acquired AMR
- **Clinical risk**: MINIMAL — no transfer potential detected

### 4. Environmental Resistome Richness

| Niche | AMR genes | n genomes |
|---|---|---|
| Environmental (E) | **69/69** | 91 |
| Human clinical (H) | 8/69 | 3,955 |
| Animal (A) | 8/69 | 3,924 |
| Food chain (F) | 3/69 | 725 |

Environmental isolates harbor all 69 detected AMR genes despite representing only 0.9% of the dataset. The novel circumpolar *Yersinia* sp. nov. belongs to this niche — its AMR profile is part of a cryptic environmental resistome invisible to current surveillance.

### 5. Marker Gene Performance

| Marker | Recovery | Full-length |
|---|---|---|
| 16S rRNA | 99.2% | **65.5%** ← fragmentation critical |
| rpoB | **100.0%** | N/A |
| gyrB | **100.0%** | N/A |
| recA | **100.0%** | N/A |
| atpD | **100.0%** | N/A |
| fusA | **100.0%** | N/A |

---

## Surveillance Recommendations

Based on integrated GWAS + MOBsuite + Platon analysis:

1. **Priority 1**: Monitor IncFII-associated blaA/vat(F) in clinical *Y. enterocolitica* — actively conjugating, 50-fold post-2020 increase
2. **Priority 2**: Screen European isolates for class 1 integron cluster (aadA12/qacEdelta1/sul1)
3. **Monitor**: South American chromosomal MDR in food chain pig isolates — stable but persistent
4. **Low priority**: blaYRC — intrinsic gene, no transfer risk
5. **Novel species**: environmental surveillance required — marker-based approaches cannot detect *Ca.* Yersinia sp. nov.

---

## Table of Contents

1. [Background](#background)
2. [Dataset](#dataset)
3. [Analysis Pipeline Status](#analysis-pipeline-status)
4. [Methods Summary](#methods-summary)
5. [Repository Structure](#repository-structure)
6. [References](#references)

---

## Background

*Yersinia* is a paradigmatic One Health genus comprising 29 species (28 described + 1 novel circumpolar clade), distributed across human clinical, animal, food/food chain, and environmental niches. This study presents the first genus-wide pangenomic analysis, integrating all species, all niches, and all AMR gene classes, revealing novel diversity and surveillance blind spots with direct public health implications.

---

## Dataset

| Parameter | Value |
|---|---|
| Total assemblies | 10,195 unique BioSamples |
| After suppression removal | 10,188 |
| Post-QC | **9,957 HQ genomes** |
| Species | **29** (28 described + 1 novel) |
| One Health classified | 8,911 (87.4%) |
| Mean genome size | 4.66 Mb |
| Mean completeness | 100.00% |
| Mean contamination | 0.78% |

| Niche | n | % |
|---|---|---|
| Human clinical (H) | 3,955 | 39.7% |
| Animal (A) | 3,924 | 39.4% |
| Unclassified (U) | 1,262 | 12.7% |
| Food/food chain (F) | 725 | 7.3% |
| Environmental (E) | 91 | 0.9% |

---

## Analysis Pipeline Status

| Phase | Analysis | Tool(s) | Status |
|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | ✅ |
| 2 | Genome download | ncbi-datasets-cli | ✅ |
| 3 | Quality control | CheckM2 v1.0.2, GUNC v1.0.6 | ✅ |
| 4 | Annotation | Bakta v1.9.4 | 🔄 ~52% on faraday HPC |
| 5 | Species delimitation | skani v0.3.1 | ✅ |
| 6 | Phylogenomics | RAxML-NG, PopPUNK | ⏳ Pending Bakta |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | ✅ |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | ⏳ Pending Bakta |
| 9a | Resistome screening | AMRFinderPlus v4.x | ✅ 9,957/9,957 |
| 9b | Plasmid reconstruction | MOBsuite v3.x | ✅ 9,957/9,957 |
| 9c | Priority plasmid analysis | Platon v1.7 | ✅ 22 priority genomes |
| 10 | GWAS | Scoary2 v0.0.15 | ✅ 330 associations |
| 11 | Phylo statistics | D statistic, ancestral reconstruction | ⏳ |

---

## Methods Summary

**Genome acquisition**: ncbi-datasets-cli, GCF > GCA per BioSample, MAGs excluded.

**One Health curation (v4)**: Priority-based assignment (H/A/F/E); 87.4% classified.

**QC**: CheckM2 v1.0.2 (completeness ≥95%, contamination ≤5%) + GUNC v1.0.6 progenomes_3 (CSS ≤0.45).

**Species delimitation**: skani v0.3.1 all-vs-all ANI (99,141,849 pairs); threshold ANI ≥ 95%.

**Marker genes**: barrnap v0.9 (16S rRNA) + pyrodigal + hmmsearch Pfam HMMs (protein markers) + MAFFT + trimal + IQ-TREE2 v3.1.1 (ModelFinder BIC).

**Resistome**: AMRFinderPlus v4.x nucleotide mode (9,957 genomes).

**Mobilome**: MOBsuite v3.x mob_recon (9,957 genomes) + Platon v1.7 accuracy mode (22 priority genomes).

**GWAS**: Scoary2 v0.0.15, Fisher's exact test, Bonferroni correction (FWER=0.05), 69 AMR genes × 21 traits.

---

## Repository Structure

```
yersinia-pangenomics/
├── 01_metadata/                    # Metadata + One Health curation
├── 02_genomes/hq/                  # HQ genome metadata (9,957)
├── 03_qc/                          # CheckM2 + GUNC results
├── 04_annotation/bakta/            # Bakta annotations
├── 05_taxonomy/skani/              # ANI + novel species
├── 07_markers/                     # Marker gene evaluation
│   ├── sequences/                  # 9,957 × 5 genes FASTA
│   ├── alignments_trimmed/         # MAFFT + trimal
│   ├── trees/                      # IQ-TREE2 treefiles
│   └── novel_species_CRITICAL_FINDING.txt
├── 09_resistome_mobilome/
│   ├── amrfinder/                  # 9,957 ✓
│   ├── mobsuite/                   # 9,957 ✓
│   └── platon/                     # 22 priority genomes ✓
│       ├── SA_cluster/             # Brazilian pig MDR cluster
│       ├── blaYRC/                 # Fish Y. ruckeri
│       └── PLATON_INTEGRATED_FINDINGS.json
├── 10_gwas/
│   ├── scoary2_final/              # Scoary2 output
│   ├── scoary2_significant.tsv     # 330 associations
│   ├── GWAS_FINDINGS.json          # Interpreted findings
│   └── mobilome_integration_findings.json
└── scripts/
```

---

## Conda Environments

| Environment | Tools |
|---|---|
| `yersinia_pan` | skani, barrnap, HMMER, MAFFT, pyrodigal, IQ-TREE2, platon |
| `checkm2` | CheckM2 v1.0.2 |
| `gunc` | GUNC v1.0.6 |
| `bakta` | Bakta v1.9.4 |
| `amrfinder` | AMRFinderPlus v4.x |
| `mobsuite` | MOBsuite v3.x |
| `skani` | skani v0.3.1 |
| `scoary-2` | Scoary2 v0.0.15 |

---

## References

1. Shaw & Yu (2023). skani. *Nature Methods*, 20:1500–1505.
2. Chklovski et al. (2023). CheckM2. *Nature Methods*, 20:1203–1212.
3. Orakov et al. (2021). GUNC. *Genome Biology*, 22:1–19.
4. Schwengers et al. (2021). Bakta. *Microbial Genomics*, 7:e000685.
5. Jain et al. (2018). ANI species boundaries. *Nature Communications*, 9:5114.
6. Nguyen et al. (2015). IQ-TREE. *Mol. Biol. Evol.*, 32:268–274.
7. Kalyaanamoorthy et al. (2017). ModelFinder. *Nature Methods*, 14:587–589.
8. Bohme et al. (2023). Scoary2. *Genome Biology*, 24:84.
9. Gautreau et al. (2020). PPanGGOLiN. *PLoS Comp. Biol.*, 16:e1007732.
10. Fritz & Purvis (2010). D statistic. *Conservation Biology*, 24:1042–1051.
11. Schwengers et al. (2021). Platon. *Microbial Genomics*, 7:e000656.
12. Robertson & Nash (2018). MOBsuite. *Microbial Genomics*, 4:e000206.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

**Last updated:** May 16, 2026
**Status:** Phases 1–3, 5, 7, 9a–c, 10 complete | Bakta ~52% on faraday HPC | Phases 6, 8, 11 pending
