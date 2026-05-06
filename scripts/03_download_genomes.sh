#!/bin/bash
# Download genomes by species in batches of 500 accessions
# Robust to interruptions — skips already downloaded genomes
#
# Usage: bash scripts/03_download_genomes.sh
# Logs:  logs/03_download_genomes.log

METADATA="01_metadata/onehealth/metadata_onehealth.tsv"
OUTDIR="02_genomes/raw"
LOGFILE="logs/03_download_genomes.log"
API_KEY="${NCBI_API_KEY:-}"
BATCH_SIZE=500

COL_ACCESSION=1
COL_SPECIES=22

mkdir -p "$OUTDIR" logs

echo "========================================" | tee -a "$LOGFILE"
echo "Download started: $(date)" | tee -a "$LOGFILE"
echo "Batch size: $BATCH_SIZE accessions" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

# Get unique species list
tail -n +2 "$METADATA" | \
    awk -F'\t' '{print $22}' | \
    sort -u > /tmp/species_list.txt

TOTAL_SPECIES=$(wc -l < /tmp/species_list.txt)
TOTAL_GENOMES=$(tail -n +2 "$METADATA" | wc -l)
echo "Total species: $TOTAL_SPECIES" | tee -a "$LOGFILE"
echo "Total genomes: $TOTAL_GENOMES" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

COUNTER=0
FAILED=""

while IFS= read -r SP; do
    COUNTER=$((COUNTER + 1))

    SP_CLEAN=$(echo "$SP" | tr ' ' '_' | tr '.' '_' | tr '/' '_')
    SP_DIR="$OUTDIR/$SP_CLEAN"

    # Count expected genomes
    N_EXPECTED=$(awk -F'\t' -v sp="$SP" \
        'NR>1 && $22==sp {count++} END {print count+0}' \
        "$METADATA")

    # Skip if already complete
    N_EXISTING=$(ls "$SP_DIR"/*.fna 2>/dev/null | wc -l)
    if [ "$N_EXISTING" -ge "$N_EXPECTED" ] && [ "$N_EXPECTED" -gt 0 ]; then
        echo "[$COUNTER/$TOTAL_SPECIES] SKIP $SP ($N_EXISTING/$N_EXPECTED)" | \
            tee -a "$LOGFILE"
        continue
    fi

    mkdir -p "$SP_DIR"

    # Get all accessions for this species
    awk -F'\t' -v sp="$SP" \
        'NR>1 && $22==sp {print $1}' \
        "$METADATA" > /tmp/sp_accessions_all.txt

    N_ACCS=$(wc -l < /tmp/sp_accessions_all.txt)
    N_BATCHES=$(( (N_ACCS + BATCH_SIZE - 1) / BATCH_SIZE ))

    echo "[$COUNTER/$TOTAL_SPECIES] $SP ($N_ACCS genomes, $N_BATCHES batches)..." | \
        tee -a "$LOGFILE"

    BATCH_FAILED=0

    # Split into batches and download
    split -l "$BATCH_SIZE" \
          /tmp/sp_accessions_all.txt \
          /tmp/sp_batch_

    BATCH_NUM=0
    for BATCH_FILE in /tmp/sp_batch_*; do
        BATCH_NUM=$((BATCH_NUM + 1))
        BATCH_N=$(wc -l < "$BATCH_FILE")

        # Skip accessions already downloaded
        BATCH_MISSING=()
        while IFS= read -r acc; do
            if [ ! -f "$SP_DIR/${acc}.fna" ]; then
                BATCH_MISSING+=("$acc")
            fi
        done < "$BATCH_FILE"

        N_MISSING=${#BATCH_MISSING[@]}

        if [ "$N_MISSING" -eq 0 ]; then
            echo "  Batch $BATCH_NUM/$N_BATCHES: all already downloaded" | \
                tee -a "$LOGFILE"
            rm "$BATCH_FILE"
            continue
        fi

        # Write missing accessions to temp file
        printf '%s\n' "${BATCH_MISSING[@]}" > /tmp/sp_batch_missing.txt

        echo "  Batch $BATCH_NUM/$N_BATCHES: downloading $N_MISSING genomes..." | \
            tee -a "$LOGFILE"

        BATCH_ZIP="$SP_DIR/batch_${BATCH_NUM}.zip"

        if datasets download genome accession \
            --inputfile /tmp/sp_batch_missing.txt \
            --include genome \
            --mag exclude \
            --api-key "$API_KEY" \
            --filename "$BATCH_ZIP" \
            >> "$LOGFILE" 2>&1; then

            # Extract
            unzip -q "$BATCH_ZIP" \
                  -d "$SP_DIR/tmp_${BATCH_NUM}/" 2>/dev/null || true

            # Move fna
            find "$SP_DIR/tmp_${BATCH_NUM}/" -name "*.fna" | \
            while read fna; do
                acc=$(basename $(dirname "$fna"))
                cp "$fna" "$SP_DIR/${acc}.fna"
            done

            # Cleanup
            rm -rf "$SP_DIR/tmp_${BATCH_NUM}/" "$BATCH_ZIP"

            N_NOW=$(ls "$SP_DIR"/*.fna 2>/dev/null | wc -l)
            echo "  Batch $BATCH_NUM/$N_BATCHES: ✓ ($N_NOW/$N_EXPECTED total)" | \
                tee -a "$LOGFILE"

        else
            echo "  Batch $BATCH_NUM/$N_BATCHES: ✗ FAILED" | \
                tee -a "$LOGFILE"
            BATCH_FAILED=$((BATCH_FAILED + 1))
        fi

        rm -f "$BATCH_FILE"
        # Small pause between batches to avoid rate limiting
        sleep 2
    done

    N_FINAL=$(ls "$SP_DIR"/*.fna 2>/dev/null | wc -l)
    if [ "$BATCH_FAILED" -gt 0 ]; then
        echo "  ✗ $SP: $N_FINAL/$N_EXPECTED ($BATCH_FAILED batches failed)" | \
            tee -a "$LOGFILE"
        FAILED="$FAILED\n  $SP"
    else
        echo "  ✓ $SP: $N_FINAL/$N_EXPECTED complete" | \
            tee -a "$LOGFILE"
    fi

done < /tmp/species_list.txt

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Completed: $(date)" | tee -a "$LOGFILE"
echo "Total genomes: $(find $OUTDIR -name '*.fna' | wc -l)" | \
    tee -a "$LOGFILE"
echo "Disk usage: $(du -sh $OUTDIR)" | tee -a "$LOGFILE"

if [ -n "$FAILED" ]; then
    echo -e "FAILED species:$FAILED" | tee -a "$LOGFILE"
else
    echo "All species downloaded successfully ✓" | tee -a "$LOGFILE"
fi
echo "========================================" | tee -a "$LOGFILE"
