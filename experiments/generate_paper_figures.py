#!/usr/bin/env python3
"""
generate_paper_figures.py

Gera 3 figuras de publicação (600 dpi, PNG) a partir dos resultados de simulação.

Uso:
  python3 generate_paper_figures.py

Entradas esperadas:
  - experiments/results.csv (saída de analyze_all.py)

Saídas geradas:
  - fig1-pdr-vs-nodes.png         (PDR % vs # nós)
  - fig2-latency-vs-nodes.png     (Latência ms vs # nós)
  - fig3-overhead-vs-nodes.png    (Overhead % vs # nós)

Todas em 600 dpi, formato para impressão IEEE.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Configuração global: estilo paper
plt.style.use('seaborn-v0_8-darkgrid')
FIGSIZE = (8, 5)
DPI = 600  # Print quality
COLORS = {'AODV': '#1f77b4', 'OLSR': '#ff7f0e'}
MARKERS = {'AODV': 'o', 'OLSR': 's'}

BASE = Path("/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH")
RESULTS_FILE = BASE / "experiments/results.csv"
OUTPUT_DIR = BASE / "documento_latex/Template_SBC/template-latex"

# ============================================================================
# 1. FIGURA: PDR vs # de Nós
# ============================================================================

def plot_pdr_vs_nodes():
    """
    Packet Delivery Ratio (%) versus número de nós.
    Curva para cada protocolo com IC95% como banda sombreada.
    """
    # Ler dados
    if not RESULTS_FILE.exists():
        print(f"❌ Arquivo não encontrado: {RESULTS_FILE}")
        print("   Execute analyze_all.py primeiro.")
        return False

    df = pd.read_csv(RESULTS_FILE)
    
    # Agrupar por protocolo e número de nós
    grouped = df.groupby(['protocol', 'num_nodes'])['pdr_pct'].agg(['mean', 'std', 'count'])
    
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    
    for protocol in ['AODV', 'OLSR']:
        data = grouped.loc[protocol]
        nodes = data.index.values
        mean_pdr = data['mean'].values
        std_pdr = data['std'].values
        count = data['count'].values
        
        # Intervalo de confiança 95%
        sem = std_pdr / np.sqrt(count)
        ic95 = 1.96 * sem
        
        # Plot linha + IC como banda
        ax.plot(nodes, mean_pdr, 
                marker=MARKERS[protocol], 
                color=COLORS[protocol],
                linewidth=2,
                markersize=8,
                label=protocol)
        ax.fill_between(nodes, 
                        mean_pdr - ic95, 
                        mean_pdr + ic95,
                        alpha=0.2,
                        color=COLORS[protocol])
    
    ax.set_xlabel('Número de Nós', fontsize=12, fontweight='bold')
    ax.set_ylabel('PDR (%)', fontsize=12, fontweight='bold')
    ax.set_title('Packet Delivery Ratio vs Escala de Rede',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11, loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 105])
    
    fig.tight_layout()
    
    output_path = OUTPUT_DIR / "fig1-pdr-vs-nodes.png"
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Salvo: {output_path}")
    plt.close()
    return True

# ============================================================================
# 2. FIGURA: Latência vs # de Nós
# ============================================================================

def plot_latency_vs_nodes():
    """
    Latência fim-a-fim (ms) versus número de nós.
    Mostra latência média + jitter como banda de variação.
    """
    if not RESULTS_FILE.exists():
        print(f"❌ Arquivo não encontrado: {RESULTS_FILE}")
        return False

    df = pd.read_csv(RESULTS_FILE)
    
    # Agrupar
    grouped = df.groupby(['protocol', 'num_nodes']).agg({
        'latency_ms': ['mean', 'std'],
        'jitter_ms': 'mean',
        'num_nodes': 'count'
    })
    grouped.columns = ['latency_mean', 'latency_std', 'jitter_mean', 'count']
    
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    
    for protocol in ['AODV', 'OLSR']:
        data = grouped.loc[protocol]
        nodes = data.index.values
        lat_mean = data['latency_mean'].values
        lat_std = data['latency_std'].values
        count = data['count'].values
        
        sem = lat_std / np.sqrt(count)
        ic95 = 1.96 * sem
        
        ax.plot(nodes, lat_mean,
                marker=MARKERS[protocol],
                color=COLORS[protocol],
                linewidth=2,
                markersize=8,
                label=protocol)
        ax.fill_between(nodes,
                        lat_mean - ic95,
                        lat_mean + ic95,
                        alpha=0.2,
                        color=COLORS[protocol])
    
    ax.set_xlabel('Número de Nós', fontsize=12, fontweight='bold')
    ax.set_ylabel('Latência E2E (ms)', fontsize=12, fontweight='bold')
    ax.set_title('Latência Fim-a-Fim vs Escala de Rede',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11, loc='best')
    ax.grid(True, alpha=0.3)
    
    fig.tight_layout()
    
    output_path = OUTPUT_DIR / "fig2-latency-vs-nodes.png"
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Salvo: {output_path}")
    plt.close()
    return True

# ============================================================================
# 3. FIGURA: Overhead vs # de Nós
# ============================================================================

def plot_overhead_vs_nodes():
    """
    Overhead de roteamento (% de bandwidth) versus número de nós.
    Destaca ponto de crossover entre AODV linear e OLSR quadrático.
    """
    if not RESULTS_FILE.exists():
        print(f"❌ Arquivo não encontrado: {RESULTS_FILE}")
        return False

    df = pd.read_csv(RESULTS_FILE)
    
    grouped = df.groupby(['protocol', 'num_nodes'])['overhead_pct'].agg(['mean', 'std', 'count'])
    
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    
    for protocol in ['AODV', 'OLSR']:
        data = grouped.loc[protocol]
        nodes = data.index.values
        overhead_mean = data['mean'].values
        overhead_std = data['std'].values
        count = data['count'].values
        
        sem = overhead_std / np.sqrt(count)
        ic95 = 1.96 * sem
        
        ax.plot(nodes, overhead_mean,
                marker=MARKERS[protocol],
                color=COLORS[protocol],
                linewidth=2.5,
                markersize=8,
                label=f'{protocol} (observado)')
        ax.fill_between(nodes,
                        overhead_mean - ic95,
                        overhead_mean + ic95,
                        alpha=0.2,
                        color=COLORS[protocol])
    
    # Linha referência: overhead threshold típico (30%)
    ax.axhline(y=30, color='red', linestyle='--', linewidth=1.5, 
              label='Threshold Prático (30%)', alpha=0.7)
    
    ax.set_xlabel('Número de Nós', fontsize=12, fontweight='bold')
    ax.set_ylabel('Overhead de Roteamento (%)', fontsize=12, fontweight='bold')
    ax.set_title('Overhead de Roteamento vs Escala de Rede',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=10, loc='best')
    ax.grid(True, alpha=0.3)
    
    fig.tight_layout()
    
    output_path = OUTPUT_DIR / "fig3-overhead-vs-nodes.png"
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    print(f"✅ Salvo: {output_path}")
    plt.close()
    return True

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("📊 Gerando Figuras de Publicação (600 dpi, IEEE format)")
    print("=" * 70)
    
    success = True
    try:
        print("\n[1/3] Gerando PDR vs Nós...")
        if not plot_pdr_vs_nodes():
            success = False
        
        print("\n[2/3] Gerando Latência vs Nós...")
        if not plot_latency_vs_nodes():
            success = False
        
        print("\n[3/3] Gerando Overhead vs Nós...")
        if not plot_overhead_vs_nodes():
            success = False
        
    except Exception as e:
        print(f"\n❌ Erro durante geração: {e}")
        success = False
    
    print("\n" + "=" * 70)
    if success:
        print("✅ Todas as figuras geradas com sucesso!")
        print(f"\n📁 Localização: {OUTPUT_DIR}")
        print("\n📝 Próximos passos:")
        print("   1. Verifique a qualidade das imagens (abra em Visualizador)")
        print("   2. Insira no LaTeX com:")
        print("      \\begin{figure}[ht]")
        print("      \\centering")
        print("      \\includegraphics[width=0.8\\textwidth]{fig1-pdr-vs-nodes.png}")
        print("      \\caption{Packet Delivery Ratio...}")
        print("      \\label{fig:pdr}")
        print("      \\end{figure}")
    else:
        print("❌ Geração de figuras falhou. Verifique dados em results.csv")
    
    print("=" * 70)

