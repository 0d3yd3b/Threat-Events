# Repository Maintenance Model

## Feed hierarchy

```text
Canonical
  └── iocs/iocs.csv
        ├── iocs/iocs.json
        ├── iocs/netscaler-88771.txt
        ├── iocs/netscaler-88772.txt
        └── iocs/stix-bundle.json

Detection
  ├── detections/yara/
  ├── detections/sigma/
  └── detections/queries/

Analysis
  └── docs/
```

## When a new IOC arrives

Record its source, confidence, CVE and role. Do not automatically replace older IOCs; keep historical indicators because they remain useful for retrospective hunts.

## When a new exploit sample arrives

Prefer to update exploit invariants and add a regression sample/reference. Do not automatically add every string from the sample to the YARA rule.

## Detection quality gate

A rule should answer one of these questions clearly:

- Is this exploit-specific?
- Is this post-exploitation-specific?
- Is this an IOC enrichment rule?

Avoid mixing all three into one broad OR-heavy rule.

## Release checklist

```text
[ ] IOC schema validates
[ ] JSON matches CSV
[ ] No secrets or customer data
[ ] Source attribution present
[ ] Confidence assigned
[ ] YARA reviewed for FP risk
[ ] Sigma logic reviewed for field compatibility
[ ] README updated
[ ] CHANGELOG updated
```
