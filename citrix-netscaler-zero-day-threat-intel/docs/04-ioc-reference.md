# IOC Reference

The canonical machine-readable feed is `iocs/iocs.csv` and `iocs/iocs.json`.

## IOC classes

- `ipv4`
- `domain`
- `url`
- `sha256`
- `file_path`
- `filename`
- `certificate_sha256`
- `user_agent`
- `http_path`
- `http_cookie`
- `credential_artifact` (redacted in public feed)

## Handling guidance

Use IOCs for:

- enrichment
- blocking when policy permits
- retro-hunting
- infrastructure clustering
- sample pivoting

Do not use fast-changing IPs/domains/hashes as the primary definition of CVE-2026-88771 exploitation.
