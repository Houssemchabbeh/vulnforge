#!/bin/bash
# Demo target: Drupal 9.3 — enterprise CMS, used by governments and banks
# Run manually before a demo. Not part of the automated workflow.
set -e

if ! podman container exists drupal-db 2>/dev/null; then
  podman run -d \
    --name drupal-db \
    --network vulnforge-net \
    -e MYSQL_ROOT_PASSWORD=vulnforge_root \
    -e MYSQL_DATABASE=drupal \
    -e MYSQL_USER=drupal \
    -e MYSQL_PASSWORD=drupal \
    --restart=unless-stopped \
    docker.io/library/mariadb:10.6
  echo "[*] MariaDB starting — waiting 10s for init..."
  sleep 10
fi

podman run -d \
  --name drupal \
  --network vulnforge-net \
  -p 8084:80 \
  --restart=unless-stopped \
  docker.io/library/drupal:9.3

echo ""
echo "[+] Drupal 9.3 running at http://localhost:8084"
echo "    Complete setup : http://localhost:8084/core/install.php"
echo "    DB host        : drupal-db"
echo "    DB credentials : drupal / drupal  |  DB name: drupal"
