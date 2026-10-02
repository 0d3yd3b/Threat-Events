# Attack Chain

## CVE-2026-88771 — observed three-stage chain

```mermaid
sequenceDiagram
    participant A as Attacker
    participant N as NetScaler
    participant H as HTTP access log
    participant L as ns.log
    participant P as ns_monuploadd_err.pl
    participant S as Shell/PHP

    A->>N: HTTP request with Base64 in User-Agent
    N->>H: User-Agent written to /var/log/httpaccess-vpn.log
    A->>N: Malicious login/auth value
    N->>L: pitboss ... NSPPE;<payload>
    P->>L: Read poisoned log entry
    P->>P: Extract text after NSPPE
    P->>H: grep/sed recover staged payload
    P->>P: b64decode
    P->>S: sh/php executes decoded payload
    S-->>N: webshell / persistence / C2 / exfiltration
```

## Alternative execution paths seen

- direct command validation (`id`, `whoami`)
- reverse shell using Python
- reverse shell using `nc -e`
- `curl | perl`
- `curl | bash/sh`
- Python drop-and-execute
- configuration archive and upload
- web-shell deployment
- SUID/SGID shell modification

## Post-exploitation branching

```mermaid
flowchart TD
    E[Command execution] --> A[Persistence]
    E --> B[Web shell]
    E --> C[Credential / config access]
    E --> D[C2]
    E --> F[Cleanup]
    A --> A1[sec_monitor]
    A --> A2[cron]
    A --> A3[SUID /bin/sh]
    B --> B1[.local_journal]
    B --> B2[.ctxs.receiver]
    B --> B3[CSS/icon alias camouflage]
    C --> C1[/flash/nsconfig]
    D --> D1[reverse shell]
    D --> D2[Platypus]
    D --> D3[SLAPSHOT tunneling]
    F --> F1[unlink staged files]
    F --> F2[crontab/path scrubbing]
```

## CVE-2026-88772 — separate DTLS path

```text
Crafted DTLS traffic
      ↓
Memory corruption / NSPPE crash
      ↓
Control-flow / code execution or DoS
      ↓
Web shell / privilege persistence / tunneling
```
