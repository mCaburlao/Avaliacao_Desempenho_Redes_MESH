#!/usr/bin/env python3
"""
generate_all_configs.py — Gera configs para grid_25nodes e random_50nodes.
O pilot chain-9 (pilot_100_aodv_olsr/) ja existe e nao e tocado.

Topologias geradas:
  grid_25nodes/   — grid regular 5x5, 25 nos, 50m de espacamento
  random_50nodes/ — 50 nos em posicoes aleatorias reprodutiveis (seed fixo)

Uso:
  python3 generate_all_configs.py
"""

import math
import random
from pathlib import Path

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
EXPERIMENTS = BASE / "experiments"

# ---------------------------------------------------------------------------
# Conteudo fixo compartilhado entre todas as topologias
# ---------------------------------------------------------------------------
MESH_WIFI = """\
# Configuracao WiFi do backbone mesh (802.11g)
standard g
ratecontrol ns3::ArfWifiManager
"""

APSTA_WIFI = """\
# Configuracao WiFi AP <-> STA (802.11g)
standard g
ratecontrol ns3::ArfWifiManager

# Modelo de canal com atenuacao por distancia
channel delay ns3::ConstantSpeedPropagationDelayModel
channel add_loss ns3::LogDistancePropagationLossModel

# vim:ft=conf
"""


def routing_txt(proto):
    if proto.lower() == "aodv":
        return "# Roteamento reativo: descobre rotas sob demanda\nproto aodv\n"
    return "# Roteamento proativo: mantem rotas via atualizacoes periodicas\nproto olsr\n"


def apps_txt(n_stas, warmup_s, tcp_warmup_s):
    """Gera apps.txt: n_stas fluxos UDP echo + 1 TCP para STA mais distante."""
    lines = [
        f"# {n_stas} STAs — UDP echo + 1 TCP file transfer",
        f"# wiredSTA IPs: 10.1.4.1-{n_stas}  |  Backhaul: 10.1.1.1",
        "",
        f"defaults StartTime={warmup_s}s",
    ]
    for i in range(1, n_stas + 1):
        lines.append(f"echo{i}-cl    10.1.4.{i}    echo_client")
    lines.append("")
    for i in range(1, n_stas + 1):
        lines.append(f"echo{i}-srv   10.1.1.1    echo_server")
    lines += [
        "",
        "# TCP file transfer: backhaul -> STA mais distante (max hops)",
        f"defaults StartTime={tcp_warmup_s}s",
        f"file{n_stas}-srv   10.1.1.1    file_server",
        f"file{n_stas}-cl    10.1.4.{n_stas}    client",
        "",
        "# Conexoes",
    ]
    for i in range(1, n_stas + 1):
        lines.append(f"connect echo{i}-cl    echo{i}-srv")
    lines.append(f"connect file{n_stas}-srv   file{n_stas}-cl")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Grid 5x5
# ---------------------------------------------------------------------------
def grid_mesh_mobility(n_side=5, spacing=50):
    return (
        f"# Grid {n_side}x{n_side}: {n_side*n_side} nos mesh, {spacing}m de espacamento\n"
        f"# No 0 = backhaul (canto inferior esquerdo)\n"
        f"ns3::GridPositionAllocator"
        f" MinX=0 MinY=0 DeltaX={spacing} DeltaY={spacing} GridWidth={n_side}\n"
    )


def grid_sta_mobility(n_side=5, spacing=50, offset_x=5, offset_y=10):
    """Uma STA por no mesh, deslocada ligeiramente do AP."""
    lines = [
        f"# {n_side*n_side} STAs: uma por no mesh (deslocada {offset_x}m X, {offset_y}m Y)",
        "",
        "ns3::ListPositionAllocator",
    ]
    for row in range(n_side):
        for col in range(n_side):
            x = col * spacing + offset_x
            y = row * spacing + offset_y
            lines.append(f"  {x:4d}  {y:4d}")
    lines.append("\n# vim:ft=conf")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Random N nodes
# ---------------------------------------------------------------------------
def _gen_positions(n, area, seed, min_dist):
    """Gera n posicoes aleatorias reprodutiveis (no 0 = backhaul na origem)."""
    rng = random.Random(seed)
    positions = [(0.0, 0.0)]  # backhaul fixo
    attempts = 0
    while len(positions) < n:
        x = rng.uniform(20, area - 20)  # margem de 20m nas bordas
        y = rng.uniform(20, area - 20)
        if all(math.hypot(x - px, y - py) >= min_dist for px, py in positions):
            positions.append((x, y))
        attempts += 1
        if attempts > 200_000:
            raise RuntimeError(
                f"Impossivel gerar {n} posicoes com min_dist={min_dist}m em area={area}m. "
                "Reduza min_dist ou aumente a area."
            )
    return positions


