# 07 · Productivity — Cloud, Documents, Git, Notes

| Service | Version (Jul 2026) | Role | Docs |
|---|---|---|---|
| **Nextcloud** (AIO) | Hub 26 / server 34.0.1 | Files, calendar, contacts, office, sharing | [nextcloud.com/aio](https://github.com/nextcloud/all-in-one) |
| **Paperless-ngx** | 2.20.15 *(3.0 in RC)* | Document scanning, OCR, full-text, tagging | [docs.paperless-ngx.com](https://docs.paperless-ngx.com/) |
| **Forgejo** | 15.0.3 (LTS) | Self-hosted Git forge | [forgejo.org/docs](https://forgejo.org/docs/latest/) |

## Nextcloud — use **AIO**
Nextcloud GmbH's **All-in-One** is the officially maintained, single-container turnkey path (integrated backups, TLS, updates, Collabora office, Talk). Manual installs cost meaningfully more ongoing effort for the same result. Nextcloud becomes the **calendar/CalDAV source** for family reminders and the **availability backend** for the lakeside booking site ([12](12-automation.md), [14](14-sites-social.md)).

## Paperless-ngx — the family's paper shredder-of-record
Scan/drop every bill, warranty, school form, and government doc → OCR → full-text search → auto-tag. In July 2026 it gains real **local-LLM** superpowers (auto title/tag/correspondent, better OCR) — wired to your own GPU, no cloud. Details in **[08 · AI](08-ai-llm.md#paperless-ngx-ai)**.

## Git — **Forgejo over Gitea**
Both are excellent Gitea-lineage forges. **Forgejo** is the pick for a new setup in 2026: its **LTS** releases (v15.0 supported into mid-2027) give a longer, more predictable upgrade cadence, and it's the community-governed fork. Hosts the family's code, dotfiles, this very homelab repo, and the **published-notes source** ([14](14-sites-social.md)). Add **Forgejo Actions** later for CI (e.g. auto-build the notes site or the travel site).

## Obsidian — the honest recommendation for a *mixed-skill family*

Today: each person keeps separate vaults synced to individual GitHub repos. Here's the real landscape and the honest call.

| Tool | Ver (Jul 2026) | Keeps `.md` files? | Best for |
|---|---|---|---|
| **Obsidian Self-hosted LiveSync** (CouchDB) | 0.25.6x | ✅ | One person's live multi-device sync w/ conflict handling + E2E |
| **Syncthing** | 2.1.1 | ✅ | Zero-server P2P folder sync for non-technical members |
| **Git** (status quo) | — | ✅ | Technical users who want real version history |
| TriliumNext | 0.103.0 | ❌ (own DB) | A power knowledge base — but a *migration*, not a sync layer |
| SilverBullet | 2.8.0 | ✅ | An always-on, server-rendered markdown web vault |
| Logseq / AFFiNE / AnyType / Notesnook | mixed | mixed | Alternatives if leaving Obsidian; most drop the flat-`.md` model |

> [!TIP]
> **Don't centralize everyone onto CouchDB.** LiveSync is superb for *one person with 3+ devices*, but it adds a server to patch, back up, and debug (and 0.25.x has had sync-breaking regressions) — a bad ask for non-technical family. **Recommended hybrid:**
> - **Technical users (you, older kids):** keep **Git** — real history, they already have the habit.
> - **Everyone else:** **Syncthing** replicates their vault's `.md` files verbatim across their devices, no server, no lock-in (conflicts become recoverable `.sync-conflict` copies).
> - **One person who genuinely wants live sync:** run **LiveSync + CouchDB** just for them.
> - Store all vaults under Nextcloud or a `tank/vaults` share so they're swept into [backups](04-storage.md) regardless of sync method.

This keeps **Obsidian markdown as the source of truth** for everyone — which is what makes the [public notes site (Quartz)](14-sites-social.md) trivial to build.

Next: **[08 · AI & Local LLMs →](08-ai-llm.md)**
