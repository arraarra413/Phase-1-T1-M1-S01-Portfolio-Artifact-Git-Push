# Week 02 — Networking & Protocol Analysis
**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

## What I Learned
This week focused on network communication architectures, protocol stacks, and transport-layer mechanisms. I analyzed how data packages move across networks and learned how to identify common network-facing exposure points. Mapping open ports and active services is essential for discovering unauthorized entry vectors within an enterprise perimeter.

## Artifacts
*   **port_check.py**
    This script acts as a localized network reconnaissance utility. It functions by programmatically testing targeted local ports to determine their connection states and evaluate potential service exposure.

## Challenges & How I Solved Them
During execution, the network checking utility generated socket connection timeouts when interacting with closed or firewalled network boundaries. I addressed this by integrating structural error-handling blocks to gracefully capture connection exceptions, allowing the tool to continue scanning without crashing.

## Reflection
Analyzing network traffic and port states changes how one views system connectivity. Perimeter awareness is the first line of defense in establishing a hardened environment.

## References
*   Nmap Project. (2026). *Nmap Network Mapper reference guide*. https://nmap.org
- 
