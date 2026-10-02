# Scope

## Included

This repository focuses on observed exploitation and post-exploitation activity related to:

- **CVE-2026-88771** — NetScaler pre-auth command injection / RCE path.
- **CVE-2026-88772** — NetScaler DTLS memory-corruption path with observed web-shell/tunneling follow-on activity.

## Explicitly excluded

The supplied Citrix bulletin references additional CVEs (88773–88778), but the research material in this collection does not provide a comparable IOC/TTP body for those vulnerabilities. They are therefore **not mixed into the operational feeds**.

Likewise, broad Linux/Unix ATT&CK behaviors such as `curl`, `wget`, `python`, `perl`, `tar`, `whoami` and `id` are not treated as standalone 88771 exploit indicators.

## Time context

The supplied reporting covers pre-disclosure activity and post-disclosure scanning/exploitation around September 2026. Indicators may age quickly, and post-disclosure traffic can include security researchers and opportunistic actors.
