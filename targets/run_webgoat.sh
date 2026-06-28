#!/bin/bash
set -e

podman run -d \
  --name webgoat \
  --network vulnforge-net \
  -p 8082:8080 \
  --restart=unless-stopped \
  docker.io/webgoat/webgoat:latest

echo "WebGoat running at http://localhost:8082/WebGoat"
