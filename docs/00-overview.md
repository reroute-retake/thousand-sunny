# 00 · Overview & Principles

## Why this project exists

Three things drove the build:

1. **A family that actually uses it.** Media for everyone, photos backed up off phones, a password manager the whole house shares, notes for the kids, and Jellyfin that grandparents can open from their own living room.
2. **A place to run local AI.** A 16 GB and (soon) 32 GB GPU shouldn't sit idle — they should serve LLMs to every machine, and make Immich and Paperless smarter for free.
3. **A portfolio.** The interesting part of a homelab isn't the app list — it's the *decisions*: how CGNAT was beaten for ₹0/month, why the sandbox is a dead-end VLAN, why the NAS runs Proxmox instead of TrueNAS. These docs foreground the decisions.

## Goals & non-goals

| ✅ Goals | ❌ Non-goals |
|---|---|
| Family-usable, name-based access to every service | 100% uptime / enterprise HA |
| $0 recurring cost for external access | Buying rack gear or a dedicated GPU server |
| Local LLMs reachable from all machines | Cloud LLM API dependence |
| Strong segmentation & a real cyber-lab that can't leak | Exposing raw ports to the internet |
| Low-effort, staged upgrades | Chasing every bleeding-edge `:latest` tag |

## What runs where (one-paragraph tour)

`bartolomeo` (the N150 with dual NICs) is the **network brain** — OPNsense routing/firewall, AdGuard Home + Unbound for DNS, Caddy as the reverse proxy that gives every service a name and a cert, and Authelia + Vaultwarden for identity and secrets. `poneglyph` (the Minisforum N5) is the **workhorse** — Proxmox VE hosting the media stack, Immich, documents, git, and Nextcloud on a ZFS mirror. `vegapunk` (RTX 5070 Ti) **serves LLMs** today; `pluton` (AMD R9700) takes that crown in ~2 months. `impeldown` (Beelink) is a **locked room** — a cyber sandbox and a retro-gaming boot, reachable only from `chopper`. Two free Oracle VPSs — `puffingtom` and `crowsnest` — live on the public internet to provide **reach and an outside vantage point**.

## Recommended additions (beyond the original wishlist)

These earned their place during research and appear throughout the docs:

| Addition | Why it adds value | Doc |
|---|---|---|
| **Unbound** (recursive DNS behind AdGuard) | Full DNS privacy — no third-party resolver sees your queries | [05](05-core-services.md) |
| **CrowdSec** (over fail2ban) | Community threat intel + multi-layer bouncers; great portfolio piece | [11](11-security.md) |
| **LiteLLM** proxy | One OpenAI-compatible endpoint in front of both GPU boxes, with failover | [08](08-ai-llm.md) |
| **Grafana Loki + Alloy** | Centralized logs; the substrate for LLM-based anomaly detection | [09](09-observability.md) |
| **Beszel + Uptime Kuma** | Featherweight metrics + uptime, sane for a 16 GB NAS | [09](09-observability.md) |
| **Proxmox Backup Server** (LXC) | Deduplicated, verifiable VM/CT backups; restore drills | [04](04-storage.md) |
| **Karakeep** (ex-Hoarder) | AI-tagged bookmark/read-later, reuses the local LLM | [08](08-ai-llm.md) |
| **ntfy** | Dead-simple push notifications for automations & alerts | [12](12-automation.md) |
| **Homepage** dashboard | Single front door with live service widgets | [09](09-observability.md) |
| **Dockge/Komodo** (optional) | Git-driven compose management if you prefer it to bare compose | [03](03-virtualization.md) |

## How to read these docs

- Each service names its **exact July 2026 version** and links **official docs**. The master list is [`16-versions.md`](16-versions.md).
- Diagrams are **Mermaid**, so they render on GitHub without images.
- **Callouts** flag the honest trade-offs:

> [!WARNING]
> Where hardware or the ISP imposes a hard limit, you'll see a warning like this instead of hand-waving.

Next: **[01 · The Fleet →](01-fleet.md)**
