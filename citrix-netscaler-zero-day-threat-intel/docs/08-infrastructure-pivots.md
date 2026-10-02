# Infrastructure Pivots

## Recommended pivot sequence

```text
Exploit match
  → sample / script / log artifact
  → hash
  → VT behavior
  → DNS / URL / IP
  → certificate / SAN / TLS key
  → related samples
  → new delivery hosts
  → new C2
```

## Pivot dimensions

### Hash pivot

Pivot every recovered SHA-256 into:

- VirusTotal
- malware repositories
- internal sandbox history
- EDR/XDR telemetry

### Certificate pivot

Use:

```text
38b7c597c3f33f2caa2b2de9873f15cf9cb9984b0eacb801ef4b654a96ba9bd0
```

and the reported `platypus-ingress` identity to find related infrastructure.

### Infrastructure rotation

The reporting shows rotating VPS/host infrastructure, Cloudflare WARP addresses, rebuilt agents and different delivery servers. Therefore:

- never make the IOC list the only detector;
- record first-seen / last-seen timestamps;
- store source and confidence per IOC;
- use infrastructure as a pivot layer, not as exploit logic.