def check_connectivity(positions, tx_range):
    """BFS para verificar conectividade. Retorna (is_connected, n_reachable)."""
    n = len(positions)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if math.hypot(positions[i][0] - positions[j][0],
                          positions[i][1] - positions[j][1]) <= tx_range:
                adj[i].append(j)
                adj[j].append(i)
    visited = {0}
    queue = [0]
    while queue:
        cur = queue.pop()
        for nb in adj[cur]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return len(visited) == n, len(visited)


def list_mesh_mobility(positions, label):
    lines = [
        f"# {len(positions)} nos mesh — posicoes lista ({label})",
        "",
        "ns3::ListPositionAllocator",
    ]
    for x, y in positions:
        lines.append(f"  {x:7.1f}  {y:7.1f}")
    lines.append("\n# vim:ft=conf")
    return "\n".join(lines) + "\n"


def list_sta_mobility(positions, offset_x=5, offset_y=10):
    lines = [
        f"# {len(positions)} STAs: uma por no mesh (deslocada {offset_x}m X, {offset_y}m Y)",
        "",
        "ns3::ListPositionAllocator",
    ]
    for x, y in positions:
        lines.append(f"  {x + offset_x:7.1f}  {y + offset_y:7.1f}")
    lines.append("\n# vim:ft=conf")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Utilitario: escrever um diretorio de config
# ---------------------------------------------------------------------------
def write_config(config_dir, mesh_mob, sta_mob, apps, routing):
    config_dir.mkdir(parents=True, exist_ok=True)
    (config_dir / "mesh_wifi.txt").write_text(MESH_WIFI)
    (config_dir / "apsta_wifi.txt").write_text(APSTA_WIFI)
    (config_dir / "mesh_mobility.txt").write_text(mesh_mob)
    (config_dir / "sta_mobility.txt").write_text(sta_mob)
    (config_dir / "apps.txt").write_text(apps)
    (config_dir / "routing.txt").write_text(routing)
    print(f"    OK  {config_dir.relative_to(BASE)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 58)
    print("  Gerando configs de experimentos")
    print("=" * 58)

    # ---- 1. Grid 5x5 (25 nos) ----------------------------------------
    print("\n[1/2] Grid 5x5 — 25 nos, spacing 50m, duration 500s")
    WARMUP_25 = 120    # OLSR converge ~70-80s em 25 nos (diam ~8 hops)
    TCP_25    = 125
    exp = EXPERIMENTS / "grid_25nodes"
    mm = grid_mesh_mobility(5, spacing=50)
    sm = grid_sta_mobility(5, spacing=50)
    ap = apps_txt(25, warmup_s=WARMUP_25, tcp_warmup_s=TCP_25)

    write_config(exp / "config_AODV_seed100", mm, sm, ap, routing_txt("aodv"))
    write_config(exp / "config_OLSR_seed101", mm, sm, ap, routing_txt("olsr"))

    # ---- 2. Random 50 nos --------------------------------------------
    print("\n[2/2] Random 50 nos, area 420x420m, duration 600s")
    WARMUP_50 = 180    # OLSR: mais nos, mais tempo de convergencia
    TCP_50    = 185
    TX_RANGE  = 115    # alcance de transmissao estimado (logdist 802.11g)
    exp = EXPERIMENTS / "random_50nodes"
    ap50 = apps_txt(50, warmup_s=WARMUP_50, tcp_warmup_s=TCP_50)

    for proto, seed in [("aodv", 200), ("olsr", 201)]:
        pos = _gen_positions(50, area=420, seed=seed, min_dist=28)
        ok, n_ok = check_connectivity(pos, tx_range=TX_RANGE)
        status = "CONECTADO" if ok else f"PARCIAL ({n_ok}/50)"
        print(f"    seed={seed}: {status}")
        if not ok:
            print(f"    AVISO: topologia nao conectada! Verifique TX_RANGE ({TX_RANGE}m).")

        mm_r = list_mesh_mobility(pos, f"seed={seed}")
        sm_r = list_sta_mobility(pos)
        label = proto.upper()
        write_config(
            exp / f"config_{label}_seed{seed}",
            mm_r, sm_r, ap50, routing_txt(proto)
        )

    print("\nConcluido. Execute ./run_all_experiments.sh para rodar tudo.")
