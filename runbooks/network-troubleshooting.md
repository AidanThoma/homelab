# Runbook: Network Troubleshooting

## Address

```bash
ip -br addr
```

## Routing

```bash
ip route
```

## DNS Configuration

```bash
cat /etc/resolv.conf
resolvectl status
```

## DNS Test

```bash
nslookup docker.aidanthoma.com 192.168.4.4
```

## Listening Ports

```bash
sudo ss -lntup
```

## NetworkManager

```bash
nmcli device status
nmcli connection show
```
