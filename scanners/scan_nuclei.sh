#!/bin/bash
# Run Nuclei against all 3 targets and save JSON output to reports/raw/
set -e

REPORT_DIR="$(dirname "$0")/../reports/raw"
DATE=$(date +%Y-%m-%d)

echo "[*] Starting Nuclei scans — $DATE"

declare -A TARGETS=(
  ["dvwa"]="http://localhost:8080"
  ["juiceshop"]="http://localhost:8081"
  ["webgoat"]="http://localhost:8082/WebGoat"
)

for TARGET_NAME in "${!TARGETS[@]}"; do
  URL="${TARGETS[$TARGET_NAME]}"
  OUTPUT="$REPORT_DIR/nuclei_${TARGET_NAME}_${DATE}.json"
  echo "[*] Scanning $TARGET_NAME ($URL)..."
  nuclei -u "$URL" \
    -o "$OUTPUT" \
    -jsonl \
    -severity low,medium,high,critical \
    -silent
  echo "[+] Done: $OUTPUT"
done

echo "[+] All Nuclei scans complete."
