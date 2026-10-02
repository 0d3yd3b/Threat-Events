# SIEM / XDR Query Pack

The exact field names differ by product. These queries are deliberately written as **logic patterns**, not copy-paste vendor syntax.

## Generic log query — 88771 exploit marker

```text
message:("pitboss" AND "PPE" AND "NSPPE" AND ("unexpectedly died" OR "missed too many heartbeats"))
AND message:(";" OR "${IFS}")
```

## Generic staged-loader query

```text
message:"INDEX:" AND message:"b64decode" AND message:("/var/log/http" OR "${IFS}")
```

## Generic post-exploit query

```text
(message:("chmod 6555 /bin/sh" OR "chmod u+s /bin/sh"))
OR message:("sec_monitor" AND ("superuser 100" OR "bind system user"))
OR message:(".local_journal" OR ".ctxs.receiver")
```

## Generic NetScaler file hunt

```text
path:("/netscaler/ns_monuploadd_err.pl" OR "/flash/nsconfig/ns.conf" OR "/etc/httpd.conf" OR "/var/python/bin/customsnmpd" OR "/tmp/.uxdport" OR "/tmp/.uxdlock")
```

## Correlation guidance

For a higher-confidence incident, correlate at least two distinct classes:

```text
88771 exploit log marker
        +
post-exploitation artifact / outbound C2 / webshell
```

or:

```text
88772 DTLS anomaly
        +
new webshell / SUID / SLAPSHOT runtime artifact
```
