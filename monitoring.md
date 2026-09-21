# Monitoring

## Stack

```text
Proxmox ------> pve-exporter ---+
                              |
Docker -------> cAdvisor -------+--> Prometheus
```

## Prometheus

Prometheus currently monitors infrastructure and Docker/container metrics.

Useful checks:

```promql
container_memory_usage_bytes
```

OpenWebUI container presence:

```promql
container_last_seen{name="open-webui"}
```

## cAdvisor

Container name of interest:

```text
open-webui
```

Image:

```text
ghcr.io/open-webui/open-webui:main
```

## Planned

- Grafana dashboards
- Alertmanager
- Uptime Kuma
- Loki / Alloy centralized logging

## Suggested Alerts

- Disk utilization > 85%
- Host or VM unavailable
- Container unavailable
- Sustained high CPU
- Sustained high memory use
- Prometheus target down
