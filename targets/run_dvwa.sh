#!/bin/bash
set -e

podman run -d \
  --name dvwa \
  --network vulnforge-net \
  -p 8080:80 \
  --restart=unless-stopped \
  docker.io/vulnerables/web-dvwa:latest

echo "DVWA running at http://localhost:8080"
echo "Default credentials: admin / password"
