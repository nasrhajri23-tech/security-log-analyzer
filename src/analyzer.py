#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

if len(sys.argv) != 2:
    print("Usage: ./analyzer.py <log_file>")
    sys.exit(1)

LOG_FILE = sys.argv[1]

FAILED_PATTERN = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
THRESHOLD = 5


def read_logs(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def detect_failed_logins(logs):
    failed_attempts = defaultdict(int)

    for line in logs:
        match = re.search(FAILED_PATTERN, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

    return failed_attempts


def main():
    logs = read_logs(LOG_FILE)
    results = detect_failed_logins(logs)

    print("Security Log Analysis Report")
    print("----------------------------")

    for ip, count in results.items():
        if count >= THRESHOLD:
            print(f"[ALERT] Possible brute-force attack from {ip} ({count} failed attempts)")
        else:
            print(f"[INFO] {ip}: {count} failed attempts")


if __name__ == "__main__":
    main()

