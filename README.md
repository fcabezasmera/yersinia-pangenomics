# Genus-wide One Health Pangenomics of *Yersinia*

> **Genus-wide pangenomic analysis of *Yersinia* (29 species, 9,957 genomes) integrating One Health metadata, antimicrobial resistance mobilome characterization, marker gene evaluation, GWAS, and multi-tool mobilome architecture analysis.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Genomes](https://img.shields.io/badge/Genomes-9%2C957%20HQ-blue)]()
[![Species](https://img.shields.io/badge/Species-29%20%28incl.%201%20novel%29-green)]()
[![AMR hits](https://img.shields.io/badge/AMR%20hits-20%2C966-red)]()
[![Status](https://img.shields.io/badge/Status-Phase%2011%20In%20Progress-orange)]()

---

## Major Findings

### 1. Novel *Yersinia* Species — *Candidatus Yersinia* sp. nov. (circumpolar clade)

- **15 genomes**, ANI < 95% with all 29 described *Yersinia* species
- **Circumpolar distribution**: Arctic Russia (10 genomes, 2006–2021) + Antarctica (5 genomes, 2025)
- **Ecological niche**: Environmental [E] — permafrost, sea ice, cryosphere
- **AMR**: blaFONA detected in 1/15 genomes (GCF_052217185.1, Franz Josef Land, 2021) — likely HGT from co-occurring *Serratia fonticola* in Arctic environment
- **Formal status**: Meets ANI criterion; IJSEM phenotypic characterization required

### 2. Complete Marker Gene Saturation

All five protein-coding markers place the novel species sister to *Y. intermedia* (rpoB and fusA identical, d=0.000), despite genome-wide ANI < 75% — species-level separation undetectable by any single-gene surveillance approach.

| Marker | Distance to *Y. intermedia* | Status |
|---|---|---|
| rpoB | 0.0000 | **IDENTICAL** |
| fusA | 0.0000 | **IDENTICAL** |
| recA | 0.0029 | Cryptic |
| gyrB | 0.0038 | Cryptic |
| atpD | 0.0070 | Cryptic |

### 3. Three AMR Mobilome Architectures (Integrated Multi-Tool Analysis)

Integrating GWAS + MOBsuite + Platon + IntegronFinder + geNomad reveals three fundamentally distinct AMR architectures:

#### Class I — Active Conjugative Plasmid-Borne (Surveillance Priority 1)
**blaA / vat(F) on IncFII** — actively spreading in clinical *Y. enterocolitica*:
- OR = 23.2 (niche_H), 22.9 (niche_F), 49.8 (era_2020+)
- 96.6% of post-2020 genomes carry these genes
- UK (98.9%) and USA (98.3%) = highest geographic prevalence
- IncFII backbone: conjugative, shared with *E. coli* clinical plasmids

#### Class II — Chromosomally Integrated MDR (Stable, Monitor)
**South American MDR cluster** — Brazilian pig *Y. enterocolitica*:
- sat2 (OR=159.5), dfrA1 (OR=147.2), floR (OR=93.5), aadA1 (OR=68.1)
- **Mechanism confirmed** (IntegronFinder + geNomad + Platon):
  1. IncFII conjugative plasmid (41 kb DTR, score=0.989) delivers class 1 integron
  2. Transposon (ITR elements, 11,575 bp, 4 genomes) mediates chromosomal insertion
  3. CALIN elements (14/genome, 12/12 SA cluster) = permanently integrated integron (integrase lost)
  4. Stable heritable MDR — cannot be cured by plasmid loss

**European class 1 integron cluster**: aadA12 (OR=17.5), catA1 (OR=13.7), qacEdelta1 (OR=7.5), sul1 (OR=7.1)

#### Class III — Intrinsic Chromosomal Resistance (Low Priority)
**blaYRC in *Y. ruckeri*** — chromosomal intrinsic beta-lactamase:
- 100% prevalence in *Y. ruckeri* (209 genomes) + *Y. entomophaga* + *Y. nurmii*
- Platon: chromosomal (RDS 0.2–2.4)
- IntegronFinder: 0 integrons
- geNomad: no high-confidence plasmid backbone
- Col(Ye4449) non-conjugative plasmids = no transfer potential
- GWAS OR=29,220 reflects species identity, not AMR acquisition
- **Clinical risk: MINIMAL**

### 4. Genus-wide AMR Species Profiles

20,966 AMR gene hits across 9,957 genomes (69 unique genes):

| Species | n | %AMR | Mean burden | Core genes | %plasmid |
|---|---|---|---|---|---|
| *Y. enterocolitica* | 5,398 | 100% | 2.18 | blaA, vat(F) | 60.4% |
| *Y. pestis* | 3,626 | 0.3% | 0.01 | — | **99.6%** |
| *Y. pseudotuberculosis* | 366 | 2.2% | 0.04 | — | 76.2% |
| *Y. ruckeri* | 209 | 100% | 1.11 | blaYRC | 42.6% |
| *Y. mollaretii* | 37 | 62.2% | 1.22 | — | 13.5% |
| *Y. proxima* | 19 | 100% | 1.05 | blaA | 15.8% |
| *Ca. Y.* sp. nov. | 15 | 6.7% | 0.07 | — | 13.3% |
| 8 species | — | **0%** | 0 | — | variable |

**Notable**: *Y. pestis* 99.6% plasmid prevalence (virulence plasmids pFra/pPla/pCD1) but only 0.3% AMR — no antibiotic selection pressure in wildlife reservoir hosts.

**Notable**: *Y. mollaretii* carries aac(6') in 62.2% of genomes — aminoglycoside resistance in a surveillance-neglected species.

### 5. Temporal and Geographic AMR Patterns

**Temporal surge** (9,957 genomes with collection dates):

| Era | %AMR | n genomes |
|---|---|---|
| Pre-2000 | 9.0% | 624 |
| 2000–2004 | 21.6% | 491 |
| 2005–2009 | 28.2% | 461 |
| 2010–2014 | 82.5% | 269 |
| 2015–2019 | 76.6% | 744 |
| **2020+** | **96.6%** | 3,958 |

**Geographic hotspots**: UK (98.9%) > USA (98.3%) > Australia (97.8%) >> Russia (10.0%) > China/Mongolia (5.6%). Pattern driven by clinical (high) vs wildlife (low) surveillance focus.

**Host gradient**: Fish (100%, intrinsic) > Pig (93.8%) > Human (88.7%) > Cattle (57.1%) > Rodent/Marmot (1.7%).

### 6. Environmental Resistome Paradox

| Niche | AMR genes | Plasmid prevalence | n genomes |
|---|---|---|---|
| Environmental (E) | **69/69** | 34.1% | 91 |
| Human clinical (H) | 8/69 | 66.3% | 3,955 |
| Animal (A) | 8/69 | **88.4%** | 3,924 |

Environmental isolates carry all 69 AMR genes despite fewest plasmids — AMR diversity is chromosomal in environmental *Yersinia*, representing a cryptic resistome invisible to current surveillance.

### 7. Marker Gene Performance

| Marker | Recovery | Full-length |
|---|---|---|
| 16S rRNA | 99.2% | **65.5%** ← fragmentation problem |
| rpoB / gyrB / recA / atpD / fusA | **100.0%** each | N/A |

---

## Surveillance Recommendations

1. **Priority 1**: Monitor IncFII blaA/vat(F) in clinical *Y. enterocolitica* — actively conjugating, 50-fold post-2020 surge
2. **Priority 2**: Screen European isolates for class 1 integron (aadA12/qacEdelta1/sul1)
3. **Monitor**: SA chromosomal MDR in pig food chain — stable CALIN, not spreading
4. **Alert**: *Y. mollaretii* aac(6') — understudied species with acquired AMR
5. **Low priority**: blaYRC (*Y. ruckeri*) — intrinsic, no transfer risk
6. **Novel species**: Requires environmental surveillance — all marker approaches fail

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
| 9c | Priority plasmid analysis | Platon v1.7 | ✅ 34 genomes |
| 9d | Integron detection | IntegronFinder | ✅ 34 genomes |
| 9e | Mobile element classification | geNomad v1.12 | ✅ 34 genomes |
| 10 | GWAS | Scoary2 v0.0.15 | ✅ 330 associations |
| 11 | Phylo statistics | D statistic (caper R) | 🔄 Running |

---

## Methods Summary

**Genome acquisition**: ncbi-datasets-cli, GCF > GCA per BioSample, MAGs excluded.

**One Health curation (v4)**: Priority-based assignment (H/A/F/E), 87.4% classified.

**QC**: CheckM2 v1.0.2 (completeness ≥95%, contamination ≤5%) + GUNC v1.0.6 progenomes_3 (CSS ≤0.45).

**Species delimitation**: skani v0.3.1 all-vs-all ANI (99,141,849 pairs); threshold ANI ≥95%.

**Marker genes**: barrnap v0.9 (16S) + pyrodigal + hmmsearch Pfam HMMs + MAFFT + trimal + IQ-TREE2 v3.1.1 (ModelFinder BIC). Models: rpoB LG+I, gyrB Q.PLANT+I+G4, recA FLAVI+I, atpD Q.PLANT+I+R2, fusA LG+I+R2.

**Resistome**: AMRFinderPlus v4.x nucleotide mode (9,957 genomes).

**Mobilome**: MOBsuite v3.x mob_recon (9,957 genomes) + Platon v1.7 accuracy mode + IntegronFinder (CALIN detection) + geNomad v1.12 end-to-end (plasmid/virus classification) on 34 priority genomes.

**GWAS**: Scoary2 v0.0.15, Fisher's exact test, Bonferroni correction (FWER=0.05), 69 AMR genes × 21 traits.

**D statistic**: caper R package (Fritz & Purvis 2010), midpoint-rooted rpoB tree, 1,000 permutations (in progress).

---

## Repository Structure

```
yersinia-pangenomics/
├── 01_metadata/                    # Metadata + One Health curation
├── 02_genomes/hq/                  # HQ genome metadata (9,957)
├── 03_qc/                          # CheckM2 + GUNC results
├── 05_taxonomy/skani/              # ANI + novel species files
├── 07_markers/                     # Marker gene evaluation
│   ├── trees/                      # IQ-TREE2 treefiles (5 genes)
│   └── novel_species_CRITICAL_FINDING.txt
├── 09_resistome_mobilome/
│   ├── amrfinder/                  # 9,957 genomes ✓
│   ├── mobsuite/                   # 9,957 genomes ✓
│   │   ├── mobsuite_genome_stats.tsv
│   │   ├── mobsuite_all_plasmids.tsv
│   │   └── MOBSUITE_GLOBAL_FINDINGS.json
│   ├── platon/                     # 34 priority genomes ✓
│   ├── integron_finder/            # 34 priority genomes ✓
│   │   └── integron_results.tsv
│   ├── genomad/                    # 34 priority genomes ✓
│   │   ├── genomad_plasmid_results.tsv
│   │   └── genomad_virus_results.tsv
│   └── INTEGRON_GENOMAD_FINDINGS.json
├── 10_gwas/
│   ├── scoary2_final/              # Scoary2 output
│   ├── scoary2_significant.tsv     # 330 associations
│   └── GWAS_FINDINGS.json
├── 11_phylo_stats/                 # D statistic (in progress)
├── 12_results/                     # Integrated findings
│   ├── species_amr_mobilome_profile.tsv
│   ├── comprehensive_amr_metadata.tsv
│   └── COMPREHENSIVE_AMR_FINDINGS.json
└── scripts/
```

---

## Conda Environments

| Environment | Key Tools |
|---|---|
| `yersinia_pan` | skani, barrnap, HMMER, MAFFT, pyrodigal, IQ-TREE2, platon |
| `checkm2` | CheckM2 v1.0.2 |
| `gunc` | GUNC v1.0.6 |
| `bakta` | Bakta v1.9.4 |
| `amrfinder` | AMRFinderPlus v4.x |
| `mobsuite` | MOBsuite v3.x |
| `integron` | IntegronFinder v2.x |
| `genomad` | geNomad v1.12 |
| `scoary-2` | Scoary2 v0.0.15 |

---

## References

1. Shaw & Yu (2023). skani. *Nature Methods*, 20:1500–1505.
2. Chklovski et al. (2023). CheckM2. *Nature Methods*, 20:1203–1212.
3. Orakov et al. (2021). GUNC. *Genome Biology*, 22:1–19.
4. Schwengers et al. (2021). Bakta. *Microbial Genomics*, 7:e000685.
5. Jain et al. (2018). ANI. *Nature Communications*, 9:5114.
6. Nguyen et al. (2015). IQ-TREE. *Mol. Biol. Evol.*, 32:268–274.
7. Kalyaanamoorthy et al. (2017). ModelFinder. *Nature Methods*, 14:587–589.
8. Bohme et al. (2023). Scoary2. *Genome Biology*, 24:84.
9. Fritz & Purvis (2010). D statistic. *Conservation Biology*, 24:1042–1051.
10. Schwengers et al. (2021). Platon. *Microbial Genomics*, 7:e000656.
11. Robertson & Nash (2018). MOBsuite. *Microbial Genomics*, 4:e000206.
12. Cury et al. (2016). IntegronFinder. *Nucleic Acids Research*, 44:4539–4550.
13. Camargo et al. (2023). geNomad. *Nature Biotechnology*, 41:1783–1795.
14. Gautreau et al. (2020). PPanGGOLiN. *PLoS Comp. Biol.*, 16:e1007732.

---

## Citation

> Cabezas-Mera, F. et al. (2026). Genus-wide One Health pangenomics of *Yersinia* reveals a cryptic antimicrobial resistance mobilome in surveillance-neglected species undetectable by current marker-based approaches. *Manuscript in preparation.*

---

**Last updated:** May 16, 2026  
**Status:** Phases 1–3, 5, 7, 9a–e, 10 complete | D statistic running | Bakta ~52% on faraday HPC
