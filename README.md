# Genus-wide One Health Pangenomics of *Yersinia*

> First genus-wide pangenomic analysis of *Yersinia* (29 species, 9,957 genomes) integrating One Health metadata, AMR mobilome characterization, marker gene evaluation, GWAS, MLST, and multi-tool mobilome architecture analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![AMR hits](https://img.shields.io/badge/AMR%20hits-20%2C966-red)]()
[![MLST](https://img.shields.io/badge/MLST-9%2C957%20genomes-orange)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## Overview

*Yersinia* encompasses 29 species (28 described + 1 novel circumpolar clade) spanning human clinical, animal, food chain, and environmental niches — from *Y. pestis*, causative agent of three historical pandemics, to zoonotic enteropathogens and free-living environmental species. This study presents the first systematic genus-wide pangenomic framework integrating all species, all niches, and all AMR gene classes, revealing a previously unknown circumpolar species invisible to all current surveillance approaches, three fundamentally distinct AMR mobilome architectures, and a striking environmental resistome paradox.

---

## Key Findings

### 1. Novel *Yersinia* Species — *Candidatus Yersinia* sp. nov. (circumpolar clade)

- **15 genomes** — ANI < 95% with all 29 described *Yersinia* species
- **Distribution**: Arctic Russia (n=10, 2006–2021) + Antarctica (n=5, 2025)
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere
- **AMR**: *blaFONA* in 1/15 genomes (GCF_052217185.1, Franz Josef Land, 2021) — HGT from *Serratia fonticola*
- **MLST**: *ypseudotuberculosis* scheme; 2/15 = ST274, 13/15 novel alleles

### 2. Complete Marker Gene Saturation

All five protein-coding markers place the novel clade sister to *Y. intermedia* despite genome-wide ANI < 75%:

| Marker | Distance to *Y. intermedia* | Status |
|---|---|---|
| rpoB | 0.0000 | **Identical** |
| fusA | 0.0000 | **Identical** |
| recA | 0.0029 | Cryptic |
| gyrB | 0.0038 | Cryptic |
| atpD | 0.0070 | Cryptic |

16S rRNA: 99.2% recovery but only 65.5% full-length (vs 100% for all protein-coding markers).

### 3. Three AMR Mobilome Architectures

| Class | Genes | Mechanism | Priority |
|---|---|---|---|
| I — Active conjugative | blaA / vat(F) | IncFII plasmid | ⚠ Surveillance 1 |
| II — Chromosomal MDR | sat2/dfrA1/floR/aadA1 | IncFII → ITR → CALIN | Monitor |
| III — Intrinsic | blaYRC | Chromosomal, no transfer | Low |

**Class I**: OR = 23–50 × (clinical/food), 50-fold post-2020 surge, IncFII shared with *E. coli*.  
**Class II**: SA cluster Brazilian pig *Y. enterocolitica*; 14 CALIN elements/genome confirmed by IntegronFinder; DTR plasmid (41 kb) + ITR transposons by geNomad.  
**Class III**: blaYRC in *Y. ruckeri* — 0 integrons, Col-type plasmids only, GWAS OR = 29,220 (species marker).

### 4. Genus-wide AMR Profiles (20,966 hits, 69 genes, 9,957 genomes)

| Species | n | %AMR | Core genes | %Plasmid |
|---|---|---|---|---|
| *Y. enterocolitica* | 5,398 | 100% | blaA, vat(F) | 60.4% |
| *Y. pestis* | 3,626 | 0.3% | — | **99.6%** |
| *Y. pseudotuberculosis* | 366 | 2.2% | — | 76.2% |
| *Y. ruckeri* | 209 | 100% | blaYRC | 42.6% |
| *Y. mollaretii* | 37 | 62.2% | — | 13.5% |
| *Ca. Y.* sp. nov. | 15 | 6.7% | — | 13.3% |
| 8 species | — | 0% | — | variable |

Notable: *Y. pestis* 99.6% plasmid prevalence (pFra/pPla/pCD1) but 0.3% AMR — no antibiotic selection in wildlife.  
Notable: *Y. mollaretii* aac(6') in 62.2% — aminoglycoside resistance in surveillance-neglected species.

### 5. MLST (9,957 genomes, 3 schemes)

| Species | Scheme | Unique STs | Dominant ST | %Typed |
|---|---|---|---|---|
| *Y. enterocolitica* | yersinia | 44 | ST18 (890), ST12 (621) | 49.4% |
| *Y. pestis* | ypseudotuberculosis | 3 | **ST90 (96.6%)** | 96.6% |
| *Y. pseudotuberculosis* | ypseudotuberculosis | 26 | ST42 (75), ST14 (56) | 88.0% |
| *Y. ruckeri* | yruckeri | — | — | 0%* |
| *Ca. Y.* sp. nov. | ypseudotuberculosis | 1 | ST274 (2/15) | 13.3% |

*yruckeri scheme incomplete in PubMLST (only 2/6 loci deposited).  
ST diversity by niche (yersinia scheme): H=66 > U=55 > A=34 > F=33 > E=20 unique STs.  
*Y. pestis* extreme clonality (ST90 = 96.6%) reflects evolutionary bottleneck.

### 6. GWAS — 330 Significant Associations

| Gene | Trait | OR | Interpretation |
|---|---|---|---|
| blaA | era_2020+ | 49.8 | 50-fold post-2020 surge |
| blaA | niche_H | 23.2 | Clinical enrichment |
| blaYRC | host_fish | 29,220 | Species identity marker |
| sat2 | geo_SA | 159.5 | SA cluster specificity |
| dfrA1 | geo_SA | 147.2 | SA cluster specificity |

Environmental niche: 69/69 AMR genes detected vs 8/69 in clinical → cryptic resistome.

### 7. Temporal and Geographic Patterns

| Era | %AMR | | Region | %AMR |
|---|---|---|---|---|
| Pre-2000 | 9.0% | | UK | 98.9% |
| 2010–14 | 82.5% | | USA | 98.3% |
| **2020+** | **96.6%** | | Russia | 10.0% |
| | | | China/Mongolia | 5.6% |

Host gradient: Fish 100% (intrinsic) > Pig 93.8% > Human 88.7% > Rodent/Marmot 1.7%.

---

## Pipeline Status

| Phase | Analysis | Tool | Status |
|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | ✅ |
| 2 | Genome download | ncbi-datasets-cli | ✅ |
| 3 | Quality control | CheckM2 v1.0.2 + GUNC v1.0.6 | ✅ |
| 4 | Annotation | Bakta v1.9.4 | 🔄 3,763/5,853 on faraday HPC |
| 5 | Species delimitation | skani v0.3.1 | ✅ |
| 6 | Phylogenomics | RAxML-NG, PopPUNK | ⏳ Pending Bakta |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | ✅ |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | ⏳ Pending Bakta |
| 9a | Resistome | AMRFinderPlus v4.x | ✅ 9,957/9,957 |
| 9b | Plasmid reconstruction | MOBsuite v3.x | ✅ 9,957/9,957 |
| 9c–e | Priority mobilome | Platon + IntegronFinder + geNomad | ✅ 34 genomes |
| 10 | GWAS | Scoary2 v0.0.15 | ✅ 330 associations |
| 11 | Phylogenetic signal | D statistic (caper + phytools) | 🔄 Running |
| 12 | MLST | mlst v2.11 | ✅ 9,957/9,957 |

---

## Taxonomy Notes

### Species Reclassifications

11 former *Yersinia* sp. genomes reclassified (ANI ≥ 95%):

| Reclassified to | n |
|---|---|
| *Y. bercovieri* | 3 |
| *Y. entomophaga* | 2 |
| *Y. vastinensis* | 2 |
| *Y. rochesterensis* | 2 |
| *Y. enterocolitica* | 1 |
| *Y. intermedia* | 1 |

### Borderline Species Pairs

| Pair | Max ANI |
|---|---|
| *Y. alsatica* / *Y. frederiksenii* | 99.98% |
| *Y. frederiksenii* / *Y. massiliensis* | 99.94% |

### Novel Species — Geographic Subgroups

| Subgroup | n | Locations | Years |
|---|---|---|---|
| Arctic Russia | 10 | Sakha, Krasnoyarsk, Franz Josef Land, Novaya Zemlya | 2006–2021 |
| Antarctica | 5 | Galindez Is., Berthelot Is., Cape Tuxen, Yalour Is. | 2025 |

Inter-subgroup ANI: mean 98.87% → single species.

---

## Dataset

| Parameter | Value |
|---|---|
| Raw assemblies | 12,868 |
| After deduplication + suppressed removal | 10,188 |
| Post-QC (CheckM2 + GUNC) | **9,957** |
| Species (described) | 28 |
| Novel species | 1 (*Ca. Yersinia* sp. nov.) |
| One Health classified | 8,911 (87.4%) |
| Human clinical (H) | 3,955 |
| Animal (A) | 3,924 |
| Food chain (F) | 725 |
| Environmental (E) | 91 |
| Unclassified (U) | 1,262 |

---

## Methods

| Step | Tool | Version | Key parameters |
|---|---|---|---|
| Genome acquisition | ncbi-datasets-cli | — | GCF>GCA/BioSample, --exclude-atypical |
| One Health curation | Python (custom) | v4 | Priority-based BioSample inference |
| Completeness | CheckM2 | 1.0.2 | ≥95% completeness, ≤5% contamination |
| Chimerism | GUNC | 1.0.6 | progenomes_3, CSS ≤0.45 |
| Species delimitation | skani | 0.3.1 | All-vs-all ANI, threshold ≥95% |
| 16S rRNA | barrnap | 0.9 | kingdom bac |
| Protein markers | pyrodigal + hmmsearch | — | Pfam HMMs |
| Phylogenetics | IQ-TREE2 | 3.1.1 | ModelFinder BIC, UFBoot 1,000 |
| Annotation | Bakta | 1.9.4 | --db full |
| AMR screening | AMRFinderPlus | 4.x | Nucleotide mode |
| Plasmid reconstruction | MOBsuite mob_recon | 3.x | Default |
| Plasmid classification | Platon | 1.7 | Accuracy mode |
| Integron detection | IntegronFinder | 2.x | --linear |
| Mobile elements | geNomad | 1.12 | End-to-end |
| GWAS | Scoary2 | 0.0.15 | Fisher's exact, Bonferroni FWER=0.05 |
| MLST | mlst | 2.11 | Per-species forced scheme |
| Phylogenetic signal | caper + phytools | — | D statistic, 1,000 permutations |

---

## Conda Environments

| Environment | Tools |
|---|---|
| `yersinia_pan` | skani, barrnap, HMMER, MAFFT, pyrodigal, IQ-TREE2, platon, mlst, R (caper, phytools) |
| `checkm2` | CheckM2 v1.0.2 |
| `gunc` | GUNC v1.0.6 |
| `bakta` | Bakta v1.9.4 |
| `amrfinder` | AMRFinderPlus v4.x |
| `mobsuite` | MOBsuite v3.x |
| `integron` | IntegronFinder v2.x |
| `genomad` | geNomad v1.12 |
| `scoary-2` | Scoary2 v0.0.15, Python/pandas |

---

## Repository Structure

```
yersinia-pangenomics/
├── 01_metadata/               # Metadata + One Health curation
├── 02_genomes/
│   ├── hq/                    # HQ metadata + accession list
│   └── raw/                   # 9,957 genome FASTA files
├── 03_qc/                     # CheckM2 + GUNC results
├── 05_taxonomy/skani/         # ANI results + novel species files
├── 07_markers/                # Marker gene evaluation + trees
├── 09_resistome_mobilome/     # AMR + plasmid + integron + geNomad
├── 10_gwas/                   # Scoary2 results (330 associations)
├── 11_phylo_stats/            # D statistic analysis
├── 12_results/
│   └── mlst/                  # MLST results (9,957 genomes, 3 schemes)
└── scripts/                   # Analysis scripts (01–12)
```

---

## References

1. Shaw & Yu (2023). skani. *Nature Methods* 20:1500–1505.
2. Chklovski et al. (2023). CheckM2. *Nature Methods* 20:1203–1212.
3. Orakov et al. (2021). GUNC. *Genome Biology* 22:1–19.
4. Schwengers et al. (2021). Bakta. *Microbial Genomics* 7:e000685.
5. Jain et al. (2018). ANI boundaries. *Nature Communications* 9:5114.
6. Nguyen et al. (2015). IQ-TREE. *Mol. Biol. Evol.* 32:268–274.
7. Kalyaanamoorthy et al. (2017). ModelFinder. *Nature Methods* 14:587–589.
8. Bohme et al. (2023). Scoary2. *Genome Biology* 24:84.
9. Fritz & Purvis (2010). D statistic. *Conservation Biology* 24:1042–1051.
10. Schwengers et al. (2021). Platon. *Microbial Genomics* 7:e000656.
11. Robertson & Nash (2018). MOBsuite. *Microbial Genomics* 4:e000206.
12. Cury et al. (2016). IntegronFinder. *Nucleic Acids Research* 44:4539–4550.
13. Camargo et al. (2023). geNomad. *Nature Biotechnology* 41:1783–1795.
14. Gautreau et al. (2020). PPanGGOLiN. *PLoS Comp. Biol.* 16:e1007732.
15. Seemann T (2014). mlst. GitHub: tseemann/mlst.
16. Achtman et al. (1999). *Yersinia pestis* MLST. *PNAS* 96:14043–14048.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

## License

MIT — see [LICENSE](LICENSE)

---

**Contact**: Francisco Cabezas-Mera | [@fcabezasmera](https://github.com/fcabezasmera)  
**Repository**: [github.com/fcabezasmera/yersinia-pangenomics](https://github.com/fcabezasmera/yersinia-pangenomics)

---

*Last updated: May 16, 2026 | Phases 1–3, 5, 7, 9a–e, 10, 12 complete | D statistic running | Bakta 3,763/5,853 on faraday HPC*
