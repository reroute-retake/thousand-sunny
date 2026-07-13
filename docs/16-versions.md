# 16 · Version Matrix (July 2026)

The source of truth for what's pinned. All versions verified against official release channels as of **July 2026**. When you bump one, update it here (this is your changelog anchor — see [11 · patching](11-security.md)).

> [!NOTE]
> Pin these tags in compose/config; don't run `:latest`. Rows flagged ⚠️ ship **breaking major** changes — upgrade deliberately, read the release notes, snapshot first.

## Platform & network
| Component | Version | Docs |
|---|---|---|
| Proxmox VE | 9.2-1 | [pve.proxmox.com](https://pve.proxmox.com/wiki/Roadmap) |
| OPNsense | 26.1.10 (26.7 ~Jul 15) | [docs.opnsense.org](https://docs.opnsense.org/) |
| AdGuard Home | 0.107.75 | [wiki](https://github.com/AdguardTeam/AdGuardHome/wiki) |
| Unbound | current | [nlnetlabs](https://unbound.docs.nlnetlabs.nl/) |
| Caddy | 2.10.x | [caddyserver.com](https://caddyserver.com/docs/) |
| Authelia | 4.39.20 | [authelia.com](https://www.authelia.com/) |
| Vaultwarden | 1.36.0 | [wiki](https://github.com/dani-garcia/vaultwarden/wiki) |
| CrowdSec | current | [docs.crowdsec.net](https://docs.crowdsec.net/) |

## Media & library
| Component | Version | Docs |
|---|---|---|
| Jellyfin | 10.11.11 *(12.0 = RC/unstable)* | [jellyfin.org/docs](https://jellyfin.org/docs/) |
| Seerr | 3.3.0 *(Overseerr+Jellyseerr merge)* | [docs.seerr.dev](https://docs.seerr.dev/) |
| Radarr | 6.3.0 | [wiki.servarr.com](https://wiki.servarr.com/radarr) |
| Sonarr | 4.0.19 | [wiki.servarr.com](https://wiki.servarr.com/sonarr) |
| Prowlarr | 2.5.0 | [wiki.servarr.com](https://wiki.servarr.com/prowlarr) |
| Bazarr | 1.6.0 | [wiki.bazarr.media](https://wiki.bazarr.media/) |
| SABnzbd | 5.0.4 | [sabnzbd.org](https://sabnzbd.org/) |
| NZBGet | 26.2 | [nzbget.com](https://nzbget.com/) |
| Decypharr | 0.7.x | [github.com/sirrobot01/decypharr](https://github.com/sirrobot01/decypharr) |
| ⚠️ Immich | 3.0.2 *(3.0 = breaking vs 2.x)* | [immich.app/docs](https://immich.app/docs) |
| Kavita | 0.9.0.2 | [wiki.kavitareader.com](https://wiki.kavitareader.com/) |
| Navidrome | 0.63.2 | [navidrome.org](https://www.navidrome.org/docs/) |

## Productivity
| Component | Version | Docs |
|---|---|---|
| Nextcloud (AIO) | Hub 26 / server 34.0.1 | [github.com/nextcloud/all-in-one](https://github.com/nextcloud/all-in-one) |
| ⚠️ Paperless-ngx | 2.20.15 *(3.0 in RC)* | [docs.paperless-ngx.com](https://docs.paperless-ngx.com/) |
| Forgejo | 15.0.3 (LTS) | [forgejo.org/docs](https://forgejo.org/docs/latest/) |
| Obsidian LiveSync | 0.25.6x | [github.com/vrtmrz/obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) |
| Syncthing | 2.1.1 | [syncthing.net](https://syncthing.net/) |
| Quartz | v5 | [quartz.jzhao.xyz](https://quartz.jzhao.xyz/) |

## AI / LLM
| Component | Version | Docs |
|---|---|---|
| llama.cpp | rolling (b95xx) | [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) |
| Ollama | 0.30.7 / 0.31.2-rc | [docs.ollama.com](https://docs.ollama.com/) |
| vLLM | 0.24/0.25 | [docs.vllm.ai](https://docs.vllm.ai/) |
| LiteLLM | 1.83.8+ | [docs.litellm.ai](https://docs.litellm.ai/) |
| paperless-gpt | 0.26.1 | [github.com/icereed/paperless-gpt](https://github.com/icereed/paperless-gpt) |
| paperless-ai | 3.0.9 | [github.com/clusterzx/paperless-ai](https://github.com/clusterzx/paperless-ai) |
| **Models** | Gemma 4 (12B/26B-A4B QAT) · Qwen3 / Qwen3-Coder / Qwen3-VL / Qwen3-Embedding · GLM-4.7-Flash | see [08](08-ai-llm.md) |

## Observability & automation
| Component | Version | Docs |
|---|---|---|
| Homepage | 1.13.2 | [gethomepage.dev](https://gethomepage.dev/) |
| Uptime Kuma | 2.4.0 | [github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) |
| Gatus | 5.36.0 | [github.com/TwiN/gatus](https://github.com/TwiN/gatus) |
| Beszel | 0.18.7 | [beszel.dev](https://beszel.dev/) |
| Grafana | 13.1.0 | [grafana.com/docs](https://grafana.com/docs/) |
| Loki | 3.7.3 | [grafana.com/docs/loki](https://grafana.com/docs/loki/latest/) |
| Alloy | 1.17.1 | [grafana.com/docs/alloy](https://grafana.com/docs/alloy/latest/) |
| n8n | 1.117.x | [docs.n8n.io](https://docs.n8n.io/) |
| ntfy | 2.13.x | [docs.ntfy.sh](https://docs.ntfy.sh/) |

## External access & labs
| Component | Version | Docs |
|---|---|---|
| Tailscale | current (Personal, free 6 users) | [tailscale.com/kb](https://tailscale.com/kb/) |
| Pangolin | 1.20.0 | [pangolin.net](https://docs.fossorial.io/) |
| Newt | 1.13.x | [github.com/fosrl/newt](https://github.com/fosrl/newt) |
| WireGuard | tools 1.0.2026 | [wireguard.com](https://www.wireguard.com/) |
| Kali Linux | 2026.2 | [kali.org/docs](https://www.kali.org/docs/) |
| Batocera | 43.1 | [batocera.org](https://batocera.org/) |
| Postiz / Mixpost | v2 / v2 | [postiz](https://docs.postiz.com/) · [mixpost](https://mixpost.app/docs) |

---
*Landscape captured July 2026. Re-verify majors before upgrading; log every change here.*
