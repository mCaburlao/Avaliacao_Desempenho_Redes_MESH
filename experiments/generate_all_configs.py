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
standard g
ratecontrol ns3::ArfWifiManager
"""

APSTA_WIFI = """\
standard g
ratecontrol ns3::ArfWifiManager
channel delay ns3::ConstantSpeedPropagationDelayModel
channel add_loss ns3::LogDistancePropagationLossModel
"""


def routing_txt(proto):
    if proto.lower() == "aodv":
        return "proto aodv\n"
    return "proto olsr\n"


def apps_txt(n_stas, warmup_s, stagger_s=50, stagger_probe_s=15):
    """Gera apps.txt: n_stas fluxos UDP echo + 1 TCP para STA mais distante.

    ESTRATÉGIA: Start times escalonados com stagger para resolução de WiFi association
    e discovery de rotas completo antes da medição.
    
    Probe flows (começam bem antes do warmup): forcam route discovery do AODV
    para TODOS os STAs antes de iniciar medicoes. Cada probe STA inicia com
    stagger_probe_s segundos de diferença para evitar race conditions e permitir
    descoberta incremental de rotas.

    Medicoes começam exatamente em warmup_s, quando todas as rotas já devem estar
    estabelecidas (exceto em topologias muito desconectadas).

    Medicoes usam Interval=0.5s (2 pps): janela de 50s para 100 pacotes,
    reduzindo simDuration ~50% sem alterar o numero de amostras nem os ICs.
    """
    # Probes começam MUITO cedo e são escalonadas para dar tempo de discovery
    probe_start_base = warmup_s - (n_stas * stagger_probe_s + 10)
    probe_stop  = warmup_s - 1

    lines = []
    for i in range(1, n_stas + 1):
        probe_i_start = probe_start_base + (i - 1) * stagger_probe_s
        lines.append(f"defaults StartTime={probe_i_start}s StopTime={probe_stop}s")
        lines.append(f"probe{i}-cl    10.4.128.{i}    echo_client")
        lines.append(f"probe{i}-srv   10.1.1.1    echo_server")
        lines.append("")

    for i in range(1, n_stas + 1):
        lines.append(f"connect probe{i}-cl    probe{i}-srv")

    lines += [
        "defaults StopTime=",
    ]
    for i in range(1, n_stas + 1):
        t = warmup_s + (i - 1) * stagger_s
        lines.append(f"defaults StartTime={t}s")
        lines.append(f"echo{i}-cl    10.4.128.{i}    echo_client    Interval=0.5s MaxPackets=100")
        lines.append(f"echo{i}-srv   10.1.1.1    echo_server")
        lines.append("")

    # TCP inicia um intervalo apos o ultimo echo STA ter comecado
    tcp_start = warmup_s + n_stas * stagger_s
    lines += [
        f"defaults StartTime={tcp_start}s",
        f"file{n_stas}-srv   10.1.1.1    file_server",
        f"file{n_stas}-cl    10.4.128.{n_stas}    client",
        "",
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
        f"ns3::GridPositionAllocator"
        f" MinX=0 MinY=0 DeltaX={spacing} DeltaY={spacing} GridWidth={n_side}\n"
    )


def grid_sta_mobility(n_side=5, spacing=50, offset_x=5, offset_y=10):
    """Uma STA por no mesh, deslocada ligeiramente do AP."""
    lines = [
        "ns3::ListPositionAllocator",
    ]
    for row in range(n_side):
        for col in range(n_side):
            x = col * spacing + offset_x
            y = row * spacing + offset_y
            lines.append(f"  {x:4d}  {y:4d}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Random N nodes
# ---------------------------------------------------------------------------
def _gen_positions(n, area, seed, min_dist):
    """Gera n posicoes aleatorias reprodutiveis.

    O no 0 e o backhaul, fixado no centro da area para reduzir o vies de canto
    observado quando ele ficava em (0, 0).
    """
    rng = random.Random(seed)
    center = area / 2.0
    positions = [(center, center)]  # backhaul fixo no centro
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
        "ns3::ListPositionAllocator",
    ]
    for x, y in positions:
        lines.append(f"  {x:7.1f}  {y:7.1f}")
    return "\n".join(lines) + "\n"


def list_sta_mobility(positions, offset_x=5, offset_y=10):
    lines = [
        "ns3::ListPositionAllocator",
    ]
    for x, y in positions:
        lines.append(f"  {x + offset_x:7.1f}  {y + offset_y:7.1f}")
    return "\n".join(lines) + "\n"


def list_sta_mobility_sampled(positions, n_stas, offset_x=5, offset_y=10):
    """Seleciona n_stas posicoes uniformemente distribuidas da lista de nos mesh.
    Usado quando meshSize >> staSize para evitar overflow de /24 (max 254 STAs)."""
    n_mesh = len(positions)
    step   = max(1, n_mesh // n_stas)
    selected = [positions[i * step] for i in range(n_stas)]
    lines = [
        "ns3::ListPositionAllocator",
    ]
    for x, y in selected:
        lines.append(f"  {x + offset_x:7.1f}  {y + offset_y:7.1f}")
    return "\n".join(lines) + "\n"


def list_sta_mobility_random(positions, n_stas, seed, offset_x=5, offset_y=10):
    """Seleciona n_stas nos mesh aleatorios de forma reprodutivel."""
    rng = random.Random(seed)
    candidates = positions[1:] if len(positions) > 1 else positions
    selected = rng.sample(candidates, min(n_stas, len(candidates)))
    lines = [
        "ns3::ListPositionAllocator",
    ]
    for x, y in selected:
        lines.append(f"  {x + offset_x:7.1f}  {y + offset_y:7.1f}")
    return "\n".join(lines) + "\n"


def list_sta_mobility_balanced(positions, n_stas=5, offset_x=5, offset_y=10):
    """Estratégia MISTA: Seleciona STAs com distribuição balanceada para testar
    cobertura real em diferentes distâncias do backhaul.
    
    Para n_stas=5: 2 pertos + 2 longe + 1 médio
    Requer: mesh_positions[0] = backhaul na origem (0, 0)
    """
    # Calcular distância de cada nó mesh até o backhaul
    distances = []
    for i, (x, y) in enumerate(positions):
        dist = math.hypot(x - positions[0][0], y - positions[0][1])
        distances.append((dist, i))
    
    # Ordenar por distância
    distances.sort()
    
    selected_indices = []
    if n_stas == 5:
        # 2 mais próximos (distância pequena)
        selected_indices.extend([idx for _, idx in distances[:2]])
        # 2 mais distantes (periferias)
        selected_indices.extend([idx for _, idx in distances[-2:]])
        # 1 no meio (mediano)
        mid_idx = len(distances) // 2
        selected_indices.append(distances[mid_idx][1])
    else:
        # Fallback: seleção uniforme por quantis
        for i in range(n_stas):
            quantile = i / n_stas
            idx = min(int(len(distances) * quantile), len(distances) - 1)
            selected_indices.append(distances[idx][1])
    
    selected_positions = [positions[idx] for idx in selected_indices[:n_stas]]
    
    lines = [
        "ns3::ListPositionAllocator",
    ]
    for x, y in selected_positions:
        lines.append(f"  {x + offset_x:7.1f}  {y + offset_y:7.1f}")
    return "\n".join(lines) + "\n"


def _grid_positions(n_side, spacing=50):
    """Gera posicoes do grid n_side x n_side como lista Python (para amostragem de STAs)."""
    return [(col * spacing, row * spacing)
            for row in range(n_side)
            for col in range(n_side)]


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
    import shutil
    
    print("=" * 58)
    print("  Gerando configs de experimentos")
    print("=" * 58)
    
    # Remover configs antigas ANTES de regenerar
    print("\nLimpando configs antigas...")
    topologies = ["grid_25nodes", "random_50nodes", "random_75nodes", "random_100nodes", 
                  "random_150nodes", "random_200nodes", "random_300nodes", "random_500nodes",
                  "random_750nodes", "random_1000nodes"]
    for topo in topologies:
        topo_path = EXPERIMENTS / topo
        if topo_path.exists():
            shutil.rmtree(topo_path)
            print(f"  Removido: {topo}")
    print()

    FIXED_N_STAS = 5   # N de STAs fixo para todas as topologias — meshSize e a unica variavel
    # densidade alvo: 50/420^2 = 0.000284 nos/m^2  -> area = sqrt(N/0.000284)
    # Suite: 10 pontos cobrindo escala logaritmica 25..1000
    #   25, 50, 75, 100, 150, 200, 300, 500, 750, 1000
    TX_RANGE = 200    # alcance de transmissao para cobrir topologias grandes (era 115, insuficiente)

    # ---- 1. Grid 5x5 (25 nos) ----------------------------------------
    print("\n[ 1/10] Grid 5x5 — 25 nos, spacing 50m, duration 240s")
    WARMUP_25 = 120
    exp = EXPERIMENTS / "grid_25nodes"
    mm = grid_mesh_mobility(5, spacing=50)
    sm = list_sta_mobility_random(_grid_positions(5, spacing=50), FIXED_N_STAS, seed=25)
    ap = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_25)
    write_config(exp / "config_AODV_seed100", mm, sm, ap, routing_txt("aodv"))
    write_config(exp / "config_OLSR_seed101", mm, sm, ap, routing_txt("olsr"))

    # ---- 2. Random 50 nos (420x420m) ---------------------------------
    print("\n[ 2/10] Random 50 nos, area 420x420m, duration 500s")
    WARMUP_50 = 180
    exp = EXPERIMENTS / "random_50nodes"
    ap50 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_50)
    pos50 = _gen_positions(50, area=420, seed=200, min_dist=28)
    ok, n_ok = check_connectivity(pos50, tx_range=TX_RANGE)
    print(f"    seed=200 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/50)'}")
    sta50 = list_sta_mobility_random(pos50, FIXED_N_STAS, seed=50)
    for proto, seed in [("aodv", 200), ("olsr", 201)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos50, "seed=200-shared"),
                     sta50,
                     ap50, routing_txt(proto))

    # ---- 3. Random 75 nos (514x514m) ---------------------------------
    # A_75 = 75/0.000284 ~264k m^2 -> 514m
    print("\n[ 3/10] Random 75 nos, area 514x514m, duration 600s")
    WARMUP_75 = 210
    exp = EXPERIMENTS / "random_75nodes"
    ap75 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_75)
    pos75 = _gen_positions(75, area=514, seed=210, min_dist=28)
    ok, n_ok = check_connectivity(pos75, tx_range=TX_RANGE)
    print(f"    seed=210 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/75)'}")
    sta75 = list_sta_mobility_random(pos75, FIXED_N_STAS, seed=75)
    for proto, seed in [("aodv", 210), ("olsr", 211)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos75, "seed=210-shared"),
                     sta75,
                     ap75, routing_txt(proto))

    # ---- 4. Random 100 nos (600x600m) --------------------------------
    print("\n[ 4/10] Random 100 nos, area 600x600m, duration 650s")
    WARMUP_100 = 240
    exp = EXPERIMENTS / "random_100nodes"
    ap100 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_100)
    pos100 = _gen_positions(100, area=600, seed=300, min_dist=28)
    ok, n_ok = check_connectivity(pos100, tx_range=TX_RANGE)
    print(f"    seed=300 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/100)'}")
    sta100 = list_sta_mobility_random(pos100, FIXED_N_STAS, seed=100)
    for proto, seed in [("aodv", 300), ("olsr", 301)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos100, "seed=300-shared"),
                     sta100,
                     ap100, routing_txt(proto))

    # ---- 5. Random 150 nos (727x727m) --------------------------------
    # A_150 = 150/0.000284 ~528k m^2 -> 727m
    print("\n[ 5/10] Random 150 nos, area 727x727m, duration 700s")
    WARMUP_150 = 270
    exp = EXPERIMENTS / "random_150nodes"
    ap150 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_150)
    pos150 = _gen_positions(150, area=727, seed=310, min_dist=28)
    ok, n_ok = check_connectivity(pos150, tx_range=TX_RANGE)
    print(f"    seed=310 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/150)'}")
    sta150 = list_sta_mobility_random(pos150, FIXED_N_STAS, seed=150)
    for proto, seed in [("aodv", 310), ("olsr", 311)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos150, "seed=310-shared"),
                     sta150,
                     ap150, routing_txt(proto))

    # ---- 6. Random 200 nos (840x840m) --------------------------------
    print("\n[ 6/10] Random 200 nos, area 840x840m, duration 750s")
    WARMUP_200 = 300
    exp = EXPERIMENTS / "random_200nodes"
    ap200 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_200)
    pos200 = _gen_positions(200, area=840, seed=400, min_dist=28)
    ok, n_ok = check_connectivity(pos200, tx_range=TX_RANGE)
    print(f"    seed=400 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/200)'}")
    sta200 = list_sta_mobility_random(pos200, FIXED_N_STAS, seed=200)
    for proto, seed in [("aodv", 400), ("olsr", 401)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos200, "seed=400-shared"),
                     sta200,
                     ap200, routing_txt(proto))

    # ---- 7. Random 300 nos (1028x1028m) ------------------------------
    # A_300 = 300/0.000284 ~1.06M m^2 -> 1028m
    print("\n[ 7/10] Random 300 nos, area 1028x1028m, duration 750s")
    WARMUP_300 = 330
    exp = EXPERIMENTS / "random_300nodes"
    ap300 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_300)
    pos300 = _gen_positions(300, area=1028, seed=410, min_dist=28)
    ok, n_ok = check_connectivity(pos300, tx_range=TX_RANGE)
    print(f"    seed=410 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/300)'}")
    sta300 = list_sta_mobility_random(pos300, FIXED_N_STAS, seed=300)
    for proto, seed in [("aodv", 410), ("olsr", 411)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos300, "seed=410-shared"),
                     sta300,
                     ap300, routing_txt(proto))

    # ---- 8. Random 500 nos (1330x1330m) ------------------------------
    print("\n[ 8/10] Random 500 nos, area 1330x1330m, duration 800s")
    WARMUP_500 = 360
    exp = EXPERIMENTS / "random_500nodes"
    ap500 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_500)
    pos500 = _gen_positions(500, area=1330, seed=500, min_dist=28)
    ok, n_ok = check_connectivity(pos500, tx_range=TX_RANGE)
    print(f"    seed=500 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/500)'}")
    sta500 = list_sta_mobility_random(pos500, FIXED_N_STAS, seed=500)
    for proto, seed in [("aodv", 500), ("olsr", 501)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos500, "seed=500-shared"),
                     sta500,
                     ap500, routing_txt(proto))

    # ---- 9. Random 750 nos (1626x1626m) ------------------------------
    # A_750 = 750/0.000284 ~2.64M m^2 -> 1625m -> 1626m
    print("\n[ 9/10] Random 750 nos, area 1626x1626m, duration 850s")
    WARMUP_750 = 390
    exp = EXPERIMENTS / "random_750nodes"
    ap750 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_750)
    pos750 = _gen_positions(750, area=1626, seed=510, min_dist=28)
    ok, n_ok = check_connectivity(pos750, tx_range=TX_RANGE)
    print(f"    seed=510 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/750)'}")
    sta750 = list_sta_mobility_random(pos750, FIXED_N_STAS, seed=750)
    for proto, seed in [("aodv", 510), ("olsr", 511)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos750, "seed=510-shared"),
                     sta750,
                     ap750, routing_txt(proto))

    # ---- 10. Random 1000 nos (1880x1880m) ----------------------------
    print("\n[10/10] Random 1000 nos, area 1880x1880m, duration 900s")
    WARMUP_1000 = 420
    exp = EXPERIMENTS / "random_1000nodes"
    ap1000 = apps_txt(FIXED_N_STAS, warmup_s=WARMUP_1000)
    pos1000 = _gen_positions(1000, area=1880, seed=600, min_dist=28)
    ok, n_ok = check_connectivity(pos1000, tx_range=TX_RANGE)
    print(f"    seed=600 (compartilhado): {'CONECTADO' if ok else f'PARCIAL ({n_ok}/1000)'}")
    sta1000 = list_sta_mobility_random(pos1000, FIXED_N_STAS, seed=1000)
    for proto, seed in [("aodv", 600), ("olsr", 601)]:
        write_config(exp / f"config_{proto.upper()}_seed{seed}",
                     list_mesh_mobility(pos1000, "seed=600-shared"),
                     sta1000,
                     ap1000, routing_txt(proto))

    print("\nConcluido. Execute ./run_all_experiments.sh para rodar tudo.")
