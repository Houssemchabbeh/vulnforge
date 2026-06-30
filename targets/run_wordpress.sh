#!/bin/bash
# Demo target: WordPress 5.9 — real-world CMS, ~40% of the internet
# Run manually before a demo. Not part of the automated workflow.
set -e

if ! podman container exists wordpress-db 2>/dev/null; then
  podman run -d \
    --name wordpress-db \
    --network vulnforge-net \
    -e MYSQL_ROOT_PASSWORD=vulnforge_root \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=wordpress \
    -e MYSQL_PASSWORD=wordpress \
    --restart=unless-stopped \
    docker.io/library/mariadb:10.6
  echo "[*] MariaDB starting — waiting 10s for init..."
  sleep 10
fi

podman run -d \
  --name wordpress \
  --network vulnforge-net \
  -p 8083:80 \
  -e WORDPRESS_DB_HOST=wordpress-db \
  -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=wordpress \
  --restart=unless-stopped \
  docker.io/library/wordpress:5.9

echo ""
echo "[+] WordPress 5.9 running at http://localhost:8083"
echo "    Complete setup : http://localhost:8083/wp-admin/install.php"
echo "    DB credentials : wordpress / wordpress"
