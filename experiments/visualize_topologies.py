#!/usr/bin/env python3
"""
visualize_topologies.py — Gera plots XY das posições mesh + STAs
para diagnosticar posicionamento de STAs em grid-25 vs random-50.

Uso:
  python3 visualize_topologies.py
  
Saida:
  - topology_comparison.png (grid-25 vs random-50 lado ao lado)
  - grid_25_positions.png
  - random_50_positions.png
"""

import sys
import math
import random
from pathlib import Path

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.patches import Circle
except ImportError:
    print("ERRO: matplotlib não instalado")
    print("  Instale com: pip install matplotlib")
    sys.exit(1)

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
EXPERIMENTS = BASE / "experiments"

# ─────────────────────────────────────────────────────────────────
# Funcoes de geração de posições (copiadas de generate_all_configs.py)
# ─────────────────────────────────────────────────────────────────

def _gen_positions(n, area, seed, min_dist):
    """Gera n posicoes aleatorias reprodutiveis (no 0 = backhaul na origem)."""
    rng = random.Random(seed)
    positions = [(0.0, 0.0)]  # backhaul fixo em origem
    attempts = 0
    while len(positions) < n:
        x = rng.uniform(20, area - 20)
        y = rng.uniform(20, area - 20)
        if all(math.hypot(x - px, y - py) >= min_dist for px, py in positions):
            positions.append((x, y))
        attempts += 1
        if attempts > 200_000:
            raise RuntimeError(f"Impossível gerar {n} posições")
    return positions


def _grid_positions(n_side=5, spacing=50):
    """Gera posições grid 5x5."""
    return [(col * spacing, row * spacing)
            for row in range(n_side)
            for col in range(n_side)]


