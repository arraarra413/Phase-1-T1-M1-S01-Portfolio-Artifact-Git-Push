# Security Architecture Document (SAD)
## Phase 1: Perimeter Hardening
* SSH Edits completed: PermitRootLogin no | PasswordAuthentication no
* Firewall configuration: UFW rules applied for ports 22 and 8080.

## Phase 2: Automated Auditor (Python Script)
* Script Location: ~/dc_auditor.py
* Output Targets: /var/log/dc_audit.log

## Phase 3: The Containerized Stack
* Container Logic: Air-gapped MySQL database isolated to internal backend network layout. Front-end Nginx exposed to proxy port 8080.
