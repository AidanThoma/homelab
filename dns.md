# Internal DNS

## Server

AdGuard Home runs in a Debian LXC:

```text
IP: 192.168.4.4
DNS port: 53 TCP/UDP
```

The household router's DNS configuration is intentionally unchanged.

## DNS Rewrites

| Name | Address |
|---|---:|
| `proxmox.aidanthoma.com` | `192.168.4.2` |
| `docker.aidanthoma.com` | `192.168.4.3` |
| `adguard.aidanthoma.com` | `192.168.4.4` |
| `lubuntu.aidanthoma.com` | `192.168.4.5` |

## Test a Record Directly

```bash
nslookup docker.aidanthoma.com 192.168.4.4
```

Expected result:

```text
Name:    docker.aidanthoma.com
Address: 192.168.4.3
```

## Verify AdGuard Is Listening

```bash
sudo ss -lntup | grep ':53'
```

## Client Configuration

Only homelab systems that should use internal records need their DNS configured as:

```text
192.168.4.4
```

Do not change the router unless network-wide internal DNS is intentionally desired later.
