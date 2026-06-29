#!/usr/bin/env python3
"""
VulnForge report parser — merges ZAP and Nuclei JSON output into a scored Markdown report.

Usage:
    python3 scanners/parser.py --target dvwa --date 2026-06-28
    python3 scanners/parser.py --target dvwa  # defaults to today
    python3 scanners/parser.py --zap path/to/zap.json --nuclei path/to/nuclei.json --target dvwa
"""

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

SCORE_MAP = {"critical": 10, "high": 7, "medium": 4, "low": 1, "info": 0, "informational": 0}

EMOJI_MAP = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "🟢"}

SEVERITY_ORDER = ["critical", "high", "medium", "low", "info"]


def normalise_severity(raw: str) -> str:
    s = raw.lower().strip()
    if s == "informational":
        return "info"
    return s if s in SCORE_MAP else "info"


# ── ZAP parser ────────────────────────────────────────────────────────────────

def parse_zap(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)

    site = data.get("site", [])
    if isinstance(site, list):
        site = site[0] if site else {}

    findings = []
    for alert in site.get("alerts", []):
        riskdesc = alert.get("riskdesc", "info")
        severity = normalise_severity(riskdesc.split(" (")[0])

        desc = _strip_html(alert.get("desc", ""))
        solution = _strip_html(alert.get("solution", ""))
        cwe = f"CWE-{alert.get('cweid', '')}" if alert.get("cweid") else ""

        instances = alert.get("instances", [])
        if not isinstance(instances, list):
            instances = [instances]

        # one finding per instance URL so dedup works correctly
        for inst in instances:
            url = inst.get("uri", "") if isinstance(inst, dict) else ""
            evidence = inst.get("evidence", "") if isinstance(inst, dict) else ""
            findings.append({
                "name": alert.get("name", "Unknown"),
                "severity": severity,
                "url": url,
                "description": desc,
                "solution": solution,
                "source": "ZAP",
                "cwe": cwe,
                "evidence": evidence,
            })

        # alert with no instances still gets one row
        if not instances:
            findings.append({
                "name": alert.get("name", "Unknown"),
                "severity": severity,
                "url": site.get("@name", ""),
                "description": desc,
                "solution": solution,
                "source": "ZAP",
                "cwe": cwe,
                "evidence": "",
            })

    return findings


# ── Nuclei parser ─────────────────────────────────────────────────────────────

def parse_nuclei(path: str) -> list[dict]:
    findings = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            info = item.get("info", {})
            severity = normalise_severity(info.get("severity", "info"))
            classification = info.get("classification", {})
            cwe_list = classification.get("cwe-id") or []
            cwe = cwe_list[0] if cwe_list else ""

            findings.append({
                "name": info.get("name", item.get("template-id", "Unknown")),
                "severity": severity,
                "url": item.get("matched-at", item.get("url", "")),
                "description": info.get("description", ""),
                "solution": "",
                "source": "Nuclei",
                "cwe": cwe,
                "evidence": item.get("matched-at", ""),
            })

    return findings


# ── Merge + dedup ─────────────────────────────────────────────────────────────

def merge(zap_findings: list[dict], nuclei_findings: list[dict]) -> list[dict]:
    seen: set[tuple] = set()
    merged = []

    for f in zap_findings + nuclei_findings:
        key = (f["name"].lower(), f["url"].lower())
        if key in seen:
            continue
        seen.add(key)
        merged.append(f)

    # sort by severity weight descending
    merged.sort(key=lambda x: -SCORE_MAP.get(x["severity"], 0))
    return merged


# ── Scoring ───────────────────────────────────────────────────────────────────

def score(findings: list[dict]) -> dict:
    counts = {s: 0 for s in SEVERITY_ORDER}
    total = 0
    for f in findings:
        sev = f["severity"]
        counts[sev] = counts.get(sev, 0) + 1
        total += SCORE_MAP.get(sev, 0)
    return {"counts": counts, "total": total}


def risk_emoji(counts: dict) -> str:
    for sev in ["critical", "high", "medium", "low"]:
        if counts.get(sev, 0) > 0:
            return EMOJI_MAP[sev]
    return "🟢"


# ── Markdown report ───────────────────────────────────────────────────────────

