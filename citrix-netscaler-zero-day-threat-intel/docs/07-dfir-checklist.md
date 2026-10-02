# DFIR Checklist

## Preserve before cleanup

- NetScaler VPX snapshot
- Remote syslog copies
- NetScaler Console evidence
- Technical support bundle
- Packet engine core dump
- Firewall / proxy / DNS flow records
- Relevant filesystem metadata

## 88771 compromise checks

- Search `/var/log/ns.log` for `pitboss` / `PPE` / `NSPPE` combinations.
- Search `/var/log/httpaccess-vpn.log` for suspicious Base64-bearing User-Agent values.
- Inspect `/netscaler/ns_monuploadd_err.pl` activity and processing timestamps.
- Check `/flash/nsconfig/ns.conf` for unauthorized users, especially `sec_monitor`.
- Compare `/etc/httpd.conf` with a known-good baseline.
- Check for PHP engine unexpectedly enabled.
- Check for new `<Files>`, `Alias`, and `AliasMatch` entries.
- Check `/bin/sh` permissions and SUID/SGID bits.
- Inspect `/var/netscaler/logon/LogonPoint/` for hidden web shells.
- Check `/var/python/bin/customsnmpd` and process history.
- Search for `/var/1.py`, `/var/tmp/.nsmon`, `/tmp/update_result_3567cs.tgz`, and related artifacts.
- Review outbound connections from the appliance.

## 88772 compromise checks

- Inspect UDP/443 DTLS activity.
- Correlate SSL handshake failures with NSPPE process exits.
- Search `/vpn/scripts/linux/` for unexpected `.deb`/`.sig`/PHP content.
- Inspect `/var/netscaler/.ns_suidcmd` use.
- Check `/tmp/.uxdport` and `/tmp/.uxdlock`.
- Review cron entries and `/var/log/sh.log`.
- Look for SUID `/bin/sh`.

## Persistence indicators

- Unexpected local privileged users
- Root cron jobs
- SUID/SGID changes
- HTTPD configuration persistence
- PHP execution enabled where it should remain off
- Web-accessible malicious files under legitimate appliance content roots

## Eradication caution

Do not treat patching alone as eradication. The source reporting explicitly warns that an attacker who already established persistence may retain access after software is updated.
