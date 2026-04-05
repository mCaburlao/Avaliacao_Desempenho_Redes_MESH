# Capability 4: Analyze Results

## What You're Achieving

Transformar dados brutos em insights estatísticos publicáveis. Você vai:

- **Process raw data** — Ler CSVs, validar, calcular agregados
- **Calculate statistics** — Média, desvio padrão, intervalo de confiança (95%)
- **Generate visualizations** — Gráficos de qualidade publicável (PDF vetorial)
- **Produce interpretation** — O que os dados dizem? Protocolo A é melhor? Em que contexto?

Output é **interpretado** — dados + gráficos + conclusões. Pronto para artigo.

## Your Workflow

1. **I scan your experiment outputs** — Quantos scenarios? Qual formato?
2. **We define analysis strategy** — Quais métricas visualizar? Comparação por quê?
3. **I generate Python scripts** — Pandas, matplotlib, scipy para análise
4. **You run locally** — Scripts rodam em seu ambiente (tipo do Jupyter)
5. **I produce report** — Gráficos + tabelas + síntese

## Expected Output Structure

```
analysis/
├── processed_results.csv            # Agregado: média, σ, IC por scenario
├── statistical_summary.md           # Tabelas: Protocol A vs B por métrica
│
├── plots/
│   ├── latency_comparison.pdf       # Gráfico: Protocolo A vs B, latência
│   ├── latency_comparison.png       # (export PNG também)
│   ├── throughput_by_scenario.pdf   # Gráfico: Throughput vs n_nodes
│   ├── pdr_confidence_intervals.pdf # Com barras de intervalo
│   └── protocol_tradeoff.pdf        # Scatter: latência vs overhead
│
├── detailed_analysis.md
│   ├── Métrica 1: [achados, IC, significância]
│   ├── Métrica 2: [achados, IC, significância]
│   └── Conclusões: Qual protocolo vence? Em quais condições?
│
└── analysis_scripts/
    ├── process_data.py              # Ler CSVs, calcular IC
    ├── visualize.py                 # Matplotlib/Seaborn plots
    └── requirements.txt             # scipy, pandas, etc
```

## How I Help

**Skills Activation:** Uso `bmad-testarch-nfr` pra validar que análise cobre não-funcionais, `bmad-agent-tech-writer` pra estruturar relatório.

**Statistical Rigor (você não precisa saber Python, eu garanto):**

1. **Confidence Intervals** — 95% por padrão, justificado
2. **Significance Testing** — t-test ou Mann-Whitney U (depende distribuição)
3. **Multiple Comparisons** — Bonferroni correction se múltiplas métricas
4. **Effect Size** — Cohen's d além de p-value

**Visualization Best Practices:**

- Gráficos em **PDF vetorial** (escalável para papel)
- Legendas em **português** (seu domínio)
- Cores acessíveis (não só vermelho/verde)
- Barras de erro como **intervalos de confiança**, não ±1σ
- Fontes legíveis em tamanho de revista

**Example Analysis Output:**

```
## Latência (ms)

| Protocolo | Média | σ     | IC 95%        | N   |
|-----------|-------|-------|---------------|-----|
| AODV      | 12.3  | 2.1   | [11.8, 12.8]  | 100 |
| RPL       | 8.7   | 1.9   | [8.2, 9.2]    | 100 |
| t-test    | p=0.001 (significante, d=1.76)          |

**Achado:** RPL tem latência 29% menor (IC 95%).
Diferença é estatisticamente significante e praticamente relevante.
```

**Batch Processing:** Se você tem centenas de scenarios:
```python
# I generate this script for you:
for scenario_dir in experiments/scenario_*/
    process_scenario(scenario_dir)
    plot_comparison(scenario_dir)
```

## Important Notes

- **Your Data:** Você precisa fornecer CSVs com colunas bem-definidas. Vou validar formato.
- **Assumptions:** Vou testar normalidade; se não-normal, uso testes não-paramétricos.
- **Reproducibility:** Scripts Python são version-controlled; alguém pode re-rodar sua análise.
- **Automated:** Você não digita Pandas — eu gero scripts, você executa.

## Reproducibility Checklist

- [ ] Todos os scripts Python versionados (git)
- [ ] Requisitos Python pinned (versions exatas em requirements.txt)
- [ ] Gráficos gerados deterministically (sem variação random)
- [ ] Intervalos de confiança documentados (nível, método)
- [ ] Teste estatístico especificado (t-test? Mann-Whitney? Por quê?)
- [ ] Effect sizes reportados além de p-values
