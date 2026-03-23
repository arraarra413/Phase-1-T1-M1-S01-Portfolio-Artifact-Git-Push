#!/bin/bash
# Cyber-Fellowship System Hardening Script
echo "[*] Initializing System Hardening..."

# Remediation of /etc/shadow
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow

# Securing the local Vault
mkdir -p ~/Vault
chmod 700 ~/Vault

echo "[+] System Posture: GOLD."
