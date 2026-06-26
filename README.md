# VulnForge 🛡️
Self-hosted DAST vulnerability scanner on RHEL 10.
Automated scanning with OWASP ZAP + Nuclei, orchestrated by n8n, alerts via Telegram.

## Stack
- **Host:** RHEL 10 (VMware Workstation)
- **Containers:** Podman (rootless)
- **Scanners:** OWASP ZAP, Nuclei
- **Orchestration:** n8n
- **Targets:** DVWA, Juice Shop, WebGoat
- **Notifications:** Telegram Bot API
- **Deployment:** Ansible
