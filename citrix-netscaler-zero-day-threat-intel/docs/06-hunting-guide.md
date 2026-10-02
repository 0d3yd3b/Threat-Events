# Hunting Guide

## Hunt priority

### Priority 1 — exploit-specific 88771 log poisoning

Search for combinations containing:

```text
pitboss
PPE
NSPPE
unexpectedly died
missed too many heartbeats
```

Then parse the command text after `NSPPE;` when present.

### Priority 2 — staged payload extraction

Search for:

```text
INDEX:
/var/log/http
b64decode
${IFS}
```

The high-value pattern is their relationship, not the isolated words.

### Priority 3 — post-exploit persistence

Look for:

```text
chmod 6555 /bin/sh
chmod u+s /bin/sh
add system user sec_monitor
bind system user sec_monitor superuser 100
```

and changes to:

```text
/flash/nsconfig/ns.conf
/etc/httpd.conf
```

### Priority 4 — web shell

Look for newly created or modified:

```text
/var/netscaler/logon/LogonPoint/.local_journal
/var/netscaler/logon/LogonPoint/custom/.ctxs.receiver
```

and HTTPD mappings for:

```text
LogonUISimple.html.style.min.css
receiver.min.css
receiver.min.<hex>.css
```

### Priority 5 — C2/delivery

Check outbound connections from the appliance to the current IOC feed, then pivot from matching samples to newly observed infrastructure.

## Important false-positive rule

Do not alert merely because a log contains `curl`, `wget`, `python`, `perl`, `tar`, `id`, or `whoami`. Those commands are common. Alerting logic should require an exploit-context discriminator or a strong post-exploitation conjunction.

## NetScaler-specific evidence sources

- `/var/log/ns.log`
- `/var/log/httpaccess-vpn.log`
- HTTPD configuration
- NetScaler configuration under `/flash/nsconfig`
- technical support bundle
- remote syslog / NetScaler Console
- packet engine core dump
- filesystem timestamps and integrity changes
- outbound flow logs

## Timeline reconstruction

Because the exploit chain can involve delayed log processing, correlate events over a wide enough window:

```text
T0: HTTP access-log poisoning
T1: authentication-log poisoning
T2: vulnerable script processing
T3: first command execution
T4: payload delivery
T5: persistence/webshell/C2
```

Do not require T0/T1/T2 to be in the same minute to identify the broader incident pattern.
