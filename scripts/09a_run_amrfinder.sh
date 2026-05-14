#!/bin/bash
# AMRFinderPlus on all HQ genomes
# Usage: bash scripts/09a_run_amrfinder.sh

GENOME_LIST="02_genomes/hq/accessions_hq.txt"
METADATA="02_genomes/hq/metadata_hq.tsv"
OUTDIR="09_resistome_mobilome/amrfinder"
LOGFILE="logs/09a_amrfinder.log"
THREADS=24

mkdir -p "$OUTDIR" logs

echo "========================================" | tee -a "$LOGFILE"
echo "AMRFinderPlus started: $(date)" | tee -a "$LOGFILE"
echo "Total genomes: $(wc -l < $GENOME_LIST)" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

COUNTER=0
TOTAL=$(wc -l < "$GENOME_LIST")
FAILED=""

while IFS= read -r ACC; do
    COUNTER=$((COUNTER + 1))

    # Get species for this accession
    SP=$(awk -F'\t' -v acc="$ACC" '$1==acc {print $22}' "$METADATA")
    SP_CLEAN=$(echo "$SP" | tr ' ' '_' | tr '.' '_' | tr '/' '_')

    FNA="02_genomes/raw/${SP_CLEAN}/${ACC}.fna"
    OUT="$OUTDIR/${ACC}_amr.tsv"

    # Skip if already done
    if [ -f "$OUT" ]; then
        continue
    fi

    # Check genome exists
    if [ ! -f "$FNA" ]; then
        echo "[$COUNTER/$TOTAL] MISSING: $FNA" | tee -a "$LOGFILE"
        continue
    fi

    # Run AMRFinderPlus
    amrfinder \
        --nucleotide "$FNA" \
        --output "$OUT" \
        --threads "$THREADS" \
        --print_node \
        >> "$LOGFILE" 2>&1

    if [ $? -eq 0 ]; then
        if (( COUNTER % 500 == 0 )); then
            echo "[$COUNTER/$TOTAL] Progress: $(ls $OUTDIR/*.tsv | wc -l) done" | \
                tee -a "$LOGFILE"
        fi
    else
        FAILED="$FAILED $ACC"
        echo "[$COUNTER/$TOTAL] FAILED: $ACC" | tee -a "$LOGFILE"
    fi

done < "$GENOME_LIST"

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Completed: $(date)" | tee -a "$LOGFILE"
echo "Total done: $(ls $OUTDIR/*.tsv 2>/dev/null | wc -l)" | \
    tee -a "$LOGFILE"
if [ -n "$FAILED" ]; then
    echo "Failed: $FAILED" | tee -a "$LOGFILE"
fi
echo "========================================" | tee -a "$LOGFILE"
