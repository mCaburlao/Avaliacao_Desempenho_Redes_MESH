#!/usr/bin/env python3
"""
generate_paper_figures.py

Gera 7 figuras de publicação (600 dpi, PNG) a partir dos resultados de simulação.
Todas as figuras incluem Intervalos de Confiança 95% e seguem padrões SBC/IEEE.

Uso:
  python3 generate_paper_figures.py

Entradas esperadas:
  - experiments_copia/results.csv (saída de analyze_all.py)

Saídas geradas (formato: fig<N>-<metrica>-vs-nodes.png em 600 dpi):
  1. fig1-pdr-vs-nodes.png              (Packet Delivery Ratio %)
  2. fig2-latency-vs-nodes.png          (Latência média E2E ms)
  3. fig3-jitter-vs-nodes.png           (Jitter médio ms)
  4. fig4-packet-loss-vs-nodes.png      (Taxa de Perda %)
  5. fig5-max-latency-vs-nodes.png      (Latência máxima ms - pior caso)
  6. fig6-throughput-vs-nodes.png       (Throughput kbps)
  7. fig7-avg-hops-vs-nodes.png         (Hops médios por pacote)

Todas em 600 dpi, IC95% como bandas sombreadas, padrão publication-ready.
Reprodutibilidade: seeds, num_nodes, e parâmetros de rede documentados em results.csv.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ============================================================================
# CONFIGURAÇÃO GLOBAL: Estilo Paper + Cores/Marcadores Consistentes
# ============================================================================
plt.style.use('seaborn-v0_8-darkgrid')
FIGSIZE = (8, 5)
DPI = 600  # Print quality para IEEE/SBC
COLORS = {'AODV': '#1f77b4', 'OLSR': '#ff7f0e'}  # Blue, Orange
MARKERS = {'AODV': 'o', 'OLSR': 's'}

# Caminhos (funciona em Windows e Linux)
BASE = Path(__file__).parent
RESULTS_FILE = BASE / "results.csv"
OUTPUT_DIR = BASE.parent / "documento_latex" / "Template_SBC" / "template-latex"

# ============================================================================
# DEFINIÇÃO DE MÉTRICAS E CONFIGURAÇÕES DE VISUALIZAÇÃO
# ============================================================================
METRICS_CONFIG = {
    'pdr': {
        'column': 'pdr',
        'title': 'Packet Delivery Ratio (PDR) vs Escala de Rede',
        'ylabel': 'PDR (%)',
        'filename': 'fig1-pdr-vs-nodes.png',
        'ylim': (0, 105),
        'decimals': 1,
    },
    'avg_delay_ms': {
        'column': 'avg_delay_ms',
        'title': 'Latência Média E2E vs Escala de Rede',
        'ylabel': 'Latência Média (ms)',
        'filename': 'fig2-latency-vs-nodes.png',
        'ylim': None,
        'decimals': 2,
    },
    'avg_jitter_ms': {
        'column': 'avg_jitter_ms',
        'title': 'Jitter Médio vs Escala de Rede',
        'ylabel': 'Jitter (ms)',
        'filename': 'fig3-jitter-vs-nodes.png',
        'ylim': None,
        'decimals': 2,
    },
    'loss': {
        'column': 'loss',
        'title': 'Taxa de Perda de Pacotes vs Escala de Rede',
        'ylabel': 'Taxa de Perda (%)',
        'filename': 'fig4-packet-loss-vs-nodes.png',
        'ylim': (0, None),
        'decimals': 1,
    },
    'max_delay_ms': {
        'column': 'max_delay_ms',
        'title': 'Latência Máxima (Pior Caso) vs Escala de Rede',
        'ylabel': 'Latência Máxima (ms)',
        'filename': 'fig5-max-latency-vs-nodes.png',
        'ylim': None,
        'decimals': 0,
    },
    'throughput_kbps': {
        'column': 'throughput_kbps',
        'title': 'Throughput Agregado vs Escala de Rede',
        'ylabel': 'Throughput (kbps)',
        'filename': 'fig6-throughput-vs-nodes.png',
        'ylim': None,
        'decimals': 1,
    },
    'avg_hops': {
        'column': 'avg_hops',
        'title': 'Número Médio de Hops vs Escala de Rede',
        'ylabel': 'Hops Médios',
        'filename': 'fig7-avg-hops-vs-nodes.png',
        'ylim': None,
        'decimals': 2,
    }
}

# ============================================================================
# FUNÇÕES DE VISUALIZAÇÃO GENÉRICAS COM IC95%
# ============================================================================

def plot_metric_vs_nodes(metric_key):
    """
    Plota qualquer métrica vs # de nós com IC95% como banda sombreada.
    
    Parâmetros:
        metric_key (str): chave em METRICS_CONFIG
    
    Returns:
        bool: True se sucesso, False c.c.
    
    Metodologia:
        - Agrupa por (protocol, num_nodes) 
        - Calcula média e IC95% do erro padrão = 1.96 * SEM
        - Desenha linha + banda sombreada para cada protocolo
        - Formato: 600 dpi, publication-ready
    """
    
    if not RESULTS_FILE.exists():
        print(f"❌ Arquivo não encontrado: {RESULTS_FILE}")
        print("   Execute analyze_all.py primeiro.")
        return False
    
    config = METRICS_CONFIG[metric_key]
    df = pd.read_csv(RESULTS_FILE)
    
    # Agrupar por protocolo e número de nós
    grouped = df.groupby(['protocol', 'num_nodes'])[config['column']].agg(
        ['mean', 'std', 'count']
    )
    
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    
    for protocol in ['AODV', 'OLSR']:
        if protocol not in grouped.index.get_level_values(0):
            print(f"⚠️  Protocolo {protocol} não encontrado nos dados")
            continue
        
        data = grouped.loc[protocol]
        nodes = np.sort(data.index.values)
        
        # Reordenar dados
        data = data.loc[nodes]
        mean_vals = data['mean'].values
        std_vals = data['std'].values
        count_vals = data['count'].values
        
        # Intervalo de confiança 95% (SEM-based)
        sem = std_vals / np.sqrt(count_vals)
        ic95 = 1.96 * sem
        
        # Plot: linha + banda IC
        ax.plot(nodes, mean_vals,
                marker=MARKERS[protocol],
                color=COLORS[protocol],
                linewidth=2,
                markersize=8,
                label=protocol,
                zorder=3)
        ax.fill_between(nodes,
                        mean_vals - ic95,
                        mean_vals + ic95,
                        alpha=0.2,
                        color=COLORS[protocol],
                        zorder=2)
    
    # Formatação
    ax.set_xlabel('Número de Nós', fontsize=12, fontweight='bold')
    ax.set_ylabel(config['ylabel'], fontsize=12, fontweight='bold')
    ax.set_title(config['title'], fontsize=13, fontweight='bold', pad=15)
    ax.legend(fontsize=11, loc='best', framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    if config['ylim']:
        ax.set_ylim(config['ylim'])
    
    fig.tight_layout()
    
    # Salvar
    output_path = OUTPUT_DIR / config['filename']
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    print(f"✅ Salvo: {config['filename']}")
    plt.close()
    
    return True

# ============================================================================
# MAIN: Gerar todas as 7 figuras
# ============================================================================

if __name__ == '__main__':
    print("=" * 80)
    print("📊 Gerando 7 Figuras de Publicação (600 DPI, IC95%, Padrão SBC/IEEE)")
    print("=" * 80)
    
    print(f"\n📁 Entrada:  {RESULTS_FILE}")
    print(f"📁 Saída:    {OUTPUT_DIR}")
    print()
    
    success = True
    total_figs = len(METRICS_CONFIG)
    
    try:
        for idx, (metric_key, config) in enumerate(METRICS_CONFIG.items(), 1):
            print(f"[{idx}/{total_figs}] Gerando {config['filename']}...", end=" ")
            if not plot_metric_vs_nodes(metric_key):
                success = False
                print("❌ FALHOU")
            else:
                print()
        
    except Exception as e:
        print(f"\n❌ Erro durante geração: {e}")
        import traceback
        traceback.print_exc()
        success = False
    
    print("\n" + "=" * 80)
    if success:
        print("✅ SUCESSO: Todas as 7 figuras geradas!")
        print()
        print("📋 Figuras Geradas:")
        for idx, (metric_key, config) in enumerate(METRICS_CONFIG.items(), 1):
            print(f"   {idx}. {config['filename']:40s} ({config['ylabel']})")
        
        print()
        print("📝 Próximos passos para inserção em LaTeX:")
        print("   1. Copie as figuras para o diretório do projeto LaTeX")
        print("   2. No seu .tex, use:")
        print()
        print("   \\begin{figure}[ht]")
        print("       \\centering")
        print("       \\includegraphics[width=0.8\\textwidth]{fig1-pdr-vs-nodes.png}")
        print("       \\caption{Packet Delivery Ratio em função da escala de rede.}")
        print("       \\label{fig:pdr}")
        print("   \\end{figure}")
        print()
        print("   [Repita para as demais figuras...]")
        print()
        print("🔬 Rigor Acadêmico:")
        print("   ✓ Todas as figuras incluem Intervalo de Confiança 95%")
        print("   ✓ Resolved em 600 DPI (publication-ready)")
        print("   ✓ Padrões IEEE/SBC: fontes sans-serif, legendas claras")
        print("   ✓ Reprodutibilidade: SEM-based IC da variância amostral")
        print()
    else:
        print("❌ FALHA: Verifique dados em results.csv e tente novamente.")
    
    print("=" * 80)

