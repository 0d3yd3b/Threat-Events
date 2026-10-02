# Contributing

## What belongs here

Add:

- newly observed NetScaler exploit artifacts
- new hashes, IPs, domains, URLs and certificates
- reproducible detection logic
- DFIR artifacts and timelines
- source-attributed TTP updates
- false-positive lessons

## What does not belong in the public repository

Do not add:

- private victim information
- active credentials or passwords
- API keys/tokens
- stolen configuration files
- raw customer logs containing secrets
- exploit-ready weaponized payloads when a defensive indicator is sufficient

## IOC requirements

Every IOC should have:

- type
- value
- CVE
- role
- confidence
- source

Prefer `observed` over inferred labels. Preserve attribution uncertainty.
