#!/bin/bash
# Run OWASP ZAP baseline scan against all 3 targets and save JSON output
set -e

REPORT_DIR="$(dirname "$0")/../reports/raw"
DATE=$(date +%Y-%m-%d)

echo "[*] Starting ZAP scans — $DATE"

declare -A TARGETS=(
  ["dvwa"]="http://dvwa:80"
  ["juiceshop"]="http://juiceshop:3000"
  ["webgoat"]="http://webgoat:8080/WebGoat"
)

for TARGET_NAME in "${!TARGETS[@]}"; do
  URL="${TARGETS[$TARGET_NAME]}"
  echo "[*] Scanning $TARGET_NAME ($URL)..."

  # Pre-create output files so ZAP container can write to them
  touch "$REPORT_DIR/zap_${TARGET_NAME}_${DATE}.json"
  touch "$REPORT_DIR/zap_${TARGET_NAME}_${DATE}.html"
  chmod 666 "$REPORT_DIR/zap_${TARGET_NAME}_${DATE}.json" \
             "$REPORT_DIR/zap_${TARGET_NAME}_${DATE}.html"

  podman run --rm \
    --network vulnforge-net \
    --userns=keep-id \
    -v "$(realpath "$REPORT_DIR")":/zap/wrk/:Z \
    ghcr.io/zaproxy/zaproxy:stable \
    zap-baseline.py \
      -t "$URL" \
      -J "zap_${TARGET_NAME}_${DATE}.json" \
      -r "zap_${TARGET_NAME}_${DATE}.html" \
      -I
  echo "[+] Done: $REPORT_DIR/zap_${TARGET_NAME}_${DATE}.json"
done

echo "[+] All ZAP scans complete."
