# Retrospective Hunt Playbook

## Time window

Start with the earliest available evidence before public disclosure and extend through the current retention window. The source reporting shows that staging, log processing and persistence can be separated in time.

## Search order

```text
1. exploit-specific log marker
2. staged payload marker
3. vulnerable script processing
4. filesystem artifacts
5. configuration changes
6. privileged-account changes
7. outbound connections
8. C2/certificate pivots
```

## Evidence preservation

Create a timeline with:

- first malicious HTTP request
- first malicious authentication request
- vulnerable script execution/processing
- first shell command
- first downloaded payload
- persistence creation
- first outbound C2
- last observed attacker activity

## Artifact integrity

Hash recovered files immediately and compare against the repository feed. Keep original copies even where the attacker is known to delete the staging artifacts.
