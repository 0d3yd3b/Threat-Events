# Technical Overview

## CVE-2026-88771

The collected reporting describes a pre-authentication NetScaler command-injection path in which attacker-controlled authentication data is written into logs and later processed by `ns_monuploadd_err.pl`.

### Stable exploit markers

```text
pitboss PPE unexpectedly died NSPPE;
pitboss PPE missed too many heartbeatsNSPPE;
```

### Processing component

```text
/netscaler/ns_monuploadd_err.pl
/netscaler/ns_monuploadd_err.pl -WR
```

### Staged execution markers

```text
INDEX:
/var/log/httpaccess-vpn.log
b64decode
${IFS}
```

The most interesting high-fidelity pattern is the conjunction of the NetScaler-specific log marker + vulnerable processor + staged decoding/execution behavior.

## CVE-2026-88772

This is a distinct DTLS/memory-corruption path. The source material describes crafted DTLS input causing memory corruption, NSPPE crashes and possible code execution or denial of service, followed in some campaigns by `.deb`-based PHP web shells and tunneling.

## Important separation

Do not collapse the two vulnerabilities into one detection signature. They share post-exploitation themes but have different initial exploitation primitives.
