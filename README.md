# Genus-wide One Health Pangenomics of *Yersinia*

> First genus-wide pangenomic analysis of *Yersinia* (29 species, 9,957 genomes) integrating One Health metadata, AMR mobilome characterization, marker gene evaluation, GWAS, and multi-tool mobilome architecture analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![AMR hits](https://img.shields.io/badge/AMR%20hits-20%2C966-red)]()
[![Status](https://img.shields.io/badge/Status-Active-orange)]()

---

## Overview

*Yersinia* encompasses 29 species (28 described + 1 novel circumpolar clade) spanning human clinical, animal, food chain, and environmental niches — from *Y. pestis*, causative agent of three historical pandemics, to zoonotic enteropathogens and free-living environmental species. Despite its medical and ecological importance, no systematic genus-wide pangenomic framework existed integrating all species, all niches, and all AMR gene classes.

This study presents that framework, revealing:
- A previously unknown circumpolar *Yersinia* species invisible to all current surveillance approaches
- Three fundamentally distinct AMR mobilome architectures
- A striking environmental resistome paradox with direct public health implications
- Genus-wide temporal, geographic, and host-specific AMR patterns

---

## Key Findings

### 1. Novel *Yersinia* Species — *Candidatus Yersinia* sp. nov. (circumpolar clade)

Formal species discovery through genus-wide ANI-based delimitation:

- **15 genomes** — ANI < 95% with all 29 described *Yersinia* species; intra-group ANI 97.61–99.99%
- **Circumpolar distribution**: Arctic Russia (n=10, 2006–2021) + Antarctica (n=5, 2025) — 19-year temporal span
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere
- **AMR**: *blaFONA* in 1/15 genomes (GCF_052217185.1, Franz Josef Land, 2021) — first AMR gene in the novel clade, likely acquired by HGT from co-occurring *Serratia fonticola* in Arctic environment

### 2. Complete Marker Gene Saturation — Central Finding

All five protein-coding markers place the novel clade sister to *Y. intermedia* despite genome-wide ANI < 75% (>25% divergence):

| Marker | Distance to *Y. intermedia* | Interpretation |
|---|---|---|
| rpoB | 0.0000 | Identical |
| fusA | 0.0000 | Identical |
| recA | 0.0029 | Cryptic |
| gyrB | 0.0038 | Cryptic |
| atpD | 0.0070 | Cryptic |

This represents complete saturation of phylogenetic signal across all evaluated markers. Any surveillance framework relying on single-gene approaches would systematically misclassify this species as *Y. intermedia* — rendering it invisible.

16S rRNA: 99.2% genome recovery but only 65.5% full-length (≥1,400 bp), versus 100% recovery for all five protein-coding markers.

### 3. Three AMR Mobilome Architectures

Integrated analysis (GWAS + MOBsuite + Platon + IntegronFinder + geNomad) reveals three mechanistically distinct AMR classes:

#### Class I — Active Conjugative Plasmid-Borne (Surveillance Priority 1)

**blaA / vat(F) on IncFII** in clinical *Y. enterocolitica*:

| Trait | Odds Ratio | q-value |
|---|---|---|
| Human clinical (H) | 23.2 | <1e-300 |
| Food chain (F) | 22.9 | 4.2e-148 |
| Europe | 15.0 | <1e-300 |
| North America | 16.4 | 4.6e-260 |
| **Post-2020** | **49.8** | **<1e-300** |

IncFII backbone shared with *E. coli* clinical plasmids — active conjugation confirmed.

#### Class II — Chromosomally Integrated MDR (Stable, Monitor)

**South American MDR cluster** in Brazilian pig *Y. enterocolitica* — mechanism fully characterized:

1. IncFII conjugative plasmid (41 kb, DTR circular, geNomad score 0.989) delivers class 1 integron
2. Transposon (ITR elements, 11,575 bp, confirmed by geNomad) mediates chromosomal insertion
3. CALIN elements (IntegronFinder: 14/genome in all 12 SA cluster genomes) — integrase lost, permanently integrated
4. Platon: chromosomal location confirmed (RDS 0.2–4.6)

Gene cluster: sat2 (OR=159.5), dfrA1 (OR=147.2), floR (OR=93.5), aadA1 (OR=68.1)

**European class 1 integron**: aadA12 (OR=17.5), catA1 (OR=13.7), qacEdelta1 (OR=7.5), sul1 (OR=7.1)

#### Class III — Intrinsic Chromosomal Resistance (Low Priority)

***Y. ruckeri* blaYRC** — chromosomal intrinsic beta-lactamase:
- 100% prevalence in *Y. ruckeri* (n=209), *Y. entomophaga* (n=5), *Y. nurmii* (n=2)
- Platon: chromosomal (RDS 0.2–2.4) | IntegronFinder: 0 integrons | geNomad: no conjugative backbone
- GWAS OR=29,220 (fish) = species identity marker, not acquired resistance
- **Clinical risk: MINIMAL** — no transfer potential

### 4. Genus-wide AMR Species Profiles

20,966 AMR hits, 69 unique genes across 29 species:

| Species | n | %AMR | Core genes | %Plasmid |
|---|---|---|---|---|
| *Y. enterocolitica* | 5,398 | 100% | blaA, vat(F) | 60.4% |
| *Y. pestis* | 3,626 | 0.3% | — | **99.6%** |
| *Y. pseudotuberculosis* | 366 | 2.2% | — | 76.2% |
| *Y. ruckeri* | 209 | 100% | blaYRC | 42.6% |
| *Y. mollaretii* | 37 | 62.2% | — | 13.5% |
| *Ca. Y.* sp. nov. | 15 | 6.7% | — | 13.3% |
| 8 species | — | 0% | — | variable |

Notable: *Y. pestis* 99.6% plasmid prevalence (virulence plasmids pFra/pPla/pCD1) but 0.3% AMR — absence of antibiotic selection pressure in wildlife reservoir.
Notable: *Y. mollaretii* aac(6') in 62.2% — aminoglycoside resistance in a surveillance-neglected species.

### 5. Environmental Resistome Paradox

| Niche | AMR genes detected | Plasmid prevalence |
|---|---|---|
| Environmental (E) | **69/69** | 34.1% (lowest) |
| Human clinical (H) | 8/69 | 66.3% |
| Animal (A) | 8/69 | 88.4% (highest) |

Environmental isolates harbor all 69 AMR genes with the fewest plasmids — chromosomal AMR dominates in environmental *Yersinia*, representing a cryptic resistome invisible to current surveillance.

### 6. Temporal and Geographic Patterns

**Temporal surge** (all genomes with collection dates):

| Era | %AMR |
|---|---|
| Pre-2000 | 9.0% |
| 2000–2009 | ~25% |
| 2010–2014 | 82.5% |
| **2020+** | **96.6%** |

**Geographic gradient**: UK 98.9% > USA 98.3% >> Russia 10.0% > China/Mongolia 5.6% — driven by clinical vs wildlife surveillance focus.

**Host gradient**: Fish 100% (intrinsic) > Pig 93.8% > Human 88.7% > Rodent/Marmot 1.7% — follows antibiotic use intensity.

---

## Surveillance Recommendations

| Priority | Target | Rationale |
|---|---|---|
| **1** | IncFII blaA/vat(F) — clinical *Y. enterocolitica* | 50-fold surge post-2020, active conjugation |
| **2** | European class 1 integron (aadA12/qacEdelta1/sul1) | Clinical *Y. enterocolitica*, IncF/IncI plasmids |
| **Monitor** | SA chromosomal MDR in pig food chain | Stable CALIN, not actively spreading |
| **Alert** | *Y. mollaretii* aac(6') | Understudied species, acquired AMR |
| **Low** | blaYRC (*Y. ruckeri*) | Intrinsic, no transfer risk |
| **Environmental** | *Ca. Y.* sp. nov. monitoring | All markers fail — pangenomics required |

---

## Dataset

| Parameter | Value |
|---|---|
| Total assemblies | 10,195 unique BioSamples |
| Post-QC (CheckM2 + GUNC) | **9,957 HQ genomes** |
| Species | **29** (28 described + 1 novel) |
| One Health classified | 8,911 (87.4%) |
| Mean genome size | 4.66 Mb |
| Mean completeness | 100.00% |

| Niche | n | % |
|---|---|---|
| Human clinical (H) | 3,955 | 39.7% |
| Animal (A) | 3,924 | 39.4% |
| Unclassified (U) | 1,262 | 12.7% |
| Food/food chain (F) | 725 | 7.3% |
| Environmental (E) | 91 | 0.9% |

---

## Pipeline Status

| Phase | Analysis | Tool | Status |
|---|---|---|---|
| 1 | Metadata + One Health curation | Python, NCBI API | ✅ |
| 2 | Genome download | ncbi-datasets-cli | ✅ |
| 3 | Quality control | CheckM2 v1.0.2, GUNC v1.0.6 | ✅ |
| 4 | Annotation | Bakta v1.9.4 | 🔄 ~52% faraday HPC |
| 5 | Species delimitation | skani v0.3.1 | ✅ |
| 6 | Phylogenomics | RAxML-NG, PopPUNK | ⏳ Pending Bakta |
| 7 | Marker gene evaluation | barrnap, HMMER, IQ-TREE2 | ✅ |
| 8 | Pangenomics | PPanGGOLiN, RIBAP | ⏳ Pending Bakta |
| 9a | Resistome | AMRFinderPlus v4.x | ✅ 9,957/9,957 |
| 9b | Plasmid reconstruction | MOBsuite v3.x | ✅ 9,957/9,957 |
| 9c–e | Priority mobilome | Platon + IntegronFinder + geNomad | ✅ 34 genomes |
| 10 | GWAS | Scoary2 v0.0.15 | ✅ 330 associations |
| 11 | Phylogenetic signal | D statistic (caper) | 🔄 Running |

---

## Repository Structure

```
yersinia-pangenomics/
├── 01_metadata/               # Metadata + One Health curation (v4)
├── 02_genomes/hq/             # 9,957 HQ genome accessions + metadata
├── 03_qc/                     # CheckM2 + GUNC results
├── 05_taxonomy/skani/         # ANI results + novel species files
├── 07_markers/
│   ├── trees/                 # IQ-TREE2 treefiles (5 marker genes)
│   ├── hmm_profiles/          # Pfam HMM profiles (pressed)
│   └── novel_species_CRITICAL_FINDING.txt
├── 09_resistome_mobilome/
│   ├── mobsuite/              # Global stats (9,957 genomes)
│   ├── platon/                # Priority genome analysis
│   ├── integron_finder/       # CALIN detection results
│   └── genomad/               # Plasmid/virus classification
├── 10_gwas/                   # Scoary2 results (330 associations)
├── 11_phylo_stats/            # D statistic analysis
├── 12_results/                # Integrated findings + species profiles
└── scripts/                   # Analysis scripts (01–11)
```

---

## Methods

| Step | Tool | Version | Parameters |
|---|---|---|---|
| Genome acquisition | ncbi-datasets-cli | — | GCF>GCA/BioSample, --exclude-atypical |
| One Health curation | Python (custom) | v4 | Priority-based (NCBI BioSample fields) |
| Completeness/contamination | CheckM2 | 1.0.2 | completeness ≥95%, contamination ≤5% |
| Chimerism | GUNC | 1.0.6 | progenomes_3, CSS ≤0.45 |
| Species delimitation | skani | 0.3.1 | all-vs-all ANI, threshold ≥95% |
| 16S rRNA extraction | barrnap | 0.9 | kingdom bac, E-value ≤1e-6 |
| Protein marker detection | pyrodigal + hmmsearch | — | Pfam HMMs, E-value ≤1e-10 |
| Phylogenetic reconstruction | IQ-TREE2 | 3.1.1 | ModelFinder BIC, UFBoot 1,000 |
| AMR screening | AMRFinderPlus | 4.x | nucleotide mode |
| Plasmid reconstruction | MOBsuite mob_recon | 3.x | default |
| Plasmid classification | Platon | 1.7 | accuracy mode |
| Integron detection | IntegronFinder | 2.x | --linear |
| Mobile element classification | geNomad | 1.12 | end-to-end |
| GWAS | Scoary2 | 0.0.15 | Fisher's exact, Bonferroni FWER=0.05 |
| Phylogenetic signal | caper (R) | 1.0.4 | D statistic, 1,000 permutations |

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
| `integron` | IntegronFinder, prodigal |
| `genomad` | geNomad v1.12 |
| `scoary-2` | Scoary2 v0.0.15 |

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
15. Bowers et al. (2017). MIMAG/MISAG. *Nature Biotechnology* 35:725–731.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

## License

MIT — see [LICENSE](LICENSE)

---

## Contact

**Francisco Cabezas-Mera** | [@fcabezasmera](https://github.com/fcabezasmera)
Repository: [github.com/fcabezasmera/yersinia-pangenomics](https://github.com/fcabezasmera/yersinia-pangenomics)

---

*Last updated: May 16, 2026 | Status: Active — D statistic running, Bakta ~52% on faraday HPC*

---

## Taxonomy Notes

### Species Reclassifications

11 former *Yersinia* sp. genomes reclassified based on ANI ≥ 95%:

| Reclassified to | n genomes |
|---|---|
| *Y. bercovieri* | 3 |
| *Y. entomophaga* | 2 |
| *Y. vastinensis* | 2 |
| *Y. rochesterensis* | 2 |
| *Y. enterocolitica* | 1 |
| *Y. intermedia* | 1 |
| **Total** | **11** |

Reclassification details: `05_taxonomy/skani/yersinia_sp_reclassification.tsv`

### Borderline Species Pairs

Two species pairs with ANI values approaching the species boundary (95%):

| Pair | Max ANI | Status |
|---|---|---|
| *Y. alsatica* / *Y. frederiksenii* | 99.98% | Putative species complex |
| *Y. frederiksenii* / *Y. massiliensis* | 99.94% | Putative species complex |

These pairs may represent a single species or recently diverged lineages requiring additional phenotypic characterization.

### Novel Species — Geographic Subgroups

| Subgroup | n | Locations | Years |
|---|---|---|---|
| Arctic Russia | 10 | Sakha, Krasnoyarsk, Karelia, Franz Josef Land, Novaya Zemlya | 2006–2021 |
| Antarctica | 5 | Galindez Is., Berthelot Is., Cape Tuxen, Yalour Is. | 2025 |

Inter-subgroup ANI (Arctic vs Antarctica): mean 98.87% → single species.

