# Backups

## Current State

Document the current backup configuration here.

## Target Design

Recommended future design:

```text
Proxmox VMs/LXCs
      |
      v
Proxmox Backup Server
      |
      +-- Daily backups
      +-- Weekly retention
      +-- Periodic restore tests
```

## What Should Be Backed Up

- Proxmox VM/LXC configurations
- Docker Compose files
- Persistent Docker volumes
- OpenWebUI data
- Prometheus configuration
- AdGuard Home configuration
- Cloudflare configuration excluding secrets
- Infrastructure documentation

## Restore Testing

A backup is not considered reliable until a restore has been tested.

Record restore tests here:

| Date | System | Result | Notes |
|---|---|---|---|
| | | | |