def render_markdown(target: str, scan_date: str, findings: list[dict], scores: dict) -> str:
    counts = scores["counts"]
    total_score = scores["total"]
    total_findings = sum(counts.values())
    emoji = risk_emoji(counts)

    lines = [
        f"# VulnForge Scan Report — {target.upper()} ({scan_date})\n",
        "## Summary\n",
        "| Severity | Count | Score |",
        "|----------|-------|-------|",
    ]
    for sev in SEVERITY_ORDER:
        c = counts.get(sev, 0)
        s = SCORE_MAP[sev] * c
        lines.append(f"| {sev.capitalize()} | {c} | {s} |")
    lines += [
        f"| **Total** | **{total_findings}** | **{total_score}** |",
        "",
        f"**Risk Score: {total_score}** {emoji}",
        "",
        "---",
        "",
        "## Findings",
        "",
    ]

    for f in findings:
        sev_label = f["severity"].capitalize()
        lines.append(f"### [{sev_label}] {f['name']}")
        lines.append(f"**Source:** {f['source']}  ")
        if f["url"]:
            lines.append(f"**URL:** {f['url']}  ")
        if f["cwe"]:
            lines.append(f"**CWE:** {f['cwe']}  ")
        if f["description"]:
            lines.append(f"\n{f['description']}\n")
        if f["solution"]:
            lines.append(f"**Solution:** {f['solution']}\n")
        if f["evidence"]:
            lines.append(f"**Evidence:** `{f['evidence']}`\n")
        lines.append("---\n")

    return "\n".join(lines)


# ── Discord summary line ──────────────────────────────────────────────────────

def discord_message(target: str, scan_date: str, scores: dict) -> str:
    counts = scores["counts"]
    total = scores["total"]
    emoji = risk_emoji(counts)
    parts = [f"{sev.capitalize()}: {counts[sev]}" for sev in SEVERITY_ORDER if counts[sev] > 0]
    detail = " | ".join(parts) if parts else "No findings"
    return f"{emoji} **{target.upper()}** ({scan_date}) — Score: {total} | {detail}"


# ── HTML strip ────────────────────────────────────────────────────────────────

def _strip_html(text: str) -> str:
    import re
    return re.sub(r"<[^>]+>", "", text).strip()


# ── CLI ───────────────────────────────────────────────────────────────────────

def resolve_paths(args) -> tuple[str | None, str | None]:
    if args.zap and args.nuclei:
        return args.zap, args.nuclei

    raw_dir = Path(__file__).parent.parent / "reports" / "raw"
    d = args.date
    t = args.target

    zap_path = raw_dir / f"zap_{t}_{d}.json"
    nuclei_path = raw_dir / f"nuclei_{t}_{d}.json"

    return (str(zap_path) if zap_path.exists() else None,
            str(nuclei_path) if nuclei_path.exists() else None)


def main():
    parser = argparse.ArgumentParser(description="VulnForge report parser")
    parser.add_argument("--target", required=True, help="Target name (dvwa, juiceshop, webgoat)")
    parser.add_argument("--date", default=str(date.today()), help="Scan date YYYY-MM-DD")
    parser.add_argument("--zap", help="Path to ZAP JSON report")
    parser.add_argument("--nuclei", help="Path to Nuclei JSONL report")
    parser.add_argument("--out", default="reports", help="Output directory for Markdown report")
    args = parser.parse_args()

    zap_path, nuclei_path = resolve_paths(args)

    zap_findings = parse_zap(zap_path) if zap_path else []
    nuclei_findings = parse_nuclei(nuclei_path) if nuclei_path else []

    if not zap_findings and not nuclei_findings:
        print(f"ERROR: no report files found for target={args.target} date={args.date}", file=sys.stderr)
        sys.exit(1)

    if not zap_path:
        print(f"WARN: no ZAP report found for {args.target} {args.date}", file=sys.stderr)
    if not nuclei_path:
        print(f"WARN: no Nuclei report found for {args.target} {args.date}", file=sys.stderr)

    findings = merge(zap_findings, nuclei_findings)
    scores = score(findings)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{args.date}_{args.target}.md"

    md = render_markdown(args.target, args.date, findings, scores)
    out_file.write_text(md)

    msg = discord_message(args.target, args.date, scores)

    print(f"Report written: {out_file}")
    print(f"Discord: {msg}")
    print(f"Score: {scores['total']} | Findings: {sum(scores['counts'].values())}")


if __name__ == "__main__":
    main()
