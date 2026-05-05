#!/bin/bash
# Tool version tracking
# Run after activating yersinia_pan environment
# Output logged to logs/tool_versions.txt

LOG="logs/tool_versions.txt"
mkdir -p logs

echo "=== Tool versions ===" > $LOG
echo "Date: $(date)" >> $LOG
echo "User: $(whoami)" >> $LOG
echo "System: $(uname -a)" >> $LOG
echo "" >> $LOG

echo "--- Conda environment ---" >> $LOG
conda info | grep "active env" >> $LOG
echo "" >> $LOG

echo "--- Main tools ---" >> $LOG
datasets --version >> $LOG 2>&1
checkm2 --version >> $LOG 2>&1
bakta --version >> $LOG 2>&1
fastANI --version >> $LOG 2>&1
gtdbtk --version >> $LOG 2>&1
snippy --version >> $LOG 2>&1
raxml-ng --version >> $LOG 2>&1
iqtree2 --version >> $LOG 2>&1
poppunk --version >> $LOG 2>&1
barrnap --version >> $LOG 2>&1
hmmbuild -h 2>&1 | head -2 >> $LOG
mafft --version >> $LOG 2>&1

echo "" >> $LOG
echo "=== Done ===" >> $LOG

cat $LOG
