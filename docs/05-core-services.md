# 05 · Core Services (`bartolomeo`)

The network brain. These run on/next to OPNsense and everything else depends on them.

| Service | Version (Jul 2026) | Role | Docs |
|---|---|---|---|
| **OPNsense** | 26.1.10 *(26.7 lands ~Jul 15)* | Firewall, router, VLANs, WireGuard, DHCP | [docs.opnsense.org](https://docs.opnsense.org/) |
| **AdGuard Home** | 0.107.75 | LAN DNS, ad/tracker block, DoH upstream, DNS rewrites | [AdGuardHome wiki](https://github.com/AdguardTeam/AdGuardHome/wiki) |
| **Unbound** | current | Recursive, DNSSEC-validating resolver behind AdGuard | [unbound docs](https://unbound.docs.nlnetlabs.nl/) |
| **Caddy** | 2.10.x | Reverse proxy, automatic TLS, service names | [caddyserver.com/docs](https://caddyserver.com/docs/) |
| **Authelia** | 4.39.20 | SSO + MFA forward-auth in front of Caddy | [authelia.com](https://www.authelia.com/) |
| **Vaultwarden** | 1.36.0 | Bitwarden-compatible password vault (family) | [wiki](https://github.com/dani-garcia/vaultwarden/wiki) |
| **CrowdSec** | current | Behavioral IPS + community blocklist + bouncers | [docs.crowdsec.net](https://docs.crowdsec.net/) |

## Why these (vs the alternatives)
- **OPNsense over pfSense CE** — predictable bi-weekly patching, native in-kernel WireGuard, clean single-codebase (no CE/Plus feature gating), full REST API. pfSense CE is fine but its release cadence has been erratic.
- **AdGuard Home over Pi-hole** — built-in DoH/DoT/DoQ upstream with no companion container, modern per-client policies (needed for the [YouTube toggle](12-automation.md)), lighter idle footprint.
- **Caddy over Traefik/NPM** — zero-config automatic HTTPS is the cleanest way to give every service a name + cert. Traefik wins only in fast-churning Docker-label environments; NPM is heavier. (Pangolin, a Traefik-based tunnel, is used on the *VPS* — see [10](10-external-access.md).)
- **Authelia over Authentik** — a lightweight Go forward-auth gateway is the right size here; Authentik's full IdP (SAML/SCIM/flows) is the documented "phase 2" if the service count explodes.
- **CrowdSec over fail2ban** — community threat intel + bouncers at both the firewall and proxy. (Never run both as the enforcing authority on one host.)

## DNS pipeline
```
client → AdGuard Home (filter + rewrites *.sunny.home) → Unbound (recursive, DNSSEC) → root servers
                         └── *.sunny.home → Caddy → service:port
```
- Blocklists: OISD Big + a light regional list; per-client rules power the YouTube automation.
- Upstream (for non-local, if not fully recursive): DoH to keep the ISP out of your DNS.

## Reverse proxy & names
Caddy holds one route per service. Example (sanitized) `Caddyfile`:
```caddy
jellyfin.sunny.home   { reverse_proxy 10.10.20.11:8096 }
immich.sunny.home     { reverse_proxy 10.10.20.12:2283 }
git.sunny.home        { reverse_proxy 10.10.20.15:3000 }
# admin surfaces sit behind Authelia:
proxmox.sunny.home {
    forward_auth 10.10.10.1:9091 { uri /api/authz/forward-auth }
    reverse_proxy https://10.10.20.2:8006 { transport http { tls_insecure_skip_verify } }
}
```
Internal certs via Caddy's `internal` CA (trust the root on family devices) or Let's Encrypt **DNS-01** for a real domain.

## Identity & secrets
- **Authelia**: `one_factor` for low-risk apps (Jellyfin has its own login), `two_factor` (TOTP/WebAuthn) for admin surfaces (Proxmox, OPNsense, Dockge, n8n). Backed by the Vaultwarden-adjacent user store or a small LLDAP.
- **Vaultwarden**: the family password manager; also stores API keys/tokens the automations use. Itself protected by Authelia + its own master passwords, backed up in the *critical* off-site tier ([04](04-storage.md)).

## Hardening highlights
- Mgmt surfaces (OPNsense, switch, Proxmox) reachable **only from VLAN 10** + Authelia MFA.
- CrowdSec firewall bouncer on OPNsense + Caddy bouncer at the proxy.
- WAN exposes **nothing** inbound (CGNAT helps here); all external reach is via the VPS tunnel ([10](10-external-access.md)).

Next: **[06 · Media stack →](06-media-stack.md)**
