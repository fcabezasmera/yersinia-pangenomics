#!/bin/bash
# Download genomes by species in batches
# Robust to interruptions — skips already downloaded species
#
# Usage: bash scripts/03_download_genomes.sh
# Logs:  logs/03_download_genomes.log

METADATA="01_metadata/onehealth/metadata_onehealth.tsv"
OUTDIR="02_genomes/raw"
LOGFILE="logs/03_download_genomes.log"
API_KEY="${NCBI_API_KEY:-}"

mkdir -p "$OUTDIR" logs

echo "========================================" | tee -a "$LOGFILE"
echo "Download started: $(date)" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

# Get unique species list (column 2)
SPECIES=$(tail -n +2 "$METADATA" | \
          awk -F'\t' '{print $2}' | \
          sort -u)

TOTAL_SPECIES=$(echo "$SPECIES" | wc -l)
COUNTER=0
FAILED=""

for SP in $(tail -n +2 "$METADATA" | \
            awk -F'\t' '{print $2}' | \
            sort -u); do

    COUNTER=$((COUNTER + 1))
    SP_CLEAN=$(echo "$SP" | tr ' ' '_' | tr '.' '_')
    SP_DIR="$OUTDIR/$SP_CLEAN"

    # Count expected genomes for this species
    N_EXPECTED=$(awk -F'\t' -v sp="$SP" \
                 'NR>1 && $2==sp {count++} END {print count+0}' \
                 "$METADATA")

    # Skip if already downloaded and complete
    N_EXISTING=$(ls "$SP_DIR"/*.fna 2>/dev/null | wc -l)
    if [ "$N_EXISTING" -eq "$N_EXPECTED" ] && [ "$N_EXPECTED" -gt 0 ]; then
        echo "[$COUNTER/$TOTAL_SPECIES] SKIP $SP ($N_EXISTING/$N_EXPECTED genomes)" | \
            tee -a "$LOGFILE"
        continue
    fi

    mkdir -p "$SP_DIR"

    # Get accessions for this species (column 1, species in column 2)
    awk -F'\t' -v sp="$SP" 'NR>1 && $2==sp {print $1}' \
        "$METADATA" > /tmp/sp_accessions.txt

    N_ACCS=$(wc -l < /tmp/sp_accessions.txt)
    echo "[$COUNTER/$TOTAL_SPECIES] Downloading $SP ($N_ACCS genomes)..." | \
        tee -a "$LOGFILE"

    # Download
    if datasets download genome accession --api-key "$API_KEY" \
        --inputfile /tmp/sp_accessions.txt \
        --include genome \
        --mag exclude \
        --filename "$SP_DIR/download.zip" \
        >> "$LOGFILE" 2>&1; then

        # Extract
        unzip -q "$SP_DIR/download.zip" \
              -d "$SP_DIR/tmp/" 2>/dev/null || true

        # Move fna files with accession as filename
        find "$SP_DIR/tmp/" -name "*.fna" | while read fna; do
            acc=$(basename $(dirname "$fna"))
            cp "$fna" "$SP_DIR/${acc}.fna"
        done

        # Cleanup
        rm -rf "$SP_DIR/tmp/" "$SP_DIR/download.zip"

        N_DOWNLOADED=$(ls "$SP_DIR"/*.fna 2>/dev/null | wc -l)
        echo "  ✓ $N_DOWNLOADED/$N_ACCS genomes saved" | \
            tee -a "$LOGFILE"

    else
        echo "  ✗ FAILED: $SP" | tee -a "$LOGFILE"
        FAILED="$FAILED\n  $SP"
    fi
done

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Download completed: $(date)" | tee -a "$LOGFILE"
echo "Total genomes: $(find $OUTDIR -name '*.fna' | wc -l)" | \
    tee -a "$LOGFILE"

if [ -n "$FAILED" ]; then
    echo -e "FAILED species:$FAILED" | tee -a "$LOGFILE"
else
    echo "All species downloaded successfully ✓" | tee -a "$LOGFILE"
fi
echo "========================================" | tee -a "$LOGFILE"