def list_sta_mobility_sampled(positions, n_stas, offset_x=5, offset_y=10):
    """Amostra uniforme de n_stas STAs a partir de posições mesh."""
    n_mesh = len(positions)
    step = max(1, n_mesh // n_stas)
    selected = [positions[i * step] for i in range(n_stas)]
    
    # Aplicar offset
    return [(x + offset_x, y + offset_y) for x, y in selected]


# ─────────────────────────────────────────────────────────────────
# Geração de plots
# ─────────────────────────────────────────────────────────────────

def plot_topology(title, mesh_pos, sta_pos, tx_range=1000, figsize=(10, 10)):
    """Cria plot único de topologia com mesh nodes e STAs."""
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot mesh nodes (azul, pequenos)
    mesh_x = [p[0] for p in mesh_pos]
    mesh_y = [p[1] for p in mesh_pos]
    ax.scatter(mesh_x, mesh_y, c='blue', s=50, alpha=0.6, label='Mesh nodes', zorder=2)
    
    # Plot backhaul (0,0) conspícuo
    ax.scatter([0], [0], c='darkblue', s=300, marker='*', 
               label='Backhaul (10.1.1.1)', zorder=3, edgecolors='black', linewidth=2)
    
    # Plot STAs (vermelho, maiores)
    sta_x = [p[0] for p in sta_pos]
    sta_y = [p[1] for p in sta_pos]
    ax.scatter(sta_x, sta_y, c='red', s=200, marker='D', alpha=0.8, 
               label='STAs (10.4.128.1-5)', zorder=4, edgecolors='darkred', linewidth=2)
    
    # Anotar STAs
    for i, (x, y) in enumerate(sta_pos, 1):
        ax.annotate(f'STA{i}', xy=(x, y), xytext=(5, 5), textcoords='offset points',
                   fontsize=9, fontweight='bold', color='darkred')
    
    # Desenhar círculos de tx_range em torno do backhaul
    circle = Circle((0, 0), tx_range, color='green', alpha=0.1, linestyle='--', 
                   linewidth=1, label=f'TX_RANGE={tx_range}m')
    ax.add_patch(circle)
    
    # Linhas de distância STA → Backhaul
    for i, (x, y) in enumerate(sta_pos, 1):
        dist = math.hypot(x - 0, y - 0)
        color = 'green' if dist <= tx_range else 'red'
        ax.plot([0, x], [0, y], color=color, alpha=0.2, linestyle=':', linewidth=1, zorder=1)
        
        # Anotar distância
        mid_x, mid_y = x/2, y/2
        ax.text(mid_x, mid_y, f'{dist:.0f}m', fontsize=8, alpha=0.7,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
    
    ax.set_xlabel('X (m)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y (m)', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    return fig, ax


def plot_comparison(grid_mesh, grid_sta, random_mesh, random_sta, tx_range=1000):
    """Cria plot lado-a-lado comparando grid-25 vs random-50."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    
    # ── Grid-25 (esquerda) ──
    grid_x = [p[0] for p in grid_mesh]
    grid_y = [p[1] for p in grid_mesh]
    ax1.scatter(grid_x, grid_y, c='blue', s=50, alpha=0.6, label='Mesh nodes')
    ax1.scatter([0], [0], c='darkblue', s=300, marker='*', label='Backhaul')
    
    grid_sta_x = [p[0] for p in grid_sta]
    grid_sta_y = [p[1] for p in grid_sta]
    ax1.scatter(grid_sta_x, grid_sta_y, c='red', s=200, marker='D', alpha=0.8,
               label='STAs', edgecolors='darkred', linewidth=2)
    
    for i, (x, y) in enumerate(grid_sta, 1):
        dist = math.hypot(x, y)
        ax1.annotate(f'STA{i}\n({dist:.0f}m)', xy=(x, y), xytext=(5, 5),
                    textcoords='offset points', fontsize=8, fontweight='bold', color='darkred')
    
    circle1 = Circle((0, 0), tx_range, color='green', alpha=0.1, linestyle='--', linewidth=1)
    ax1.add_patch(circle1)
    ax1.set_xlabel('X (m)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Y (m)', fontsize=11, fontweight='bold')
    ax1.set_title('Grid 5×5 (25 nodes)', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # ── Random-50 (direita) ──
    random_x = [p[0] for p in random_mesh]
    random_y = [p[1] for p in random_mesh]
    ax2.scatter(random_x, random_y, c='blue', s=50, alpha=0.4, label='Mesh nodes (random)')
    ax2.scatter([0], [0], c='darkblue', s=300, marker='*', label='Backhaul')
    
    random_sta_x = [p[0] for p in random_sta]
    random_sta_y = [p[1] for p in random_sta]
    ax2.scatter(random_sta_x, random_sta_y, c='red', s=200, marker='D', alpha=0.8,
               label='STAs', edgecolors='darkred', linewidth=2)
    
    for i, (x, y) in enumerate(random_sta, 1):
        dist = math.hypot(x, y)
        ax2.annotate(f'STA{i}\n({dist:.0f}m)', xy=(x, y), xytext=(5, 5),
                    textcoords='offset points', fontsize=8, fontweight='bold', color='darkred')
    
    circle2 = Circle((0, 0), tx_range, color='green', alpha=0.1, linestyle='--', linewidth=1)
    ax2.add_patch(circle2)
    ax2.set_xlabel('X (m)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Y (m)', fontsize=11, fontweight='bold')
    ax2.set_title('Random 50 nodes (seed=200)', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    # Ajustar limites para mostrar tudo
    max_range = 420  # área random-50
    ax2.set_xlim(-50, max_range + 50)
    ax2.set_ylim(-50, max_range + 50)
    
    plt.tight_layout()
    return fig


def main():
    print("\n📊 Gerando visualização de posições de topologias...")
    print("=" * 60)
    
    # ── Dados Grid-25 ──
    print("\n[1/3] Grid 5×5 (25 nodes)...")
    grid_mesh = _grid_positions(5, spacing=50)
    grid_sta = list_sta_mobility_sampled(grid_mesh, n_stas=5)
    
    print(f"  Mesh nodes: {len(grid_mesh)}")
    print(f"  STAs amostradas: {len(grid_sta)}")
    print(f"  Posições STAs (X, Y, dist ao backhaul):")
    for i, (x, y) in enumerate(grid_sta, 1):
        dist = math.hypot(x, y)
        print(f"    STA{i}: ({x:.1f}, {y:.1f}) → dist={dist:.1f}m")
    
    # ── Dados Random-50 ──
    print("\n[2/3] Random 50 nodes (seed=200)...")
    random_mesh = _gen_positions(50, area=420, seed=200, min_dist=28)
    random_sta = list_sta_mobility_sampled(random_mesh, n_stas=5)
    
    print(f"  Mesh nodes: {len(random_mesh)}")
    print(f"  STAs amostradas (step={len(random_mesh)//5}): {len(random_sta)}")
    print(f"  Posições STAs (X, Y, dist ao backhaul):")
    for i, (x, y) in enumerate(random_sta, 1):
        dist = math.hypot(x, y)
        print(f"    STA{i}: ({x:.1f}, {y:.1f}) → dist={dist:.1f}m")
    
    # ── Estatísticas de comparação ──
    print("\n[3/3] Comparação de distribuições...")
    grid_dists = [math.hypot(x, y) for x, y in grid_sta]
    random_dists = [math.hypot(x, y) for x, y in random_sta]
    
    print(f"\nDistâncias STAs → Backhaul:")
    print(f"  Grid-25:   min={min(grid_dists):.1f}m  max={max(grid_dists):.1f}m  avg={sum(grid_dists)/len(grid_dists):.1f}m")
    print(f"  Random-50: min={min(random_dists):.1f}m  max={max(random_dists):.1f}m  avg={sum(random_dists)/len(random_dists):.1f}m")
    
    tx_range = 1000
    grid_reachable = sum(1 for d in grid_dists if d <= tx_range)
    random_reachable = sum(1 for d in random_dists if d <= tx_range)
    
    print(f"\nSTAs reachable com TX_RANGE={tx_range}m:")
    print(f"  Grid-25:   {grid_reachable}/5 STAs")
    print(f"  Random-50: {random_reachable}/5 STAs")
    
    # ── Geração de plots ──
    print("\n📈 Gerando plots...")
    
    # Plot individual grid-25
    fig1, _ = plot_topology("Grid 5×5 (25 nodes)", grid_mesh, grid_sta, tx_range=tx_range, figsize=(10, 10))
    fig1.savefig(EXPERIMENTS / "grid_25_positions.png", dpi=150, bbox_inches='tight')
    print("   ✓ grid_25_positions.png")
    
    # Plot individual random-50
    fig2, _ = plot_topology("Random 50 nodes (seed=200)", random_mesh, random_sta, tx_range=tx_range, figsize=(10, 10))
    fig2.savefig(EXPERIMENTS / "random_50_positions.png", dpi=150, bbox_inches='tight')
    print("   ✓ random_50_positions.png")
    
    # Plot comparação lado-a-lado
    fig3 = plot_comparison(grid_mesh, grid_sta, random_mesh, random_sta, tx_range=tx_range)
    fig3.savefig(EXPERIMENTS / "topology_comparison.png", dpi=150, bbox_inches='tight')
    print("   ✓ topology_comparison.png")
    
    print("\n" + "=" * 60)
    print("✅ Visualizações geradas!")
    print(f"   Abra em: {EXPERIMENTS}/topology_comparison.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
