# TTP Reference

## CVE-2026-88771

| Technique / behavior | Evidence |
|---|---|
| Exploit public-facing application | Pre-auth NetScaler exploitation |
| Authentication/log poisoning | `pitboss` / `PPE` / `NSPPE` log injection |
| Unix shell | command execution after vulnerable log processing |
| Ingress tool transfer | `curl` / `wget` payload retrieval |
| Scripting interpreters | `sh`, `bash`, `perl`, `python`, `php` |
| Web shell | `.local_journal`, `.ctxs.receiver` |
| Masquerading | CSS/icon/static-resource naming |
| Account creation | `sec_monitor` |
| Privilege escalation | SUID/SGID `/bin/sh` |
| Archive collected data | `tar` of `/flash/nsconfig` |
| Exfiltration over web protocol | HTTP upload of archive |
| Command and control | reverse shells, HTTP, WebSocket/mTLS, TCP proxy |
| Scheduled task persistence | cron / `nsmon.pl` |
| File deletion | `unlink` staging artifacts |
| Process/service manipulation | kill/restart/HUP |

## CVE-2026-88772

| Technique / behavior | Evidence |
|---|---|
| Exploit public-facing application | DTLS pre-auth exploitation |
| Memory corruption | malformed/crafted DTLS traffic |
| Web shell | `.deb` / `.sig` / PHP web shell variants |
| Command execution | PHP execution and shell commands |
| File upload/download | `up` / `dl` web-shell functions |
| Privilege escalation | SUID `/bin/sh`, `/var/netscaler/.ns_suidcmd` |
| Tunneling | SLAPSHOT loopback TCP proxy |
| C2 encryption | RC4 or mTLS depending on payload family |
| Persistence | cron and HTTPD configuration |
