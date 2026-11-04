# Computer Networks — facts and worked examples

## Layers
| OSI | Role | TCP/IP | Examples |
| --- | --- | --- | --- |
| 7 Application | user services | Application | HTTP, FTP, SMTP, DNS |
| 6 Presentation | encoding, encryption | Application | TLS, JPEG |
| 5 Session | sessions | Application | – |
| 4 Transport | end-to-end, ports | Transport | TCP, UDP |
| 3 Network | logical addressing, routing | Internet | IP, ICMP |
| 2 Data Link | frames, MAC | Link | Ethernet, switch |
| 1 Physical | bits | Link | cables, hubs |

Mnemonic (top-down): "All People Seem To Need Data Processing". Protocol Data Units: segment (transport), packet (network), frame (data link), bits (physical).

## TCP vs UDP
| | TCP | UDP |
| --- | --- | --- |
| Connection | Connection-oriented (3-way handshake: SYN, SYN-ACK, ACK) | Connectionless |
| Reliability | Ordered, retransmits, flow and congestion control | Best effort |
| Use | Web, email, file transfer | DNS queries, streaming, VoIP |

## Common port numbers
HTTP 80, HTTPS 443, FTP 21, SSH 22, SMTP 25, DNS 53, DHCP 67/68 (UDP).

## Devices
Hub (L1, broadcasts), switch (L2, uses MAC table), router (L3, uses IP), gateway (connects different protocols/networks).

## IP addressing worked example
192.168.1.0/26: 32 − 26 = 6 host bits → 2^6 = 64 addresses, 64 − 2 = **62 usable hosts** (network and broadcast addresses excluded). Subnet mask 255.255.255.192. Block size 64, so subnets start at .0, .64, .128, .192.
Formula: usable hosts = 2^(32 − prefix) − 2.

## Common MCQ traps
- A switch does not forward by IP; a router does.
- ARP maps IP → MAC; DNS maps name → IP.
- TCP is not "faster" than UDP; UDP has less overhead.
- IPv4 is 32 bits; IPv6 is 128 bits.
- Private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
