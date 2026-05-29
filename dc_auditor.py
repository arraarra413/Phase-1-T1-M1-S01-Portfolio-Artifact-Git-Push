import os
dc_ip = "10.0.0.4"
log_path = "/var/log/dc_audit.log"
response = os.system(f"ping -c 4 {dc_ip} > /dev/null 2>&1")
status_msg = "DC is UP\n" if response == 0 else "DC is DOWN\n"
with open(log_path, "a") as log_file:
    log_file.write(status_msg)
