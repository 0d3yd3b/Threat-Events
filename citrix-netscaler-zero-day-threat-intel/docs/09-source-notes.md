# Source Notes & Confidence

## Source-derived facts

This repository is intentionally based on the materials supplied during the research process. The sources include vendor research, CERT-EU, technical exploitation analysis, community/sensor reporting, and user-supplied samples.

## Confidence semantics

| Label | Meaning |
|---|---|
| observed | Directly reported in the source as seen on a target/sensor/sample |
| sample | Present in an analyzed malware/exploit sample supplied or cited by the source |
| contextual | Useful context but not sufficient alone to prove exploitation |
| capability | Supported as a framework/tool capability; not necessarily observed on the NetScaler victim |
| unattributed | Observed infrastructure/tooling that the source does not confidently tie to one campaign |

## Attribution caution

The source material explicitly distinguishes original/pre-disclosure activity from post-disclosure scanning and opportunistic exploitation. The repository therefore avoids assigning every IOC to one actor.

## Source references

- https://tenex.ai/blog/what-tenex-observed-inside-active-exploitation-of-netscaler-zero-day/
- https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- https://www.levelblue.com/blogs/spiderlabs-blog/citrix-netscaler-cve-2026-88771-observed-exploitation-artifacts-and-hunt-indicators
- https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances
- CERT-EU — security advisory on active NetScaler exploitation (28 Sep 2026)
