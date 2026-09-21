# Network

![](diagrams\Homelab.png)

## LAN

| Setting | Value |
|---|---|
| Network | `192.168.4.0/24` |
| Gateway | `192.168.4.1` |
| Internal DNS | `192.168.4.4` |

The household router DNS is not modified. Only selected homelab machines are configured to use AdGuard Home.

## Address Plan

| Address | Host | Notes |
|---:|---|---|
| `192.168.4.1` | Router / gateway | Existing network gateway |
| `192.168.4.2` | Proxmox | Hypervisor |
| `192.168.4.3` | Docker VM | Container host |
| `192.168.4.4` | DNS LXC | AdGuard Home |
| `192.168.4.5` | Lubuntu VM | Linux desktop VM |

## Proxmox Networking

Document the active bridge and physical NIC here after confirming them on the host:

```bash
ip -br addr
ip route
cat /etc/network/interfaces
```

Typical layout:

```text
Physical NIC -> vmbr0 -> VMs/LXCs -> 192.168.4.0/24
```

## DNS Policy

- Proxmox host: may use `192.168.4.4`
- Docker VM: use `192.168.4.4`
- Other homelab guests: optionally use `192.168.4.4`
- AdGuard LXC itself: use an upstream resolver rather than depending solely on itself
- Household clients: unchanged
