#!/bin/bash
set -e

echo "[*] Fetching latest Nuclei release..."
URL=$(curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest \
  | python3 -c "
import sys, json
assets = json.load(sys.stdin)['assets']
for a in assets:
    if 'linux_amd64' in a['name'] and a['name'].endswith('.zip'):
        print(a['browser_download_url'])
        break
")

echo "[*] Downloading: $URL"
curl -L -o /tmp/nuclei.zip "$URL"

echo "[*] Installing..."
cd /tmp && unzip -o nuclei.zip nuclei
sudo mv /tmp/nuclei /usr/local/bin/nuclei
sudo chmod +x /usr/local/bin/nuclei

echo "[+] Done."
nuclei -version
