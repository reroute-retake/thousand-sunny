# Changelog

All notable changes to **Project Thousand Sunny** documentation. Format loosely follows [Keep a Changelog](https://keepachangelog.com/). Landscape date: **July 2026**.

## [1.1.0] — 2026-07-14 — Hardening pass (independent review)

An external review validated the architecture and raised five resilience/operational gaps. All five are now addressed:

### Added
- **Tunnel resilience & provider fallback** ([doc 10](docs/10-external-access.md#tunnel-resilience--provider-fallback)) — the Oracle VPS is now treated as *replaceable*. Documented a provider-agnostic 15-minute rebuild kit (cloud-init/Ansible + config in encrypted git) and cheap paid fallbacks (RackNerd ~$11–22/yr, Hetzner CX22, Netcup) so a lost free instance never kills external access.
- **`waterseven`** — the hall VLAN switch is now a **named fleet member** with an exact model (TP-Link **TL-SG105E**; alt 2nd TL-SG108E) in [doc 01](docs/01-fleet.md) and wired through [doc 02](docs/02-network.md). `impeldown`'s VLAN-60 isolation explicitly depends on it.
- **Off-site USB encryption** ([doc 04](docs/04-storage.md)) — concrete **LUKS** and **ZFS-native-encryption** procedures, A/B drive rotation, and key-custody guidance for the rotated off-site drive.
- **Configuration backup & change management** ([doc 11](docs/11-security.md)) — OPNsense native `os-git-backup` → private Forgejo repo; honest note that the web-UI-only TL-SG108E/105E switches need semi-manual export; `oxidized` positioned for future SSH-capable gear; `crowsnest` alerts on stale backups.

### Changed
- **32 GB RAM + 2nd 4 TB mirror promoted from "roadmap" to 🔴 Day-0 blocking prerequisites** across the [README](README.md), [doc 03](docs/03-virtualization.md), [doc 04](docs/04-storage.md), and [doc 15](docs/15-roadmap.md) — with the Immich-face-scan / Nextcloud-indexing OOM risk called out explicitly.
- **`crowsnest`** role expanded to watch tunnel/VPS liveness and config-backup freshness ([doc 09](docs/09-observability.md)).
- **Limitation #9** (Oracle) now references the concrete fallback plan ([doc 15](docs/15-roadmap.md)).
- Shopping list re-prioritised: RAM + mirror flagged Day-0; `waterseven` raised to P2 (needed before `impeldown`).

## [1.0.0] — 2026-07-14 — Initial architecture

- Full fleet design (One Piece naming), network/VLAN segmentation, Proxmox VM/LXC layout with per-service sizing, ZFS storage + 3-2-1 backups, core services, media stack (incl. AllDebrid via Decypharr), productivity, **local LLM serving** (llama.cpp/Ollama/vLLM + LiteLLM), observability with LLM anomaly detection, **$0 external access** (Tailscale + Pangolin/WireGuard), security & ops, automation (Telegram YouTube-toggle, movie pipeline, reminders), `impeldown` cyber + retro dual-boot, sites & social, roadmap, and a full July-2026 version matrix.
