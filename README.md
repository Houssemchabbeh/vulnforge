# VulnForge

Self-hosted DAST platform running on RHEL 10. Automates vulnerability scanning across real-world web application stacks using OWASP ZAP and Nuclei, orchestrated by n8n, with Discord alerts and auto-committed Markdown reports.

---

## Architecture

![VulnForge DAST Automation Architecture](docs/Security_Automation_Architecture_Diagram.png)

---

## Stack

| Component | Tool | Port |
|-----------|------|------|
| Host OS | RHEL 10.1 (VMware Workstation) | — |
| Orchestrator | n8n | 5678 |
| Scanner | OWASP ZAP | — |
| Scanner | Nuclei | — |
| Container runtime | Podman (rootless) | — |
| Notifications | Discord Webhook | — |
| Deployment | Ansible | — |

---

## Targets

### Automated (scanned nightly)

| Target | Port | Description |
|--------|------|-------------|
| DVWA | 8080 | Damn Vulnerable Web Application — PHP/MySQL |
| OWASP Juice Shop | 8081 | Modern vulnerable Node.js e-commerce app |
| WebGoat | 8082 | OWASP Java-based training application |

### Demo targets (run on demand)

Real-world software stacks for demonstrating scanner reliability against production-grade codebases.

| Target | Port | Description |
|--------|------|-------------|
| WordPress 5.9 | 8083 | Most widely deployed CMS (~40% of the web) |
| Drupal 9.3 | 8084 | Enterprise CMS used by governments and banks |
| Gitea 1.17 | 8085 | Self-hosted Git — represents internal DevOps tooling |

See [`targets/DEMO_TARGETS.md`](targets/DEMO_TARGETS.md) for run commands and scan examples.

---

## Prerequisites

- RHEL 10 (or compatible) with Developer subscription
- Podman installed and rootless setup enabled
- Ansible installed (`dnf install ansible`)
- Nuclei binary in `$PATH` (see [`scripts/install_nuclei.sh`](scripts/install_nuclei.sh))
- `~/.env` containing `DISCORD_WEBHOOK_URL=https://...`
- `ansible/vault.yml` encrypted with `ansible-vault` containing `discord_webhook_url`

---

## Deploy

Full stack deploys in under 5 minutes from scratch:

```bash
git clone https://github.com/YOUR_USERNAME/vulnforge.git
cd vulnforge
ansible-playbook ansible/site.yml --ask-vault-pass
```

This applies:
- CIS-aligned system hardening (SSH, sysctl, firewalld)
- Rootless Podman network and container setup
- DVWA, Juice Shop, WebGoat containers with systemd user units
- Nuclei binary installation and ZAP image pull
- n8n container with nightly scan workflow

---

## Scan Output

Findings are scored by severity and saved as Markdown reports in `reports/`.

```
| Severity | Count | Score |
|----------|-------|-------|
| Critical |   0   |   0   |
| High     |   0   |   0   |
| Medium   |   3   |  12   |
| Low      |   9   |   9   |
| Info     |   3   |   0   |
| Total    |  15   |  21   |

Risk Score: 21 🟡
```

Scoring: Critical=10pts · High=7pts · Medium=4pts · Low=1pt · Info=0pts

Sample report: [`reports/2026-06-28_dvwa.md`](reports/2026-06-28_dvwa.md)

---

## Discord Notifications

Every scan cycle sends a Discord alert with:
- Target name and risk score
- Severity breakdown (Critical / High / Medium / Low counts)
- Risk emoji (🔴 Critical · 🟠 High · 🟡 Medium · 🟢 Low)

---

## System Hardening (Lynis)

The Ansible hardening role applies the following controls:

| Category | Controls Applied |
|----------|-----------------|
| SSH | Root login disabled, password auth disabled, MaxAuthTries 3, idle timeout, X11/TCP forwarding off, login banner |
| Kernel (sysctl) | ASLR, SYN cookies, IP forwarding off, ICMP redirect rejection, reverse path filtering, martian packet logging, ptrace restriction, dmesg restrict |
| Audit | auditd installed and enabled, rules for identity changes, SSH config, login events, privileged command execution |
| PAM | Password min length 12, complexity requirements, faillock (5 attempts → 5 min lockout), password aging (90/7/14 days) |
| Services | bluetooth, avahi-daemon, cups disabled; USB storage module blacklisted |
| OS defaults | umask 027, core dumps disabled, sudo audit logging to /var/log/sudo.log |
| Network | firewalld default zone drop, SSH + app ports only |
| SELinux | Enforcing (targeted policy) |

| Stage | Lynis Hardening Index |
|-------|-----------------------|
| Pre-hardening (Day 1 baseline) | 66 / 100 |
| Post-hardening (after Ansible playbook) | 74 / 100 |

---

## Project Structure

```
vulnforge/
├── ansible/
│   ├── roles/
│   │   ├── hardening/     # SSH, sysctl, firewalld hardening
│   │   ├── podman_setup/  # rootless Podman network
│   │   ├── targets/       # DVWA, Juice Shop, WebGoat
│   │   ├── scanners/      # Nuclei binary + ZAP image
│   │   ├── n8n/           # n8n orchestrator container
│   │   └── discord/       # webhook env setup
│   └── site.yml           # master playbook
├── scanners/
│   ├── scan_nuclei.sh     # Nuclei scan runner
│   ├── scan_zap.sh        # ZAP scan runner
│   └── parser.py          # severity scoring + Markdown report generator
├── targets/
│   ├── run_dvwa.sh
│   ├── run_juiceshop.sh
│   ├── run_webgoat.sh
│   ├── run_wordpress.sh   # demo target
│   ├── run_drupal.sh      # demo target
│   ├── run_gitea.sh       # demo target
│   ├── stop_all.sh
│   └── DEMO_TARGETS.md    # interview cheat sheet
├── reports/               # auto-generated scan reports
├── n8n/
│   └── vulnforge_workflow.json
└── docs/
    └── baseline_score.txt
```

---

## License

MIT
