# `deploy/` — puffingtom rebuild kit

This is the **provider-agnostic rebuild kit** referenced in [`docs/10-external-access.md`](../docs/10-external-access.md#tunnel-resilience--provider-fallback). It rebuilds the public edge (`puffingtom`) — the CGNAT-bypass tunnel + reverse proxy — on **any** VPS (Oracle, RackNerd, Hetzner, Netcup…) in ~15 minutes, so losing the free Oracle instance never kills external access.

> [!WARNING]
> **Everything here is a sanitized template.** No real keys, IPs, or domains are committed. Copy the `*.example` files, fill in values from Vaultwarden/SOPS, and keep the filled versions out of git (see [`.gitignore`](../.gitignore)).

## Two paths, same goal

| Path | What runs on `puffingtom` | Home side | When to use |
|---|---|---|---|
| **A · WireGuard + Caddy** *(primary)* | `wireguard` + `caddy` (Ansible-managed) | OPNsense WireGuard client dials out | Fully declarative, minimal moving parts, easiest to reason about |
| **B · Pangolin + Newt** *(alternative)* | `pangolin` + `gerbil` + `traefik` (Docker) | `newt` connector (Docker) dials out | You want the GUI/SSO/per-resource rules from doc 10 |

Both are CGNAT-safe because **home always dials outbound**; the VPS only needs a public IPv4 + open 80/443 + WireGuard UDP.

## Layout
```
deploy/
├── cloud-init/puffingtom.cloud-init.yaml   # first-boot hardening + Docker (paste into any VPS)
├── ansible/                                # Path A, declarative (roles: common, wireguard, caddy)
│   ├── site.yml  inventory.example.ini  group_vars/edge.example.yml
│   └── roles/{common,wireguard,caddy}/…
├── wireguard/                              # reference confs (VPS + home peer)
├── caddy/Caddyfile.example                 # public site → home service map
├── pangolin/                               # Path B compose (VPS server + home newt)
└── .env.example
```

## Quick start (Path A)
```bash
# 1) Spin any VPS with an Ubuntu 24.04 image; paste cloud-init/puffingtom.cloud-init.yaml as user-data.
# 2) From your workstation:
cd deploy/ansible
cp inventory.example.ini inventory.ini            # set the VPS IP
cp group_vars/edge.example.yml group_vars/edge.yml # fill domain + keys (or use SOPS/ansible-vault)
ansible-galaxy collection install -r requirements.yml
ansible-playbook site.yml
# 3) Repoint DNS (A record) to the new VPS IP. Caddy auto-issues TLS. Done.
```

The full step-by-step (including key generation and the OPNsense side) is in [`../docs/runbooks/00-tunnel-rebuild.md`](../docs/runbooks/00-tunnel-rebuild.md). Provider-specific notes (RackNerd/Hetzner/Netcup) are in [`../docs/runbooks/01-provider-notes.md`](../docs/runbooks/01-provider-notes.md).
