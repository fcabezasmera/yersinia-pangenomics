#!/bin/bash
# MOBsuite mob_recon on all HQ genomes
# Usage: bash scripts/09b_run_mobsuite.sh

METADATA="02_genomes/hq/metadata_hq.tsv"
OUTDIR="09_resistome_mobilome/mobsuite"
LOGFILE="logs/09b_mobsuite.log"
THREADS=24

mkdir -p "$OUTDIR" logs

echo "========================================" | tee -a "$LOGFILE"
echo "MOBsuite started: $(date)" | tee -a "$LOGFILE"
echo "Total genomes: $(wc -l < 02_genomes/hq/accessions_hq.txt)" | \
    tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"

COUNTER=0
TOTAL=$(wc -l < 02_genomes/hq/accessions_hq.txt)
FAILED=""

while IFS= read -r ACC; do
    COUNTER=$((COUNTER + 1))

    SP=$(awk -F'\t' -v acc="$ACC" '$1==acc {print $22}' "$METADATA")
    SP_CLEAN=$(echo "$SP" | tr ' ' '_' | tr '.' '_' | tr '/' '_')

    FNA="02_genomes/raw/${SP_CLEAN}/${ACC}.fna"
    OUT="$OUTDIR/${ACC}"

    # Skip if already done
    if [ -d "$OUT" ] && [ -f "$OUT/contig_report.txt" ]; then
        continue
    fi

    if [ ! -f "$FNA" ]; then
        echo "[$COUNTER/$TOTAL] MISSING: $ACC" | tee -a "$LOGFILE"
        continue
    fi

    mob_recon \
        --infile "$FNA" \
        --outdir "$OUT" \
        -n "$THREADS" \
        --force \
        >> "$LOGFILE" 2>&1

    if [ $? -eq 0 ]; then
        if (( COUNTER % 500 == 0 )); then
            DONE=$(ls -d $OUTDIR/*/ 2>/dev/null | wc -l)
            echo "[$COUNTER/$TOTAL] Progress: $DONE done" | \
                tee -a "$LOGFILE"
        fi
    else
        FAILED="$FAILED $ACC"
        echo "[$COUNTER/$TOTAL] FAILED: $ACC" | tee -a "$LOGFILE"
    fi

done < 02_genomes/hq/accessions_hq.txt

echo "" | tee -a "$LOGFILE"
echo "========================================" | tee -a "$LOGFILE"
echo "Completed: $(date)" | tee -a "$LOGFILE"
echo "Total done: $(ls -d $OUTDIR/*/ 2>/dev/null | wc -l)" | \
    tee -a "$LOGFILE"
if [ -n "$FAILED" ]; then
    echo "Failed: $FAILED" | tee -a "$LOGFILE"
fi
echo "========================================" | tee -a "$LOGFILE"
