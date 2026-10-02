# High-Signal Observed Strings

These are retained because they are directly useful for hunting the specific exploitation path.

## 88771 exploit markers

```text
pitboss PPE unexpectedly died NSPPE;
pitboss PPE missed too many heartbeatsNSPPE;
pitboss PPE unexpectedly died NSPPE-00;
```

## Staged-loader markers

```text
INDEX:
${IFS}
ns_monuploadd_err.pl
b64decode
/var/log/httpaccess-vpn.log
```

## Post-exploit webshell/config markers

```text
.local_journal
.ctxs.receiver
SetHandler application/x-httpd-php
AliasMatch
receiver.min.
LogonUISimple.html.style.min
php_flag engine on
```

## Privilege/persistence markers

```text
sec_monitor
superuser 100
chmod 6555 /bin/sh
chmod u+s /bin/sh
/tmp/.uxdport
/tmp/.uxdlock
```

## Why these strings are retained

The strings are tied to NetScaler-specific filenames, log labels or observed persistence structures. Generic command names are intentionally not used as standalone exploit signatures.
