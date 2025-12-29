# Security Log Analyzer

A lightweight Python-based security tool for analyzing Linux authentication logs and detecting repeated failed SSH login attempts that may indicate brute-force attacks.

---

## Overview

Linux systems record all authentication activity in log files such as `/var/log/auth.log`.  
Manually reviewing these logs is inefficient and error-prone, especially when identifying repeated failed login attempts.

This project demonstrates **core security monitoring concepts** by implementing a command-line tool that parses Linux SSH authentication logs, aggregates failed login attempts by source IP, and flags suspicious behavior using threshold-based detection.

The tool simulates a **basic SOC (Security Operations Center) log analysis workflow**.

---

## Features

- Parses Linux SSH authentication log entries  
- Detects repeated failed login attempts  
- Aggregates attempts by source IP address  
- Flags potential brute-force activity using configurable thresholds  
- Generates a structured security analysis report  

---

## How It Works

1. Reads a Linux authentication log file provided by the user  
2. Identifies failed SSH login events using pattern matching  
3. Extracts source IP addresses from log entries  
4. Counts failed attempts per IP  
5. Flags IPs exceeding a defined threshold  
6. Outputs results to the terminal and a report file  


Environment
OS: Linux (Kali Linux)
Language: Python 3
Execution: Command-line interface (CLI)


