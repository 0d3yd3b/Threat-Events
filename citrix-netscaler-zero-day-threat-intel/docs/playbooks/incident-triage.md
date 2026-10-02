# SOC / DFIR Incident Triage Playbook

## Trigger A — 88771 marker

1. Capture the complete log event and surrounding 30–60 minutes.
2. Extract the value following `NSPPE;`.
3. Search the same host/device for HTTP User-Agent anomalies and `INDEX:`.
4. Search for `ns_monuploadd_err.pl` execution/processing.
5. Inspect filesystem and configuration persistence indicators.
6. Correlate outbound connections with `iocs/iocs.csv`.

## Trigger B — 88772 DTLS anomaly

1. Preserve packet/log evidence around UDP/443.
2. Correlate SSL handshake failures with NSPPE exits/restarts.
3. Search `/vpn/scripts/linux/` for unexpected web-accessible packages/files.
4. Check `.ns_suidcmd`, `/tmp/.uxdport`, `/tmp/.uxdlock`, cron and SUID shell state.

## Escalation condition

Escalate from "exploit attempt" to "probable compromise" when exploit evidence is joined by independent post-exploitation evidence such as:

- new web shell
- privileged local account
- SUID/SGID shell
- unexpected outbound C2
- configuration archive/exfiltration
- persistent cron entry
