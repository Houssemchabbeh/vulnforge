#!/bin/bash

echo "Stopping VulnForge targets..."

for name in dvwa juiceshop webgoat wordpress wordpress-db drupal drupal-db gitea; do
  if podman container exists "$name" 2>/dev/null; then
    podman stop "$name" && podman rm "$name"
    echo "  removed: $name"
  else
    echo "  not running: $name"
  fi
done

echo "Done."
