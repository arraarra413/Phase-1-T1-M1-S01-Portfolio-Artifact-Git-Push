#!/usr/bin/env python3
import subprocess
import json

# Instruction 1: Capture the process list
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# Instruction 2: Check for the unauthorized process
if "unauthorized_cryptominer" in process_list.stdout:
    
    # Instruction 3: Create the alert
    alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": "unauthorized_cryptominer"
    }
    
    # Export to JSON
    with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
    
    print("[+] ALARM: Unauthorized process detected! security_alert.json created.")
else:
    print("[+] Audit Complete: No threats found.")
