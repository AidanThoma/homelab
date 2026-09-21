# Cloudflare

## Purpose

Cloudflare Tunnel provides external access to selected services without directly forwarding inbound router ports.

## Current Use

OpenWebUI is exposed through Cloudflare Tunnel.

## Operational Notes

- Keep tunnel credentials out of this repository.
- Keep API tokens out of this repository.
- Do not commit `config.yml` if it contains sensitive identifiers or credentials.
- Prefer private VPN access for administrative interfaces such as Proxmox and SSH.

## Useful Checks

```bash
systemctl status cloudflared
cloudflared --version
```

## Planned

Consider Tailscale or WireGuard for private remote administration while continuing to use Cloudflare Tunnel for intentionally published web applications.
