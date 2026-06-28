#!/bin/bash
set -e

podman run -d \
  --name juiceshop \
  --network vulnforge-net \
  -p 8081:3000 \
  --restart=unless-stopped \
  docker.io/bkimminich/juice-shop:latest

echo "Juice Shop running at http://localhost:8081"
