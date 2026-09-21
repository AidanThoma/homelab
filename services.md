# Services

## Proxmox VE

* Host: `proxmox.aidanthoma.com`
* IP: `192.168.4.2`
* Web UI: `https://proxmox.aidanthoma.com:8006`
* Listening ports:

  * TCP `8006` — Proxmox web interface / API
  * TCP `22` — SSH
  * TCP `9221` — Proxmox exporter metrics

## Docker Host

* Host: `docker.aidanthoma.com`
* IP: `192.168.4.3`
* Primary role: container host
* Listening ports:

  * TCP `22` — SSH
  * TCP `3000` — OpenWebUI
  * TCP `9090` — Prometheus
  * TCP `8080` — cAdvisor
* SSH example:

```bash
ssh aidan@docker.aidanthoma.com
```

## AdGuard Home

* Host: `adguard.aidanthoma.com`
* IP: `192.168.4.4`
* Purpose: internal DNS for selected homelab devices
* Listening ports:

  * UDP `53` — DNS
  * TCP `53` — DNS
  * TCP `80` — AdGuard Home web interface
  * TCP `22` — SSH
* Initial setup only:

  * TCP `3000` — AdGuard Home setup interface

## Lubuntu

* Host: `lubuntu.aidanthoma.com`
* IP: `192.168.4.5`
* Purpose: Linux desktop / lab VM
* Listening ports:

  * TCP `22` — SSH

## OpenWebUI

* Runs on Docker VM
* Host IP: `192.168.4.3`
* Container image: `ghcr.io/open-webui/open-webui:main`
* Container name: `open-webui`
* Port mapping:

```text
Docker Host TCP 3000 -> Container TCP 8080
```

* Internal container port:

  * TCP `8080`
* Host listening port:

  * TCP `3000`
* External access is handled through Cloudflare Tunnel

## Prometheus

* Runs on Docker VM
* Host IP: `192.168.4.3`
* Listening port:

  * TCP `9090` — Prometheus web interface and API
* Collects infrastructure and container metrics
* Data sources currently include:

  * cAdvisor
  * Proxmox exporter

## cAdvisor

* Runs on Docker VM
* Host IP: `192.168.4.3`
* Listening port:

  * TCP `8080` — container metrics endpoint
* Exposes Docker container metrics to Prometheus

## Proxmox Exporter

* Runs for monitoring the Proxmox host
* Proxmox IP: `192.168.4.2`
* Listening port:

  * TCP `9221` — Prometheus metrics endpoint
* Exposes Proxmox node, VM, LXC, storage, and infrastructure metrics to Prometheus

## Port Summary

| Host          |   Port | Protocol | Service              |
| ------------- | -----: | -------- | -------------------- |
| `192.168.4.2` |   `22` | TCP      | Proxmox SSH          |
| `192.168.4.2` | `8006` | TCP      | Proxmox Web UI / API |
| `192.168.4.2` | `9221` | TCP      | Proxmox Exporter     |
| `192.168.4.3` |   `22` | TCP      | Docker VM SSH        |
| `192.168.4.3` | `3000` | TCP      | OpenWebUI            |
| `192.168.4.3` | `8080` | TCP      | cAdvisor             |
| `192.168.4.3` | `9090` | TCP      | Prometheus           |
| `192.168.4.4` |   `22` | TCP      | AdGuard LXC SSH      |
| `192.168.4.4` |   `53` | TCP/UDP  | AdGuard DNS          |
| `192.168.4.4` |   `80` | TCP      | AdGuard Web UI       |
| `192.168.4.5` |   `22` | TCP      | Lubuntu SSH          |

## Notes

Not every listening port should be reachable from outside the homelab.

Cloudflare Tunnel is used for selected externally accessible services without directly exposing service ports through the household router.

Administrative services such as Proxmox, SSH, Prometheus, cAdvisor, and AdGuard Home should remain restricted to trusted management networks unless explicitly required.