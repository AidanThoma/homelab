# Security

## Never Commit

- Passwords
- API tokens
- SSH private keys
- Cloudflare tunnel credentials
- `.env` files containing secrets
- Recovery codes
- Session cookies
- Private certificates/keys

## General Practices

- Use named administrative users with `sudo` instead of routine direct root login.
- Prefer SSH key authentication.
- Restrict public exposure of management interfaces.
- Keep Proxmox, Debian, Ubuntu/Lubuntu, Docker images, and services updated.
- Back up important configuration before major changes.
- Use least privilege for service accounts and API credentials.

## SSH

Example hardening goals:

```text
PermitRootLogin no
PasswordAuthentication no   # after SSH keys are confirmed working
```

Do not disable password authentication until key-based login has been tested successfully from another terminal.
