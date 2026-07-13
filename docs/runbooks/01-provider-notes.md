# Runbook · VPS provider notes (edge fallback)

Provider-specific notes for standing up `puffingtom` (or its replacement). All prices/limits **July 2026** — re-verify at purchase. A pure tunnel node needs little: **1 vCPU, ~1 GB RAM, a dedicated IPv4**, and cloud-init or SSH.

| Provider | Entry spec | ~Price | Dedicated IPv4 | cloud-init | Notes |
|---|---|---|:--:|:--:|---|
| **Oracle Always Free** | Ampere A1, 2 OCPU/12 GB (halved Jun 2026) | ₹0 | ✅ | ✅ | Current primary. Idle-reclaim risk → this runbook exists. |
| **RackNerd** ⭐ | 1 vCPU / 1 GB / ~20 GB | **~$11–22/yr** | ✅ 1 incl. | ✅ | Cheapest reliable fallback; price-locked renewals; pick a nearby DC (e.g. an Asia/India-routed one). |
| **Hetzner** CX22 | 2 vCPU / 4 GB / 40 GB NVMe | ~€3.29/mo | ✅ 1 | ✅ | Best automation/API; EU + Singapore + US regions. |
| **Netcup** VPS 1000 G11 | 2 vCPU / 8 GB / 256 GB | ~€3.99/mo | ✅ | ✅ (SCP) | Great specs/€; EU (Nuremberg). Monthly billing only. |
| **IONOS** | 1 vCPU / 1 GB | ~$2/mo | ✅ | ✅ | Ultra-cheap monthly, enterprise SLA. |

## General repoint checklist (any provider)
1. Create VPS (Ubuntu 24.04) → note public IPv4.
2. Ensure inbound **80/tcp, 443/tcp, 51820/udp, 2222/tcp** are open (cloud-init sets UFW; also check the provider's *external* firewall/security-list — Oracle and Hetzner both have one that can silently block).
3. Paste cloud-init → run Ansible (Path A) or compose (Path B).
4. **DNS:** point the A records at the new IP. If using **DuckDNS**, update the token-based record; TTL low (300 s) makes cutovers fast.
5. Verify per [00-tunnel-rebuild.md](00-tunnel-rebuild.md).

## Provider gotchas
- **Oracle:** the Security List / NSG blocks everything by default — open the ports there *and* in UFW. Keep both `puffingtom` + `crowsnest` lightly active so the 7-day idle-reclaim never triggers.
- **Hetzner:** a separate Cloud Firewall may be attached — mirror the UFW rules there. Excellent snapshot support for a pre-cutover image.
- **RackNerd:** unmanaged KVM; confirm the DC/routing to India before buying (LA/Singapore nodes route well). One IPv4 included; extra IPs cost.
- **Netcup:** SCP panel + API (less slick than Hetzner). ECC RAM on root-server tiers if you want the tunnel box to double as something more.
- **All:** if the provider gives **IPv6 only** on the cheapest tier, that won't work as a family fallback (family ISPs may lack IPv6) — insist on a **dedicated IPv4**.

## Cost reality
The **$0 baseline stays $0** on Oracle. The fallback is insurance: **~₹1,000–1,800/yr** (RackNerd) buys a permanent, reclaim-proof edge you can cut over to in ~15 minutes. Document it now; you may never need it.
