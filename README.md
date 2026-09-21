# Aidan's Homelab

Documentation for my Proxmox-based homelab used to learn virtualization, Linux administration, Docker, DNS, monitoring, networking, secure remote access, and self-hosted AI.

## Current Architecture

```text
                         Internet
                            |
                    Cloudflare Tunnel
                            |
                      Docker VM
                    192.168.4.3
                            |
             +--------------+--------------+
             |              |              |
         OpenWebUI      Prometheus      cAdvisor
                                           |
                                      Container metrics

     Proxmox Host -------------------- pve-exporter
     192.168.4.2                         |
          |                              |
          +-------------------------- Prometheus
          |
          +-- AdGuard Home LXC       192.168.4.4
          |
          +-- Lubuntu VM             192.168.4.5
```

## Hosts

| Host | Type | IP | Purpose |
|---|---|---:|---|
| Proxmox | Hypervisor | `192.168.4.2` | Runs VMs and LXCs |
| Docker | VM | `192.168.4.3` | Docker workloads and self-hosted services |
| DNS | Debian LXC | `192.168.4.4` | AdGuard Home internal DNS |
| Lubuntu | VM | `192.168.4.5` | Linux desktop / lab VM |

## Internal DNS

AdGuard Home provides DNS for selected homelab systems only. The household router DNS is intentionally unchanged.

Current internal records:

```text
proxmox.aidanthoma.com -> 192.168.4.2
docker.aidanthoma.com  -> 192.168.4.3
adguard.aidanthoma.com -> 192.168.4.4
lubuntu.aidanthoma.com -> 192.168.4.5
```

## Services

- Proxmox VE
- Docker
- OpenWebUI
- Cloudflare Tunnel
- Prometheus
- cAdvisor
- Proxmox exporter
- AdGuard Home
- SSH

## Documentation

- [Network](network.md)
- [Services](services.md)
- [DNS](dns.md)
- [Monitoring](monitoring.md)
- [Cloudflare](cloudflare.md)
- [Backups](backups.md)
- [Security](SECURITY.md)
- [Runbooks](runbooks/)

## Goals

- Centralize infrastructure documentation
- Make hosts reachable by memorable DNS names
- Monitor Proxmox and Docker workloads
- Keep management services off the public internet where possible
- Automate deployments and configuration over time
- Maintain reproducible recovery procedures

## Planned Improvements

- Grafana dashboards
- Alertmanager notifications
- Uptime Kuma
- Proxmox Backup Server
- Centralized logging with Grafana Loki / Alloy
- Ansible configuration management
- VLAN segmentation
- Tailscale or WireGuard for remote administration

## Security Notes

This repository must never contain passwords, API tokens, private keys, Cloudflare tunnel credentials, recovery codes, or other secrets.
