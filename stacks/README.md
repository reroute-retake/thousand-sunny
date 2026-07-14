# `stacks/` — grouped Docker-in-LXC compose files

One folder per **grouped LXC** from [`docs/03-virtualization.md`](../docs/03-virtualization.md). Each runs as its own Docker-in-LXC guest on `poneglyph`, so a bad update hits one stack, not the house.

> [!WARNING]
> **Sanitized templates.** Image tags are pinned to the [version matrix](../docs/16-versions.md) (July 2026). Every secret lives in each stack's `.env` (copy from `.env.example`; the real `.env` is git-ignored). No real passwords/keys/domains are committed.

## Conventions (apply to every stack)
- **Sizing:** each compose header states the LXC budget from doc 03; per-service `mem_limit` / `cpus` are set to fit it. Give the LXC that RAM/vCPU in Proxmox.
- **Paths:** `${APPDATA}` → NVMe (`fast/appdata` — configs & DBs); `${MEDIA}`/bulk → HDD ZFS mirror (`tank/…`). Set both in `.env`.
- **Identity:** `PUID`/`PGID`/`TZ` on LinuxServer images so files are owned correctly.
- **Naming, not ports:** services expose a port on the LXC IP; **Caddy on `bartolomeo`** reverse-proxies friendly names to them (see [doc 05](../docs/05-core-services.md)) — e.g. `jellyfin.sunny.home → 10.10.20.11:8096`.
- **iGPU:** stacks that transcode/do vision (`ct-media`, `ct-photos`) bind `/dev/dri`; the **LXC must pass the iGPU through** (doc 03). Heavy Immich ML can instead offload to `vegapunk` ([doc 08](../docs/08-ai-llm.md)).
- **Updates:** pinned tags + `docker compose pull && up -d` after a snapshot (doc 11). Don't chase `:latest`.

## Run a stack
```bash
cd stacks/ct-media
cp .env.example .env      # fill secrets/paths
docker compose up -d
docker compose logs -f
```

## Map
| Stack | LXC budget (doc 03) | Services |
|---|---|---|
| `ct-proxy` | 2 vCPU / 1.5 GB | Caddy · Authelia · Vaultwarden · CrowdSec · redis (web + identity tier — [doc 05](../docs/05-core-services.md)) |
| `ct-media` | 6 vCPU / 6 GB / iGPU | Jellyfin · Seerr · Radarr · Sonarr · Prowlarr · Bazarr · SABnzbd · Decypharr |
| `ct-photos` | 4 vCPU / 4 GB / iGPU | Immich (server · ML · redis · db) |
| `ct-library` | 3 vCPU / 3 GB | Paperless-ngx (+redis/db/gotenberg/tika) · Kavita · Navidrome |
| `ct-cloud` | 4 vCPU / 4 GB | Nextcloud AIO (manages Collabora/Talk itself) |
| `ct-automation` | 2 vCPU / 2 GB | n8n · ntfy |
| `ct-observe` | 3 vCPU / 3 GB | Homepage · Uptime Kuma · Beszel(+agent) · Grafana · Loki · Alloy |

> `ct-git` (Forgejo) runs as a **native LXC**, not Docker — so it isn't here (see doc 03).
