# Changelog

All notable changes to **Project Thousand Sunny** documentation. Format loosely follows [Keep a Changelog](https://keepachangelog.com/). Landscape date: **July 2026**.

## [1.7.1] — 2026-07-14 — CI first-run fixes

### Fixed
- **Mermaid** (2 diagrams): removed a backslash-escaped quote in the [network topology](docs/02-network.md) (`Bravia 55\"` → `55-inch`) and quoted a parenthesised decision node in the [ops upgrade flow](docs/11-security.md) — both were Mermaid parse errors.
- **markdown-lint**: disabled `MD051` (link-fragments) — the `internal-links` job already validates fragments with GitHub-accurate slugs, and markdownlint's slugger diverges on punctuated headings.
- **external-links** (advisory): added `.lycheeignore` for `docs.paperless-ngx.com`, which bot-blocks link checkers with HTTP 403 (the link itself is valid).

## [1.7.0] — 2026-07-14 — CI validation

### Added
- **GitHub Actions `validate` workflow** (`.github/workflows/validate.yml`), on push/PR: **markdownlint** (markdownlint-cli2), **Mermaid** diagram parse (mermaid-cli), **yamllint**, **`docker compose config`** across every `stacks/` + `deploy/pangolin/` file, an **internal link + heading-anchor** check (`scripts/check-internal-links.py`, GitHub-compatible slugs), and an **advisory external-link** check (lychee). Tuned configs `.markdownlint.jsonc` + `.yamllint.yml`; helper `scripts/extract-mermaid.py`. **CI badge** added to the README.

### Changed
- `stacks/ct-media/docker-compose.yml` rewritten **without YAML merge keys** (`<<:`) so `docker compose config` validates across all Compose versions — identical behaviour (same images/limits/volumes/env).

## [1.6.1] — 2026-07-14 — denden SSID→VLAN mapping (review)

### Changed
- Runbook 06 §5 now maps SSIDs → VLANs with the cleaner DSA-native **`option vid` on `network 'lan'`** (drops the per-VLAN interface stanzas for a single `lan`/`br-lan` handle). Documented the `br-lan.X` + `option network` form as an **equally valid alternative** — it's the official OpenWrt VLAN-wiki pattern and bridges correctly *without* `option type 'bridge'` (netifd auto-detects the VLAN-aware bridge), so it was never broken. Added a `bridge vlan show` verification step and flagged the LuCI 24.10.1 VLAN-picker save regression.

## [1.6.0] — 2026-07-14 — denden OpenWrt runbook

### Added
- **`docs/runbooks/06-denden-openwrt.md`** — flash the Archer AC1750 to OpenWrt and run it as a VLAN-aware **dumb AP** (Option A of the denden trap): exact model/rev verification, factory flash + **TFTP recovery** fallback, dumb-AP conversion (no DHCP/WAN/firewall), **DSA `bridge-vlan`** config matching `sabaody` port 5 (native VLAN 30, tagged 10/20/40/50; `vegapunk` untagged VLAN 20; mgmt VLAN 10), SSID→VLAN mapping, verification incl. the **"no mgmt on Wi-Fi"** check, and failsafe/TFTP rollback. Linked from [doc 01](docs/01-fleet.md) and [runbook 05](docs/runbooks/05-switch-vlan-config.md).

## [1.5.1] — 2026-07-14 — denden AP trunk trap (review)

### Fixed
- **Study riser (`sabaody` port 5) no longer sends Mgmt untagged.** Native/PVID changed VLAN 10 → **VLAN 30 (Trusted)**, tagged 10,20,40,50 — so a stock, non-VLAN-aware `denden` can't dump the Management VLAN onto upstairs Wi-Fi, and mgmt only ever travels tagged.

### Added
- **"The `denden` AP trunk trap"** in [runbook 05](docs/runbooks/05-switch-vlan-config.md#the-denden-ap-trunk-trap) — the stock-firmware VLAN gotcha (untagged→Wi-Fi leak, dropped 802.1Q tags) with three fixes: A) OpenWrt (recommended), B) an upstairs switch (`skypiea`), C) access-port VLAN 30. Reflected in [doc 01](docs/01-fleet.md) (`denden` flags OpenWrt as effectively required), [doc 02](docs/02-network.md) (port-5 native = 30), and [doc 15](docs/15-roadmap.md) (limitation #8 + optional `skypiea` shopping row).

## [1.5.0] — 2026-07-14 — Switch VLAN runbook

### Added
- **`docs/runbooks/05-switch-vlan-config.md`** — exact 802.1Q port maps for `sabaody` (TL-SG108E) and `waterseven` (TL-SG105E), the `poneglyph` VLAN 10+20 all-tagged trunk (with the native-VLAN rationale vs the other trunks), and the ordered **untagged-VLAN-1 gotcha** procedure (membership vs PVID, escape hatch, mgmt-VLAN-last, firmware/CVE + config backup). Cross-linked from [doc 02](docs/02-network.md), whose `sabaody` table now includes the `poneglyph` port.

## [1.4.5] — 2026-07-14 — Bootstrap template fix (review)

### Fixed
- Dropped `qemu-guest-agent` from the base **LXC** template in [runbook 04](docs/runbooks/04-proxmox-vlan-bootstrap.md) — it's a KVM-VM-only tool (filesystem freeze + guest exec via the QEMU channel) and is inert in containers, where Proxmox already has native host-level access.

## [1.4.4] — 2026-07-14 — Proxmox bootstrap runbook

### Added
- **`docs/runbooks/04-proxmox-vlan-bootstrap.md`** — first-time `poneglyph` build: Proxmox VE 9.2 install, a VLAN-aware `vmbr0` with the **host mgmt on VLAN 10 (`10.10.10.2`)** and **guest NICs tagged to VLAN 20**, the `tank` ZFS mirror (+ ARC cap and datasets), a **hardened unprivileged Docker-in-LXC base template**, first-guest clone, and the VLAN 20→Mgmt monitoring exception. Cross-linked from [doc 03](docs/03-virtualization.md) and [runbook 03](docs/runbooks/03-proxmox-bare-metal-restore.md).

## [1.4.3] — 2026-07-14 — Monitoring fixes (review)

### Fixed
- **Proxmox IP corrected `10.10.20.2` → `10.10.10.2`** across the Homepage config, `ct-proxy` Caddyfile, [doc 05](docs/05-core-services.md), and the [restore runbook](docs/runbooks/03-proxmox-bare-metal-restore.md) — the Proxmox *host* mgmt interface is on VLAN 10 per [doc 02](docs/02-network.md), while its guest containers are VLAN 20.
- **Homepage `resources` widget relabeled `poneglyph` → `ct-observe`** — it reflects the container/LXC view, not the hypervisor; documented using the Proxmox widget for real host stats.

### Added
- **VLAN 20 → Mgmt monitoring/reverse-proxy exception** ([doc 02](docs/02-network.md#monitoring-and-reverse-proxy-exception-vlan-20-to-mgmt)) — a narrow, two-source/three-port pass rule so `ct-observe` `siteMonitor` checks and the `proxmox.sunny.home` route can reach mgmt UIs without opening Servers→Mgmt generally. Cross-referenced from docs 05 and 09 and the Homepage config. Prevents the "everything on VLAN 10 shows offline" trap.

## [1.4.2] — 2026-07-14 — Homepage dashboard starter

### Added
- **`stacks/ct-observe/config/homepage/`** — starter Homepage config (`settings.yaml`, `services.yaml` grouped by stack incl. `ct-proxy`, `widgets.yaml`, `bookmarks.yaml`) referencing every Thousand Sunny service by its `*.sunny.home` name, with `siteMonitor` up/down checks and commented API-widget blocks keyed via `HOMEPAGE_VAR_*`.

### Changed
- `stacks/ct-observe/docker-compose.yml` — Homepage binds the committed `./config/homepage` and reads `.env` for `HOMEPAGE_VAR_*`; `.env.example` gains those placeholders.

## [1.4.1] — 2026-07-14 — OPNsense home-side runbook

### Added
- **`docs/runbooks/02-opnsense-wireguard.md`** — the home-side OPNsense config: the outbound WireGuard client interface (no default-gateway hijack, MTU note), the narrow tunnel→Jellyfin firewall rule (with a `ct-proxy` hand-off variant), the VLAN-60 sandbox rules with a **1-hour auto-off** (native Schedule + n8n firewall-API toggle with a cron fail-safe), and Servers-VLAN routing. Cross-linked from [doc 02](docs/02-network.md) and [doc 10](docs/10-external-access.md).

## [1.4.0] — 2026-07-14 — Hardening pass #2 (architecture review)

A second review flagged four architecture risks; all addressed.

### Changed
- **Least privilege — web/identity tier moved off the firewall.** `bartolomeo` now runs *only* routing, firewall, WireGuard, and DNS (AdGuard/Unbound). Caddy, Authelia, Vaultwarden, and CrowdSec parsing move to a new **unprivileged `ct-proxy` LXC** on `poneglyph` (VLAN 20) — a web-tier exploit no longer lands on the perimeter firewall. Rewrote [doc 05](docs/05-core-services.md); updated README (fleet + architecture diagram), [doc 01](docs/01-fleet.md), [doc 02](docs/02-network.md), [doc 03](docs/03-virtualization.md) (added `ct-proxy`, retightened the RAM budget → cap ARC ~4 GB, 64 GB comfort target), and [doc 11](docs/11-security.md) (web-tier threat row).
- **Sandbox internet auto-off.** The VLAN-60→WAN toggle now **auto-expires after 1 hour** (OPNsense schedule or an n8n flow with a cron fail-safe) so a forgotten toggle can't let detonated malware phone home. Updated [doc 02](docs/02-network.md), [doc 13](docs/13-impeldown-labs.md); added the workflow to [doc 12](docs/12-automation.md#4-sandbox-internet-auto-off).

### Added
- **Break-glass / offline credentials** procedure ([doc 11](docs/11-security.md#break-glass--offline-credentials)) — Proxmox/OPNsense root, ZFS + backup passphrases, and identity-tier bootstrap kept in an offline KeePassXC + paper-in-safe, independent of Vaultwarden/Authelia/DNS, to prevent chicken-and-egg lockout.
- **Boot-drive redundancy + RTO** ([doc 04](docs/04-storage.md)) — recommend mirroring `rpool` with a 2nd SSD; if single-disk, a documented ~1–3 h RTO and a new [bare-metal restore runbook](docs/runbooks/03-proxmox-bare-metal-restore.md). Added limitation #11 and a shopping row in [doc 15](docs/15-roadmap.md).
- **`stacks/ct-proxy/`** — runnable compose for the new tier (Caddy + Authelia + Vaultwarden + redis + CrowdSec) with sanitized Caddyfile and Authelia config.

## [1.3.0] — 2026-07-14 — Docker stacks

### Added
- **`stacks/` — runnable per-service Docker compose**, one folder per grouped LXC from [doc 03](docs/03-virtualization.md), each with a sanitized `.env.example`:
  - `ct-media` — Jellyfin, Seerr, Radarr, Sonarr, Prowlarr, Bazarr, SABnzbd, Decypharr (iGPU passthrough; AllDebrid via Decypharr FUSE mount).
  - `ct-photos` — Immich (server + machine-learning + valkey + VectorChord Postgres), iGPU-ready.
  - `ct-library` — Paperless-ngx (+redis/postgres/gotenberg/tika, with optional LiteLLM auto-tagging), Kavita, Navidrome.
  - `ct-cloud` — Nextcloud All-in-One mastercontainer.
  - `ct-automation` — n8n + ntfy.
  - `ct-observe` — Homepage, Uptime Kuma, Beszel(+agent), Grafana, Loki, Alloy — with working `loki-config.yml` and a Docker-log `config.alloy` pipeline (the substrate for the doc-09 LLM anomaly digest).
- Image tags pinned to the [version matrix](docs/16-versions.md); per-service `mem_limit`/`cpus` sized to each LXC's doc-03 budget.

### Changed
- README "Runnable configs" and [doc 03](docs/03-virtualization.md) now link `stacks/`.

## [1.2.0] — 2026-07-14 — Edge rebuild kit

### Added
- **`deploy/` — a runnable `puffingtom` rebuild kit** delivering on the v1.1 "keep a rebuild kit" promise:
  - `cloud-init/puffingtom.cloud-init.yaml` — provider-agnostic first-boot hardening (SSH key-only :2222, UFW, fail2ban, unattended-upgrades) + Docker.
  - `ansible/` — declarative Path A (WireGuard + Caddy): `site.yml`, inventory/vars examples, and `common` / `wireguard` / `caddy` roles with Jinja templates.
  - `wireguard/` + `caddy/` reference configs (VPS server + home-peer + Caddyfile).
  - `pangolin/` — Path B alternative (Pangolin server compose + home Newt connector) with the doc-10 memory-cap workaround.
  - `.env.example` — the shape of every secret (real values stay in Vaultwarden/SOPS).
- **`docs/runbooks/00-tunnel-rebuild.md`** — the ~15-minute failover runbook (key reuse, both paths, DNS repoint, verification, MTU gotcha).
- **`docs/runbooks/01-provider-notes.md`** — Oracle/RackNerd/Hetzner/Netcup/IONOS specifics, external-firewall gotchas, and the "insist on a dedicated IPv4" rule.

### Changed
- [doc 10](docs/10-external-access.md) tunnel-resilience section now links the concrete kit + runbooks.
- README gains a "Runnable configs" section; `.gitignore` extended to keep filled deploy values (`.env`, `inventory.ini`, `group_vars/edge.yml`, real `*.conf`) out of git.

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
