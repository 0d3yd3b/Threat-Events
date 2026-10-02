#!/usr/bin/env python3
"""Print a compact IOC inventory summary for release checks."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "iocs" / "iocs.csv").open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))

print(f"Total IOCs: {len(rows)}")
print("By CVE:", dict(Counter(r["cve"] for r in rows)))
print("By type:", dict(Counter(r["type"] for r in rows)))
print("By confidence:", dict(Counter(r["confidence"] for r in rows)))
