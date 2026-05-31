# Week 01 — Linux Fundamentals & Filesystem Navigation
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
During this introductory session, I established core competencies in Linux systems administration and command-line interactions. I focused heavily on navigating hierarchical filesystems securely, evaluating directory ownership, and manipulating absolute and relative paths. Understanding these foundational administrative structures is critical for performing routine configuration auditing and identifying unauthorized system access.

## Artifacts
*   **system_auditor.py**
    This script automates the process of auditing local system configurations and verifying file integrity across critical directories. I modified its permissions to make it an executable tool capable of reviewing standard system states.

## Challenges & How I Solved Them
Initially, understanding the absolute distinction between relative and absolute directory paths caused minor navigation friction during automated script execution. I resolved this challenge by systematically tracing my environment's working directories using the `pwd` command and explicitly stating full environment paths within my automation scripts to prevent broken directory links.

## Reflection
Mastering command-line operations is a non-negotiable prerequisite for effective security operations. Moving away from graphical interfaces forces a deeper operational understanding of the underlying operating system architecture.

## References
*   The Linux Documentation Project. (2024). *The Linux system administrator's guide*. https://tldp.org
- 
