#!/usr/bin/env python3
"""
Filter metadata applying:
1. Remove MAGs and uncultured
2. Consolidate species/strain names to species level
3. GCF > GCA rule per BioSample (best assembly level)

Output:
  01_metadata/filtered/metadata_filtered.tsv
  01_metadata/filtered/accessions_to_download.txt
  01_metadata/filtered/species_summary.tsv
"""

import pandas as pd
import os
import re

# --- Paths ---
INPUT  = "01_metadata/raw/yersinia_metadata_raw.tsv"
OUTDIR = "01_metadata/filtered"
os.makedirs(OUTDIR, exist_ok=True)

# --- Load ---
print("Loading metadata...")
df = pd.read_csv(INPUT, sep="\t", dtype=str)
print(f"  Raw assemblies: {len(df)}")

# --- Rename columns ---
df.columns = [
    "accession", "organism_name", "biosample",
    "assembly_level", "source_database", "refseq_category",
    "geo_loc", "isolation_source", "host",
    "collection_date", "serovar", "strain",
    "host_disease", "lat_lon",
    "total_length", "contig_n50", "scaffold_n50",
    "num_contigs", "gc_percent",
    "checkm_completeness", "checkm_contamination"
]

# --- Step 1: Remove MAGs and uncultured ---
mag_filter = df["organism_name"].str.contains(
    "uncultured|metagenome|MAG|environmental",
    case=False, na=False
)
df = df[~mag_filter].copy()
print(f"  After MAG removal: {len(df)}")

# --- Step 2: Consolidate to species level ---
def consolidate_species(name):
    name = str(name).strip()

    # Known species prefixes — order matters (longer first)
    species_list = [
        "Yersinia pseudotuberculosis",
        "Yersinia enterocolitica",
        "Yersinia kristensenii",
        "Yersinia frederiksenii",
        "Yersinia massiliensis",
        "Yersinia rochesterensis",
        "Yersinia aleksiciae",
        "Yersinia vastinensis",
        "Yersinia bercovieri",
        "Yersinia mollaretii",
        "Yersinia intermedia",
        "Yersinia artesiana",
        "Yersinia entomophaga",
        "Yersinia pekkanenii",
        "Yersinia wautersii",
        "Yersinia hibernica",
        "Yersinia thracica",
        "Yersinia canariae",
        "Yersinia alsatica",
        "Yersinia proxima",
        "Yersinia fenwicki",
        "Yersinia aldovae",
        "Yersinia similis",
        "Yersinia ruckeri",
        "Yersinia rohdei",
        "Yersinia nurmii",
        "Yersinia pestis",
    ]

    for sp in species_list:
        if name.startswith(sp):
            return sp

    # All remaining "Yersinia sp." variants
    if name.startswith("Yersinia sp"):
        return "Yersinia sp."

    return name

df["species"] = df["organism_name"].apply(consolidate_species)

print(f"\n  Species after consolidation: {df['species'].nunique()}")

# --- Step 3: Assembly level priority ---
level_order = {
    "Complete Genome": 0,
    "Chromosome": 1,
    "Scaffold": 2,
    "Contig": 3
}
df["level_rank"] = df["assembly_level"].map(level_order).fillna(9)

# --- Step 4: GCF > GCA per BioSample ---
db_order = {
    "SOURCE_DATABASE_REFSEQ": 0,
    "SOURCE_DATABASE_GENBANK": 1
}
df["db_rank"] = df["source_database"].map(db_order).fillna(9)

df_sorted = df.sort_values(
    by=["biosample", "db_rank", "level_rank"],
    ascending=True
)

df_filtered = df_sorted.drop_duplicates(
    subset="biosample", keep="first"
).copy()

print(f"  After GCF>GCA deduplication: {len(df_filtered)}")

# --- Step 5: Reports ---
print("\n  Source database distribution:")
print(df_filtered["source_database"].value_counts().to_string())

species_summary = df_filtered.groupby("species").size()\
    .reset_index(name="n_assemblies")\
    .sort_values("n_assemblies", ascending=False)

print(f"\n  Final species count: {len(species_summary)}")
print(species_summary.to_string(index=False))

# --- Step 6: Assembly level distribution ---
print("\n  Assembly level distribution:")
print(df_filtered["assembly_level"].value_counts().to_string())

# --- Save ---
df_filtered.to_csv(
    f"{OUTDIR}/metadata_filtered.tsv", sep="\t", index=False
)
df_filtered["accession"].to_csv(
    f"{OUTDIR}/accessions_to_download.txt",
    index=False, header=False
)
species_summary.to_csv(
    f"{OUTDIR}/species_summary.tsv", sep="\t", index=False
)

print(f"\n✓ Filtered metadata  → {OUTDIR}/metadata_filtered.tsv")
print(f"✓ Accessions list    → {OUTDIR}/accessions_to_download.txt")
print(f"✓ Species summary    → {OUTDIR}/species_summary.tsv")
print(f"\nFinal dataset: {len(df_filtered)} unique assemblies")
