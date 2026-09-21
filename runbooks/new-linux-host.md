# Runbook: Add a New Linux Host

## 1. Assign Networking

Choose an unused static address from the homelab address plan.

Verify:

```bash
ip -br addr
ip route
```

## 2. Configure DNS

Use:

```text
192.168.4.4
```

## 3. Create Administrative User

```bash
adduser aidan
usermod -aG sudo aidan
```

## 4. Enable SSH

Debian/Ubuntu:

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
```

## 5. Create DNS Record

Add a rewrite in AdGuard Home.

## 6. Test

```bash
nslookup HOSTNAME
ssh aidan@HOSTNAME
```

## 7. Document

Update:

- `network.md`
- `services.md`
- `README.md`
