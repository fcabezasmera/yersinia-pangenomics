#!/usr/bin/env python3
"""
One Health metadata curation — v4.
Extended with:
- Additional animal hosts (primates, fish, marsupials, insects)
- Additional vectors (ticks, mustelids)
- Additional food items (venison, bacon, carrot)
- collected_by field for medium confidence inference
- host_disease field for additional context

Priority order:
  1. source_type (NCBI pre-classified)
  2. host field (high confidence keywords)
  3. isolation_source field (high confidence keywords)
  4. host_disease field (high confidence keywords)
  5. collected_by field (medium confidence)
  6. host/isolation_source medium confidence keywords

Outputs:
  01_metadata/onehealth/metadata_onehealth.tsv
  01_metadata/onehealth/niche_summary.tsv
  01_metadata/onehealth/unclassified_sources.tsv
  01_metadata/onehealth/sensitivity_high.tsv
  01_metadata/onehealth/sensitivity_high_medium.tsv
"""

import pandas as pd
import os

# --- Paths ---
INPUT_FILTERED = "01_metadata/filtered/metadata_filtered.tsv"
INPUT_EXTENDED = "01_metadata/raw/yersinia_metadata_extended.tsv"
OUTDIR         = "01_metadata/onehealth"
os.makedirs(OUTDIR, exist_ok=True)

# --- Load ---
print("Loading metadata...")
df = pd.read_csv(INPUT_FILTERED, sep="\t", dtype=str)
ext = pd.read_csv(INPUT_EXTENDED, sep="\t", dtype=str)
ext.columns = [
    "accession","name","long_name","level",
    "refseq_category","bioproject","tax_id",
    "organism_name","biosample_organism","ani_organism",
    "strain","isolate","biosample","sample_name",
    "host","host_disease","isolation_source","source_type",
    "geo_loc","lat_lon","collection_date",
    "collected_by","identified_by",
    "submission_date","publication_date",
    "sequencing_tech","assembly_method"
]

df_merged = df.merge(
    ext[["accession","source_type","strain","isolate",
         "sample_name","collected_by","identified_by",
         "sequencing_tech","assembly_method","bioproject"]],
    on="accession", how="left"
)
print(f"  Assemblies: {len(df_merged)}")

# Normalize source_type
df_merged["source_type"] = df_merged["source_type"]\
    .str.lower().str.strip().fillna("")

