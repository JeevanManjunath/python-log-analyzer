from collections import defaultdict
from datetime import datetime
import time

log_file = "server.log"
blacklist_file = "blacklist.txt"
report_file = "suspicious_report.txt"

failed_attempts = defaultdict(int)

# Load blacklist
blacklisted_ips = set()
with open(blacklist_file, "r") as file:
    for line in file:
        blacklisted_ips.add(line.strip())

print("Real-time log monitoring started...\n")

while True:

    with open(log_file, "r") as file:
        for line in file:
            parts = line.split(" - ")
            ip = parts[0]
            status = parts[1].strip()

            if ip in blacklisted_ips:
                print(f"BLOCKED IP DETECTED: {ip}")

            if status == "Login Failed":
                failed_attempts[ip] += 1

    print("\nFailed Login Analysis\n")

    suspicious_ips = []

    for ip, count in failed_attempts.items():
        print(f"{ip} -> {count} failed attempts")

        if count >= 3:
            print(f"ALERT: Possible brute force attack from {ip}")
            suspicious_ips.append((ip, count))

    with open(report_file, "w") as report:
        report.write("Suspicious Login Activity Report\n")
        report.write(f"Generated at: {datetime.now()}\n\n")

        for ip, count in suspicious_ips:
            report.write(f"{ip} - {count} failed login attempts\n")

    print("\nReport updated...\n")

    time.sleep(5)