# Public Repository Design Rationale

## Include

### 1. Machine-readable IOCs
`iocs/iocs.csv` is the canonical feed. JSON and STIX provide common ingestion formats.

### 2. High-fidelity detections
The 88771 exploit-core YARA rule deliberately requires multiple NetScaler-specific artifacts instead of a large OR list of generic shell commands.

### 3. SOC / DFIR workflows
Hunt order, evidence preservation, timeline reconstruction and escalation criteria are included because an IOC hit alone does not establish compromise.

### 4. Visual explanation
Mermaid diagrams and the browser IOC explorer help security researchers and executives understand the attack chain without reading the entire report.

### 5. Source and confidence metadata
Every IOC records source, role and confidence so downstream users can distinguish direct observation from context or unattributed infrastructure.

## Exclude from the public repository

### Exact credentials and authentication secrets
The supplied research includes web-shell passwords, CSRF values and other credential-like material. These are not operationalized in the public IOC feed.

### Full weaponized exploit chains
A public defender repository does not need to redistribute complete copy/paste attack chains. The stable exploit markers, command-pattern fragments and behavioral correlations provide the defensive value.

### Victim/customer data
No customer identifiers, raw logs, private configuration or incident-specific secrets belong in the repo.

### Generic ATT&CK noise
Do not add standalone `curl`, `wget`, `python`, `perl`, `tar`, `id` or `whoami` rules as CVE-2026-88771 detectors.

## Why this structure scales

The exploit primitive is relatively stable while attacker infrastructure changes rapidly. Keeping them in separate layers lets detection engineers preserve signal while threat researchers continuously enrich the IOC feed.
