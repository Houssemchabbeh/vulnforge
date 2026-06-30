# VulnForge Demo Targets

Quick reference for spinning up targets before a demo or interview.

---

## Automated targets (always running via systemd)

These start automatically and are scanned nightly by n8n.

| Target | Port | URL | Credentials |
|--------|------|-----|-------------|
| DVWA | 8080 | http://localhost:8080 | admin / password |
| OWASP Juice Shop | 8081 | http://localhost:8081 | — |
| WebGoat | 8082 | http://localhost:8082/WebGoat | guest / guest |

---

## Demo targets (run on demand)

Real-world software stacks. Start whichever fits the demo context.

### WordPress 5.9 — Real-world CMS

**When to use:** "Show me a scan against something that runs in actual production."

```bash
bash targets/run_wordpress.sh
```

| | |
|-|-|
| URL | http://localhost:8083 |
| First-time setup | http://localhost:8083/wp-admin/install.php |
| DB credentials | wordpress / wordpress |

**Scan commands:**
```bash
# Nuclei — WordPress-specific templates
nuclei -u http://localhost:8083 -tags wordpress -severity low,medium,high,critical -jsonl -o reports/raw/nuclei_wordpress_$(date +%Y-%m-%d).json

# ZAP baseline
bash scanners/scan_zap.sh  # or point ZAP manually at http://localhost:8083
```

---

### Drupal 9.3 — Enterprise CMS

**When to use:** "Show me a scan against software used by governments and banks."

```bash
bash targets/run_drupal.sh
```

| | |
|-|-|
| URL | http://localhost:8084 |
| First-time setup | http://localhost:8084/core/install.php |
| DB host | drupal-db |
| DB credentials | drupal / drupal  \|  DB name: drupal |

**Scan commands:**
```bash
# Nuclei — Drupal-specific templates (includes Drupalgeddon checks)
nuclei -u http://localhost:8084 -tags drupal -severity low,medium,high,critical -jsonl -o reports/raw/nuclei_drupal_$(date +%Y-%m-%d).json
```

---

### Gitea 1.17 — Self-hosted Git

**When to use:** "Show me a scan against internal developer tooling, like what you'd find inside a company network."

```bash
bash targets/run_gitea.sh
```

| | |
|-|-|
| URL | http://localhost:8085 |
| First-time setup | http://localhost:8085 (installer runs on first visit) |
| DB | SQLite — no separate DB needed |

**Scan commands:**
```bash
# Nuclei — Gitea-specific templates
nuclei -u http://localhost:8085 -tags gitea -severity low,medium,high,critical -jsonl -o reports/raw/nuclei_gitea_$(date +%Y-%m-%d).json
```

---

## Stop everything

```bash
bash targets/stop_all.sh
```

Stops all 8 containers (automated + demo). Safe to run even if some are not running.
