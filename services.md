# Services

## Proxmox VE

- Host: `proxmox.aidanthoma.com`
- IP: `192.168.4.2`
- Web UI: `https://proxmox.aidanthoma.com:8006`

## Docker Host

- Host: `docker.aidanthoma.com`
- IP: `192.168.4.3`
- Primary role: container host
- SSH example:

```bash
ssh aidan@docker.aidanthoma.com
```

## AdGuard Home

- Host: `adguard.aidanthoma.com`
- IP: `192.168.4.4`
- DNS: TCP/UDP `53`
- Purpose: internal DNS for selected homelab devices

## Lubuntu

- Host: `lubuntu.aidanthoma.com`
- IP: `192.168.4.5`
- SSH: enabled

## OpenWebUI

- Runs on Docker VM
- Container image: `ghcr.io/open-webui/open-webui:main`
- Container name: `open-webui`
- External access is handled through Cloudflare Tunnel

## Prometheus

- Runs on Docker VM
- Collects infrastructure and container metrics
- Data sources currently include:
  - cAdvisor
  - Proxmox exporter

## cAdvisor

- Runs on Docker VM
- Exposes Docker container metrics to Prometheus

## Proxmox Exporter

- Exposes Proxmox metrics to Prometheus