# --- Keyword dictionaries ---
NICHE_RULES = {
    "H": {
        "high": [
            # Direct human terms
            "human", "homo sapiens",
            # Clinical samples
            "blood", "urine", "stool", "feces", "faeces",
            "wound", "clinical", "hospital", "patient",
            "csf", "cerebrospinal", "sputum", "biopsy",
            "abscess", "peritoneal", "pleural", "synovial",
            "rectal swab", "rectal", "throat swab",
            "lymph node", "appendix", "mesenteric",
            # Clinical presentations
            "diarrhea", "diarrhoea", "gastroenteritis",
            "yersiniosis", "enteritis", "colitis",
            "bacteremia", "bacteraemia", "septicemia",
            "bubo",
            # Patient descriptors
            "infant", "child", "pediatric",
            "adult patient", "human clinical",
            "human feces", "human stool", "human blood",
        ],
        "medium": [
            "infection", "outbreak", "case",
            "clinical isolate", "medical", "diagnostic",
            "sepsis", "enteric infection", "intestinal",
        ]
    },
    "A": {
        "high": [
            # Domestic livestock
            "pig", "swine", "porcine", "sus scrofa",
            "cattle", "bovine", "cow", "bos taurus",
            "calf", "veal",
            "sheep", "ovine", "ovis", "lamb",
            "goat", "caprine", "capra",
            "poultry", "chicken", "gallus",
            "turkey", "duck", "anas", "goose",
            "cat", "felis", "dog", "canis",
            "horse", "equus", "donkey", "mule",
            # Rodents (Y. pestis reservoirs)
            "rodent", "mouse", "mus musculus",
            "rat", "rattus",
            "vole", "microtus", "clethrionomys",
            "eothenomys", "apodemus",
            "hamster", "cricetus", "cricetulus",
            "gerbil", "meriones", "rhombomys", "rhombomis",
            "ground squirrel", "spermophilus", "citellus",
            "marmot", "marmota",
            "prairie dog", "cynomys",
            "jerboa", "dipus", "allactaga", "alactaga",
            "pika", "ochotona",
            "multimammate", "mastomys",
            "chinchilla", "chacoan mara",
            "alticola",
            # Lagomorphs
            "rabbit", "hare", "lepus",
            # Wild mammals
            "deer", "cervid", "roe deer", "elk", "moose",
            "capreolus",
            "fox", "vulpes", "badger", "meles",
            "wild boar", "sus scrofa ferus",
            "raccoon", "procyon",
            "weasel", "polecat", "mustela", "ferret",
            "mink", "martes", "otter", "lutra",
            "wolf", "bear", "ursus",
            "mole", "shrew", "suncus", "insectivore",
            "opossum", "marsupial", "didelphis",
            "pudu", "guanaco", "vicuna",
            # Primates (non-human)
            "non-human primate", "primate",
            "spider monkey", "ape", "macaque",
            "chimpanzee", "gorilla", "baboon",
            "lemur", "marmoset",
            # Birds
            "bird", "avian", "raptor", "passerine",
            "pigeon", "columba", "sparrow",
            # Fish
            "fish", "salmon", "salmo", "trout",
            "oncorhynchus", "rainbow trout",
            "atlantic salmon", "coregon",
            "coregonus", "tilapia", "carp",
            "perch", "cod", "gadus",
            # Reptiles/amphibians
            "reptile", "snake", "lizard", "frog",
            # Invertebrate vectors
            "flea", "xenopsylla", "pulex",
            "callopsylla", "oropsylla", "nosopsyllus",
            "rhadinopsylla", "citellophilus",
            "ctenophthalmus", "frontopsylla",
            "neopsylla", "leptopsylla",
            "tick", "ixodes", "dermacentor",
            "haemaphysalis", "rhipicephalus",
            "louse", "lice", "linognathoides",
            "mite", "acari",
            "insect", "belgica", "diptera",
            # Camelids
            "camel", "camelus", "llama", "alpaca",
            # General animal terms
            "veterinary", "wildlife", "zoo",
            "livestock", "farm animal", "domestic animal",
            "wild animal", "feral", "game animal",
        ],
        "medium": [
            "zoonotic", "zoonosis", "animal host",
            "vet clinic", "animal reservoir",
            "non-human", "zoological",
        ]
    },
    "F": {
        "high": [
            # Meat products
            "meat", "pork", "beef", "veal meat",
            "lamb meat", "mutton", "venison",
            "chicken meat", "poultry meat", "turkey meat",
            "minced", "ground meat", "mince",
            "sausage", "ham", "deli", "cold cut",
            "bacon", "salami", "chorizo",
            # Seafood
            "seafood", "fish product", "shrimp",
            "oyster", "mussel", "clam", "crab",
            # Dairy
            "dairy", "milk", "cheese", "yogurt",
            "butter", "cream", "ice cream",
            # Vegetables/produce
            "vegetable", "lettuce", "spinach", "sprout",
            "salad", "produce", "fruit", "carrot",
            "cabbage", "onion", "celery", "cucumber",
            # Ready-to-eat
            "ready-to-eat", "rte", "raw food",
            # Processing/retail
            "food", "slaughterhouse", "abattoir",
            "butcher", "retail food", "market food",
            "cutting board", "food contact",
            "food processing", "food plant",
            "grocery", "supermarket",
        ],
        "medium": [
            "food chain", "food safety", "food facility",
            "restaurant", "catering", "kitchen",
        ]
    },
    "E": {
        "high": [
            # Water bodies
            "water", "river", "lake", "stream", "pond",
            "sea", "ocean", "marine", "estuary", "bay",
            "drinking water", "tap water", "well water",
            "groundwater", "surface water", "spring",
            "irrigation", "aquatic", "reservoir",
            "creek", "brook", "fjord", "lagoon",
            # Soil/sediment
            "soil", "sediment", "mud", "earth",
            "compost", "manure", "sludge",
            # Wastewater
            "wastewater", "sewage", "effluent",
            "runoff", "drainage", "leachate",
            # Vegetation
            "plant", "rhizosphere", "root", "leaf",
            "grass", "forest", "park", "vegetation",
            # General environmental
            "environmental", "environment",
            "air", "dust", "biofilm",
            "beach", "coastal", "wetland",
            "cave", "glacier", "permafrost",
            "freshwater", "saltwater", "brackish",
            "antarctic", "antarctica",
        ],
        "medium": [
            "nature", "outdoor", "field sample",
            "ecological", "ecosystem",
        ]
    }
}

# collected_by → medium confidence
COLLECTED_BY_RULES = {
    "H": [
        "cdc", "department of health", "public health",
        "hospital", "clinical laboratory", "health department",
        "institute of public health", "national health",
        "food and drug", "fda", "rivm", "hpa", "phe",
        "health protection", "ministry of health",
        "disease control", "sanitary",
    ],
    "A": [
        "veterinary", "zoo", "wildlife", "animal health",
        "onderstepoort", "arc-onderstepoort",
        "anti-plague", "plague institute",
        "institute of epidemiology",
        "nature conservancy", "fish and wildlife",
    ],
    "F": [
        "food safety", "food inspection",
        "agri-food", "agriculture",
        "ministry of food", "food and drug",
        "food authority",
    ],
    "E": [
        "environmental agency", "environmental protection",
        "water authority", "geological survey",
    ]
}

