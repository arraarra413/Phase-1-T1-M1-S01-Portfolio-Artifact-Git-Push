import subprocess
import json
import os

output_path = os.path.expanduser("~/threat_report.json")

# Phase 1: Interrogate Logs
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)
raw_output = result.stdout

# Phase 2: Data Parsing
lines = raw_output.split('\n')
attacker_ips = []

for line in lines:
    if line:
        parts = line.split(" ")
        if len(parts) > 10:
            attacker_ips.append(parts[10])

# Phase 3: The Export
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": list(set(attacker_ips))
}

with open(output_path, "w") as file:
    json.dump(alert_data, file, indent=4)

print(f"[+] Threat Hunt Complete. Report generated at: {output_path}")

