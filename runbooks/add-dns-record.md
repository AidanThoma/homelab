# Runbook: Add an Internal DNS Record

1. Open the AdGuard Home dashboard.
2. Navigate to DNS rewrites.
3. Add the hostname and IP address.
4. Test directly against AdGuard:

```bash
nslookup HOSTNAME 192.168.4.4
```

5. Test from a client configured to use AdGuard:

```bash
nslookup HOSTNAME
```