def assign_niche(row):
    """
    Priority-based niche assignment.
    Returns (niche, confidence, matched_term)
    """
    source_type = str(row.get("source_type", "") or "").lower().strip()

    # --- P1: NCBI source_type ---
    if source_type == "human":
        return "H", "high", "source_type:human"
    elif source_type == "animal":
        return "A", "high", "source_type:animal"
    elif source_type == "environmental":
        return "E", "high", "source_type:environmental"
    elif source_type == "food":
        return "F", "high", "source_type:food"

    # --- Prepare text fields ---
    iso  = str(row.get("isolation_source", "") or "").lower().strip()
    host = str(row.get("host", "") or "").lower().strip()
    dis  = str(row.get("host_disease", "") or "").lower().strip()
    cby  = str(row.get("collected_by", "") or "").lower().strip()

    EMPTY_VALUES = {
        "nan", "missing", "unknown", "not collected",
        "not applicable", "na", "none", "", "not available",
        "not provided", "not known", "n/a", "other",
        "not available: not collected"
    }

    iso_empty  = iso in EMPTY_VALUES
    host_empty = host in EMPTY_VALUES
    dis_empty  = dis in EMPTY_VALUES

    # All empty → U
    if iso_empty and host_empty and dis_empty:
        # Try collected_by as last resort (medium confidence)
        if cby and cby not in EMPTY_VALUES:
            for niche, keywords in COLLECTED_BY_RULES.items():
                for kw in keywords:
                    if kw in cby:
                        return niche, "medium", f"collected_by:{kw}"
        return "U", "low", "no_information"

    # Combined text for keyword matching
    text = f"{iso} | {host} | {dis}"

    # --- P2: High confidence keywords ---
    for niche in ["H", "A", "F", "E"]:
        for kw in NICHE_RULES[niche]["high"]:
            if kw in text:
                return niche, "high", kw

    # --- P3: Medium confidence keywords ---
    for niche in ["H", "A", "F", "E"]:
        for kw in NICHE_RULES[niche]["medium"]:
            if kw in text:
                return niche, "medium", kw

    # --- P4: collected_by medium confidence ---
    if cby and cby not in EMPTY_VALUES:
        for niche, keywords in COLLECTED_BY_RULES.items():
            for kw in keywords:
                if kw in cby:
                    return niche, "medium", f"collected_by:{kw}"

    return "U", "low", text[:100]

# --- Apply ---
print("Assigning One Health niches...")
results = df_merged.apply(assign_niche, axis=1)
df_merged["niche"]        = results.apply(lambda x: x[0])
df_merged["confidence"]   = results.apply(lambda x: x[1])
df_merged["matched_term"] = results.apply(lambda x: x[2])

# --- Summary ---
print("\n=== Niche distribution ===")
print(df_merged["niche"].value_counts().to_string())

print("\n=== Confidence distribution ===")
print(df_merged["confidence"].value_counts().to_string())

print("\n=== Niche × Confidence ===")
print(pd.crosstab(df_merged["niche"], df_merged["confidence"]).to_string())

print("\n=== Niche by species ===")
niche_by_species = pd.crosstab(df_merged["species"], df_merged["niche"])
niche_by_species["total"] = niche_by_species.sum(axis=1)
niche_by_species["pct_classified"] = (
    (niche_by_species["total"] -
     niche_by_species.get("U",
     pd.Series(0, index=niche_by_species.index))) /
    niche_by_species["total"] * 100
).round(1)
print(niche_by_species.sort_values("total", ascending=False).to_string())

# --- Sizes ---
df_high        = df_merged[df_merged["confidence"] == "high"]
df_high_medium = df_merged[df_merged["confidence"].isin(["high","medium"])]
df_unclass     = df_merged[df_merged["niche"] == "U"]

print(f"\n=== Sensitivity analysis datasets ===")
print(f"  Total:                    {len(df_merged)}")
print(f"  Classified (H+A+F+E):    {len(df_merged[df_merged['niche']!='U'])}")
print(f"  High confidence only:    {len(df_high)}")
print(f"  High + medium:           {len(df_high_medium)}")
print(f"  Unclassifiable [U]:      {len(df_unclass)}")

print("\n=== Medium confidence breakdown ===")
medium = df_merged[df_merged["confidence"]=="medium"]
print(medium["matched_term"].value_counts().head(20).to_string())

# --- Save ---
df_merged.to_csv(
    f"{OUTDIR}/metadata_onehealth.tsv", sep="\t", index=False)

df_unclass[["accession","species","isolation_source",
            "host","host_disease","source_type",
            "collected_by","matched_term"]]\
    .to_csv(f"{OUTDIR}/unclassified_sources.tsv",
            sep="\t", index=False)

niche_summary = pd.crosstab(
    df_merged["species"], df_merged["niche"]).reset_index()
niche_summary["total"] = niche_summary[
    [c for c in niche_summary.columns if c != "species"]].sum(axis=1)
niche_summary.sort_values("total", ascending=False)\
    .to_csv(f"{OUTDIR}/niche_summary.tsv", sep="\t", index=False)

df_high.to_csv(
    f"{OUTDIR}/sensitivity_high.tsv", sep="\t", index=False)
df_high_medium.to_csv(
    f"{OUTDIR}/sensitivity_high_medium.tsv", sep="\t", index=False)
df_high["accession"].to_csv(
    f"{OUTDIR}/accessions_high_confidence.txt",
    index=False, header=False)
df_high_medium["accession"].to_csv(
    f"{OUTDIR}/accessions_high_medium_confidence.txt",
    index=False, header=False)

print(f"\n✓ All outputs saved to {OUTDIR}/")
print("Done.")
