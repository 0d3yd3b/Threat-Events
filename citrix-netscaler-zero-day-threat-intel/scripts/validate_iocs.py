#!/usr/bin/env python3
"""Validate the repository IOC feed without external dependencies."""
from __future__ import annotations

import csv
import ipaddress
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "iocs" / "iocs.csv"
JSON_PATH = ROOT / "iocs" / "iocs.json"

REQUIRED = {"type", "value", "cve", "role", "confidence", "source"}
SHA256_RE = re.compile(r"^[A-Fa-f0-9]{64}$")


def validate_row(row: dict[str, str], idx: int) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED - set(row)
    if missing:
        errors.append(f"row {idx}: missing columns {sorted(missing)}")
        return errors
    if not row["value"].strip():
        errors.append(f"row {idx}: empty value")
    if row["type"] == "ipv4":
        try:
            ipaddress.ip_address(row["value"])
        except ValueError:
            errors.append(f"row {idx}: invalid IPv4 {row['value']}")
    if row["type"] in {"sha256", "certificate_sha256"} and not SHA256_RE.fullmatch(row["value"]):
        errors.append(f"row {idx}: invalid SHA-256 {row['value']}")
    if row["cve"] not in {"CVE-2026-88771", "CVE-2026-88772"}:
        errors.append(f"row {idx}: invalid CVE {row['cve']}")
    return errors


def main() -> int:
    errors: list[str] = []
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for idx, row in enumerate(rows, start=2):
        errors.extend(validate_row(row, idx))

    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if payload.get("generated_from") != "iocs.csv":
        errors.append("iocs.json: unexpected generated_from value")
    if len(payload.get("iocs", [])) != len(rows):
        errors.append("iocs.json: IOC count does not match iocs.csv")

    if errors:
        print("IOC validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"IOC validation passed: {len(rows)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
