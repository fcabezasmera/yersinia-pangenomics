# Genus-wide One Health Pangenomics of *Yersinia*

> **Genus-wide pangenomic analysis of *Yersinia* (28 species, ~10,000 genomes) integrating One Health metadata, antimicrobial resistance mobilome characterization, and marker gene evaluation for genomic surveillance.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-28-green)]()
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange)]()

---

## Table of Contents

1. [Background](#background)
2. [Research Questions](#research-questions)
3. [Dataset](#dataset)
4. [Repository Structure](#repository-structure)
5. [Methods Summary](#methods-summary)
6. [Analysis Pipeline Status](#analysis-pipeline-status)
7. [Conda Environments](#conda-environments)
8. [Genome Selection Rule](#genome-selection-rule)
9. [Key References](#key-references)
10. [Data Availability](#data-availability)
11. [Citation](#citation)
12. [Contact](#contact)

---

## Background

*Yersinia* is a paradigmatic One Health genus comprising 28 species distributed
across human clinical, animal, food/food chain, and environmental niches — from
*Y. pestis*, the causative agent of three historical pandemics, to zoonotic
enteropathogens and environmental free-living species. Despite its ecological
relevance, the mobilome of 26 of the 28 species remains completely uncharacterized.

This study presents the first genus-wide pangenomic analysis of *Yersinia*,
integrating structured One Health metadata, systematic AMR mobilome
characterization, and marker gene evaluation, addressing a critical gap in
genomic surveillance of this medically, veterinary, and environmentally
relevant genus.

**Central hypothesis:**
> Surveillance-neglected *Yersinia* species harbor novel conjugative plasmids
> carrying AMR genes undetectable by current marker-based approaches, and
> genus-wide pangenomics with One Health metadata reveals this cryptic reservoir
> under active selection across multiple niches.

---

## Research Questions

1. Do surveillance-neglected *Yersinia* species harbor novel conjugative plasmids
   carrying AMR genes undetectable by current marker-based surveillance approaches?

2. Which single-gene markers (16S rRNA, *rpoB*, *gyrB*, *recA*, *atpD*, *fusA*)
   best capture genus-wide phylogenetic diversity for environmental and clinical
   surveillance, and what fraction of AMR diversity remains invisible to
   standard amplicon-based approaches?

3. Is there active inter-niche AMR gene flow across One Health interfaces,
   and can phylogenetic dispersal statistics (D statistic) identify the
   genes under active horizontal transfer?

---

## Dataset

### Summary statistics

| Parameter | Value |
|---|---|
| Total assemblies downloaded (NCBI, May 2026) | 10,195 unique BioSamples |
| After removal of suppressed assemblies | 10,188 |
| Post-QC: CheckM2 + GUNC | **9,957 HQ genomes** |
| Species represented | 28 |
| One Health classified (H + A + F + E) | 8,911 (87.4%) |
| Unclassifiable [U] | 1,284 (12.6%) |
| Genome size (mean) | 4.66 Mb |
| Completeness (mean) | 100.00% |
| Contamination (mean) | 0.78% |

### Species and One Health distribution

| Species | HQ | H | A | F | E | U | % classified |
|---|---|---|---|---|---|---|---|
| *Y. enterocolitica* | 5,397 | 3,597 | 608 | 705 | 66 | 500 | 91.1% |
| *Y. pestis* | 3,626 | 277 | 3,013 | 1 | 3 | 353 | 90.3% |
| *Y. pseudotuberculosis* | 366 | 28 | 70 | 6 | 0 | 257 | 28.3% |
| *Y. ruckeri* | 209 | 1 | 191 | 0 | 3 | 15 | 92.9% |
| *Y. kristensenii* | 53 | 4 | 9 | 3 | 3 | 34 | 38.2% |
| *Y. intermedia* | 48 | 5 | 10 | 7 | 7 | 19 | 60.4% |
| *Y. mollaretii* | 37 | 4 | 5 | 0 | 0 | 28 | 24.3% |
| *Y. sp.* | 26 | 8 | 10 | 0 | 5 | 7 | 61.3% |
| *Y. frederiksenii* | 22 | 8 | 2 | 2 | 4 | 9 | 64.0% |
| *Y. bercovieri* | 21 | 5 | 2 | 1 | 1 | 12 | 42.9% |
| *Y. proxima* | 19 | 2 | 2 | 6 | 0 | 10 | 50.0% |
| *Y. alsatica* | 18 | 1 | 0 | 0 | 0 | 19 | 5.0% |
| *Y. massiliensis* | 16 | 2 | 0 | 3 | 0 | 13 | 27.8% |
| *Y. rochesterensis* | 14 | 1 | 1 | 0 | 0 | 12 | 14.3% |
| *Y. aleksiciae* | 14 | 3 | 0 | 3 | 0 | 9 | 40.0% |
| *Y. rohdei* | 13 | 3 | 3 | 0 | 0 | 7 | 46.2% |
| *Y. aldovae* | 11 | 1 | 1 | 0 | 3 | 6 | 45.5% |
| *Y. similis* | 10 | 0 | 5 | 0 | 1 | 4 | 60.0% |
| *Y. vastinensis* | 10 | 0 | 0 | 0 | 0 | 10 | 0.0% |
| *Y. artesiana* | 4 | 0 | 0 | 0 | 0 | 4 | 0.0% |
| *Y. thracica* | 4 | 0 | 1 | 0 | 0 | 3 | 25.0% |
| *Y. hibernica* | 4 | 1 | 1 | 1 | 0 | 1 | 75.0% |
| *Y. canariae* | 3 | 1 | 0 | 0 | 0 | 2 | 33.3% |
| *Y. entomophaga* | 3 | 0 | 0 | 0 | 1 | 2 | 33.3% |
| *Y. wautersii* | 3 | 0 | 0 | 0 | 1 | 2 | 33.3% |
| *Y. pekkanenii* | 3 | 0 | 0 | 1 | 0 | 2 | 33.3% |
| *Y. nurmii* | 2 | 1 | 0 | 1 | 0 | 0 | 100.0% |
| *Y. fenwicki* | 1 | 1 | 0 | 0 | 0 | 0 | 100.0% |

**One Health categories:**
- **[H]** Human clinical — isolated from human host or clinical setting
- **[A]** Animal — isolated from animal host, wildlife, or vector
- **[F]** Food/food chain — isolated from food, slaughterhouse, or retail
- **[E]** Environmental — isolated from water, soil, or environmental matrix
- **[U]** Unclassifiable — insufficient or absent metadata

### Quality control summary

| Filter | Threshold | Passed | Failed |
|---|---|---|---|
| CheckM2 completeness | ≥ 95% | — | — |
| CheckM2 contamination | ≤ 5% | 9,957 | 231 |
| GUNC (progenomes_3) | CSS ≤ 0.45 | 10,157 | 31 |
| GUNC genuine failures† | CSS > 0.45 + CheckM2 fail | — | 4 |
| **Final HQ dataset** | **Both filters** | **9,957** | **235** |

†27 GUNC failures were retained as false positives (CheckM2 HQ status;
high CSS attributed to species underrepresentation in progenomes_3).
4 genuine failures excluded: 2 × CheckM2 contamination >6%, 2 × completeness ~78%.

### Assembly level distribution (HQ dataset)

| Level | N | % |
|---|---|---|
| Contig | 8,656 | 86.9% |
| Scaffold | 857 | 8.6% |
| Complete Genome | 401 | 4.0% |
| Chromosome | 43 | 0.4% |

---

## Repository Structure

```
yersinia-pangenomics/
│
├── 01_metadata/
│   ├── raw/                          # NCBI metadata downloads (2 files)
│   ├── filtered/                     # Post GCF>GCA deduplication
│   │   ├── metadata_filtered.tsv     # 10,188 unique assemblies
│   │   ├── accessions_to_download.txt
│   │   └── species_summary.tsv
│   └── onehealth/                    # One Health curated metadata (v4)
│       ├── metadata_onehealth.tsv    # Full metadata with niche assignments
│       ├── niche_summary.tsv         # Summary by species × niche
│       ├── sensitivity_high.tsv      # High confidence only (8,756)
│       ├── sensitivity_high_medium.tsv # High+medium confidence (8,911)
│       ├── unclassified_sources.tsv  # [U] assemblies for inspection
│       └── removed_suppressed.tsv    # 7 assemblies removed from NCBI
│
├── 02_genomes/
│   ├── raw/                          # .fna files by species (45 GB, gitignored)
│   └── hq/                           # Post-QC genome list
│       ├── metadata_hq.tsv           # 9,957 HQ assemblies with QC metrics
│       └── accessions_hq.txt         # HQ accession list
│
├── 03_qc/
│   ├── checkm2/
│   │   └── quality_report.tsv        # CheckM2 results (10,188 genomes)
│   ├── gunc/
│   │   └── GUNC.progenomes_3.maxCSS_level.tsv
│   └── excluded_genomes.tsv          # Excluded genomes with reasons
│
├── 04_annotation/
│   └── bakta/                        # Bakta annotations (in progress)
│                                     # 4,104/9,957 complete
│
├── 05_taxonomy/
│   └── skani/                        # skani ANI all-vs-all (in progress)
│       ├── hq_genomes.txt            # Input genome list
│       └── skani_allvsall.txt        # ANI matrix output
│
├── 06_phylogeny/                     # Phylogenomics (pending)
│   ├── snippy/                       # Core SNP alignment
│   ├── raxml/                        # RAxML-NG reference tree
│   ├── iqtree/                       # IQ-TREE2 per-species trees
│   ├── poppunk/                      # Population structure
│   └── clonalframeml/               # Recombination estimation
│
├── 07_markers/                       # Marker gene evaluation (pending)
│   ├── extraction/                   # barrnap (16S) + HMMER (proteins)
│   ├── alignments/                   # MAFFT alignments per marker
│   ├── trees/                        # IQ-TREE2 per marker
│   └── results/                      # nRF, resolution, heterogeneity
│
├── 08_pangenome/                     # Pangenomics (pending)
│   ├── ppanggolin/                   # PPanGGOLiN per species
│   ├── ribap/                        # RIBAP genus-level
│   └── panaroo/                      # Panaroo (contrast)
│
├── 09_resistome_mobilome/            # AMR and mobilome (in progress)
│   ├── amrfinder/                    # AMRFinderPlus results
│   ├── mobsuite/                     # MOBsuite plasmid reconstruction
│   ├── platon/                       # Platon plasmid characterization
│   ├── icefinder/                    # ICEfinder ICEs
│   ├── islandpath/                   # IslandPath-DIMOB genomic islands
│   ├── integron_finder/              # IntegronFinder class 1/2/3
│   └── novel_plasmids/               # Novel plasmid detection
│
├── 10_gwas/                          # Pangenome-wide association (pending)
│   ├── scoary2/                      # Scoary2
│   └── pyseer/                       # Pyseer LMM
│
├── 11_phylo_stats/                   # Phylogenetic statistics (pending)
│   ├── d_statistic/                  # D statistic (AMR dispersal)
│   └── ancestral_reconstruction/     # Pagel ML ancestral states
│
├── 12_results/
│   ├── tables/                       # Final result tables
│   └── figures/                      # Manuscript figures
│
├── panmob/                           # PanMob Python toolkit (in development)
├── scripts/                          # Analysis scripts per phase
│   ├── 01_filter_metadata.py         # GCF>GCA rule + species consolidation
│   ├── 02_onehealth_curation.py      # One Health metadata curation v4
│   ├── 03_download_genomes.sh        # Batch genome download
│   ├── 09a_run_amrfinder.sh          # AMRFinderPlus pipeline
│   └── 09b_run_mobsuite.sh           # MOBsuite pipeline
└── logs/                             # Tool execution logs (gitignored)
```

---

## Methods Summary

### Genome acquisition and selection

Genomes were downloaded from NCBI GenBank/RefSeq (May 2026) using the
`ncbi-datasets-cli`. For each unique BioSample, RefSeq assemblies (GCF) were
preferred over GenBank assemblies (GCA). Metagenome-assembled genomes (MAGs)
and atypical assemblies were excluded using `--exclude-atypical`. Seven assemblies
subsequently suppressed from NCBI were removed and documented in
`01_metadata/onehealth/removed_suppressed.tsv`.

**Genome selection rule:** For each BioSample — if GCF exists → use GCF;
if GCA only → use GCA. This ensures maximum coverage with maximum quality.

### One Health metadata curation

Isolation source, host, and environmental metadata were retrieved from NCBI
BioSample and assigned to four One Health categories using a priority-based
framework:

1. NCBI `source_type` pre-classification (human/animal/environmental/food)
2. Host field keywords (ENVO/MeSH ontologies)
3. Isolation source field keywords
4. `collected_by` institution field (medium confidence)

All analyses were performed under two sensitivity conditions: high confidence only
(8,756 assemblies) and high + medium confidence (8,911 assemblies). Discordances
between the two conditions are explicitly reported.

### Quality control

Genome completeness and contamination were assessed with **CheckM2 v1.0.2**
(completeness ≥95%, contamination ≤5%; MIMAG thresholds for isolate genomes
[Bowers et al. 2017]). Chimerism was evaluated with **GUNC v1.0.6**
(progenomes_3 database; CSS ≤0.45). For species with fewer than five available
genomes, borderline GUNC failures (CSS 0.45–0.60) were manually inspected using
`gunc decontaminate` and retained if chimeric contigs represented <5% of total
assembly length.

### Genome annotation

Standardized annotation was performed with **Bakta v1.9.4** (full database,
`--compliant --genus Yersinia`). AMR gene annotation was performed independently
using **AMRFinderPlus v4.x** in nucleotide mode to ensure consistent database
versioning across all 9,957 genomes.

### Species delimitation

Pairwise ANI was computed with **skani v0.3.1** (all-vs-all, `--min-af 0.15`,
24 threads). Species boundaries were defined at ANI ≥95% consistent with
established prokaryotic species definitions [Jain et al. 2018].

---

## Analysis Pipeline Status

| Phase | Analysis | Tool(s) | Version | Status |
|---|---|---|---|---|
| 1 | Metadata + One Health curation | ncbi-datasets-cli, Python | — | ✅ Complete |
| 2 | Genome download | ncbi-datasets-cli | — | ✅ Complete |
| 3 | Quality control | CheckM2, GUNC | 1.0.2, 1.0.6 | ✅ Complete |
| 4 | Standardized annotation | Bakta | 1.9.4 | 🔄 4,104/9,957 |
| 5 | Species delimitation (ANI) | skani | 0.3.1 | 🔄 In progress |
| 6 | Phylogenomics | RAxML-NG, PopPUNK, ClonalFrameML | — | ⏳ Pending |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | — | ⏳ Pending |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | — | ⏳ Pending |
| 9 | Resistome + mobilome | AMRFinderPlus, MOBsuite, Platon | 4.x, 3.x, 1.7 | 🔄 In progress |
| 10 | One Health GWAS | Scoary2, Pyseer | 2.x, 1.3 | ⏳ Pending |
| 11 | Phylogenetic statistics | D statistic (caper R), phytools | — | ⏳ Pending |

---

## Conda Environments

| Environment | Primary tools | Status |
|---|---|---|
| `yersinia_pan` | ncbi-datasets-cli, skani, barrnap, HMMER, MAFFT | ✅ Active |
| `checkm2` | CheckM2 v1.0.2 | ✅ Available |
| `gunc` | GUNC v1.0.6 | ✅ Available |
| `bakta` | Bakta v1.9.4 | ✅ Available |
| `amrfinder` | AMRFinderPlus v4.x | ✅ Available |
| `mobsuite` | MOBsuite v3.x | ✅ Available |
| `skani` | skani v0.3.1 | ✅ Available |

**Note:** API keys and database paths are stored as environment variables
and are not committed to this repository. See `.env.example` for required
environment variables.

---

## Genome Selection Rule

```
For each unique BioSample accession:
  GCF available (RefSeq) → use GCF
  GCA only (GenBank)     → use GCA
  MAGs / atypical        → excluded (--exclude-atypical)

Example:
  Species X has 40 GCA assemblies, 35 with GCF pairs
  → 35 GCF + 5 GCA (unpaired) = 40 unique genomes
```

---

## Key References

1. Shaw, J. & Yu, Y.W. (2023). Rapid and accurate distance-based phylogenetic
   inference using skani. *Nature Methods*, 20:1500–1505.

2. Chklovski, A. et al. (2023). CheckM2: a rapid, scalable and accurate tool
   for assessing microbial genome quality using machine learning.
   *Nature Methods*, 20:1203–1212.

3. Orakov, A. et al. (2021). GUNC: detection of chimerism and contamination
   in prokaryotic genomes. *Genome Biology*, 22:1–19.

4. Schwengers, O. et al. (2021). Bakta: rapid and standardized annotation of
   bacterial genomes via a comprehensive database.
   *Microbial Genomics*, 7:e000685.

5. Jain, C. et al. (2018). High throughput ANI analysis of 90K prokaryotic
   genomes reveals clear species boundaries.
   *Nature Communications*, 9:5114.

6. Bowers, R.M. et al. (2017). Minimum information about a single amplified
   genome (MISAG) and a metagenome-assembled genome (MIMAG).
   *Nature Biotechnology*, 35:725–731.

7. D'Costa, V.M. et al. (2011). Antibiotic resistance is ancient.
   *Nature*, 477:457–461.

8. Forsberg, K.J. et al. (2012). The shared antibiotic resistome of soil
   bacteria and human pathogens. *Science*, 337:1107–1111.

9. Smillie, C.S. et al. (2011). Ecology drives a global network of gene
   exchange connecting the human microbiome. *Science*, 331:1261–1265.

10. Sheppard, S.K. et al. (2018). Convergent evolution of virulence in
    *Campylobacter* one decade on. *Nature Communications*, 9:2209.

11. Mather, A.E. et al. (2013). Distinguishable epidemics of multidrug-resistant
    *Salmonella* Typhimurium DT104 in different hosts.
    *Nature Communications*, 4:2606.

12. Fritz, S.A. & Purvis, A. (2010). A new measure of phylogenetic signal
    strength in binary traits. *Conservation Biology*, 24:1042–1051.

13. Bohme, K. et al. (2023). Scoary2: Rapid association of phenotypic
    multi-omics data with microbial pan-genomes. *Genome Biology*, 24:84.

14. Gautreau, G. et al. (2020). PPanGGOLiN: Depicting microbial diversity
    via a partitioned pangenome graph.
    *PLoS Computational Biology*, 16:e1007732.

15. Hoelzer, G. et al. (2024). RIBAP: a comprehensive bacterial core genome
    annotation pipeline for pangenome calculation beyond the species level.
    *Genome Biology*, 25:1.

---

## Data Availability

| Data component | Repository | Identifier |
|---|---|---|
| Genome accessions | NCBI GenBank/RefSeq | See `01_metadata/filtered/accessions_to_download.txt` |
| Curated One Health metadata | Zenodo | DOI: pending |
| ANI distance matrix | Zenodo | DOI: pending |
| Phylogenetic trees | TreeBASE | Pending |
| AMR gene tables | Zenodo | DOI: pending |
| Plasmid characterization | Zenodo | DOI: pending |
| PanMob toolkit | GitHub + Zenodo | Pending |

Genome sequences are not redistributed here; all accessions are publicly
available at NCBI GenBank/RefSeq.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of
> *Yersinia* reveals a cryptic antimicrobial resistance mobilome in
> surveillance-neglected species. *Manuscript in preparation.*

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.

---

## Contact

**Francisco Cabezas-Mera**
GitHub: [@fcabezasmera](https://github.com/fcabezasmera)
Repository: [github.com/fcabezasmera/yersinia-pangenomics](https://github.com/fcabezasmera/yersinia-pangenomics)
