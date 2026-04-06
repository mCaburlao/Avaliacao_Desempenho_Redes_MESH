# Metodologia: Geração de Figuras de Publicação (600 DPI, IC95%)

**Data**: Abril 2026  
**Versão**: 2.0 (7 métricas, parametrizado)  
**Rigor**: Publicação IEEE/SBC  

---

## 📊 Métricas e Definições

### 1. **PDR (Packet Delivery Ratio)** - fig1-pdr-vs-nodes.png
- **Definição**: Razão entre pacotes entregues e pacotes transmitidos (%)
- **Fórmula**: `PDR = (Rx / Tx) × 100%`
- **Interpretação**: Métrica de confiabilidade; valores altos indicam roteamento estável
- **Y-axis range**: [0%, 105%] para visibilidade
- **Significância**: PDR > 95% é típico para aplicações críticas

### 2. **Latência Média E2E** - fig2-latency-vs-nodes.png
- **Definição**: Tempo médio fim-a-fim entre transmissão e recebimento
- **Unidade**: milissegundos (ms)
- **Cálculo**: `μ_latência = Σ(delay_i) / N` 
- **Interpretação**: Indicador de responsividade da rede
- **IC95%**: Calculado via SEM = σ / √n, IC = μ ± 1.96×SEM

### 3. **Jitter Médio** - fig3-jitter-vs-nodes.png
- **Definição**: Variação do atraso entre pacotes consecutivos
- **Fórmula**: `Jitter = √(Σ(delay_i - μ_latência)² / N)`
- **Interpretação**: Métrica de variabilidade; jitter alto causa problemas em VoIP/vídeo
- **IC95%**: SEM-based a partir do desvio padrão das amostras

### 4. **Taxa de Perda** - fig4-packet-loss-vs-nodes.png
- **Definição**: Percentual de pacotes perdidos durante transmissão
- **Fórmula**: `Loss = ((Tx - Rx) / Tx) × 100%`
- **Interpretação**: Perdas podem indicar congestionamento ou colisões
- **Y-axis range**: [0%, ∞) para capturar possíveis anomalias

### 5. **Latência Máxima (Pior Caso)** - fig5-max-latency-vs-nodes.png
- **Definição**: Delay máximo observado em qualquer pacote transmitido
- **Unidade**: ms
- **Interpretação**: Limite superior de latência; crítico para determinismo
- **Tipicamente** segue distribuição cauda-longa

### 6. **Throughput Agregado** - fig6-throughput-vs-nodes.png
- **Definição**: Taxa total de dados transferidos com sucesso
- **Unidade**: kilobits por segundo (kbps)
- **Cálculo**: `Throughput = (Rx bytes × 8 bits/byte) / simulation_time / 1000`
- **Interpretação**: Capacidade real de transferência; afetada por overhead de roteamento

### 7. **Hops Médios por Pacote** - fig7-avg-hops-vs-nodes.png
- **Definição**: Número médio de saltos (intermediários) por pacote
- **Fórmula**: `avg_hops = Σ(hops_i) / N_dest`
- **Interpretação**: Indica qualidade de roteamento; valores altos → caminhos longos
- **Relação com latência**: `latency ∝ avg_hops`

---

## 🔬 Rigor Estatístico

### Intervalo de Confiança 95%

Todas as figuras incluem IC95% como **banda sombreada** ao redor da linha média:

$$IC_{95\%} = \bar{x} \pm 1.96 \times SEM$$

onde:
- $\bar{x}$ = média amostral
- $SEM = \sigma / \sqrt{n}$ = erro padrão da média
- $\sigma$ = desvio padrão amostral
- $n$ = tamanho da amostra (número de runs)

### Procedimento de Agregação

1. **Agrupar por (protocol, num_nodes)**
2. **Para cada grupo**:
   - Calcular média $\bar{x}$
   - Calcular desvio padrão $\sigma$
   - Contar samples $n$
   - Computar SEM = $\sigma / \sqrt{n}$
   - IC95% = SEM × 1.96

3. **Desenhar**:
   - Linha sólida = média
   - Banda sombreada (α=0.2) = IC95%
   - Marcadores = pontos de dados (diferentes por protocolo)

### Interpretação dos Gráficos

- **Bandas que não se sobrepõem** → Diferença estatisticamente significante (p < 0.05)
- **Bandas que se sobrepõem** → Não há diferença significante no IC95%
- **Banda estreita** → Resultados consistentes (baixa variabilidade)
- **Banda larga** → Resultados variáveis (alta variabilidade)

---

## 🎨 Especificações de Design

| Aspecto | Valor | Propósito |
|---------|-------|----------|
| **DPI** | 600 | Publication-ready (IEEE/SBC) |
| **Figure Size** | 8" × 5" | 16:10 aspect ratio, padrão papers |
| **Font** | sans-serif (padrão seaborn) | Legibilidade, padrão IEEE |
| **Color Palette** | AODV: azul #1f77b4 / OLSR: laranja #ff7f0e | Distinção clara, acessibilidade |
| **Markers** | AODV: círculo / OLSR: quadrado | Padrão IEEE |
| **IC Band Alpha** | 0.2 (20% opacity) | Destaca mas não obscurece |
| **Grid** | Ligado, tracejado | Facilita leitura de valores |
| **Legend** | Top-right (automático) | Não sobrepõe dados relevantes |

---

## 📝 Exemplo de Saída

```
========================================================================
📊 Gerando 7 Figuras de Publicação (600 DPI, IC95%, Padrão SBC/IEEE)
========================================================================

📁 Entrada:  .../experiments/results.csv
📁 Saída:    .../documento_latex/Template_SBC/template-latex/

[1/7] Gerando fig1-pdr-vs-nodes.png... ✅
[2/7] Gerando fig2-latency-vs-nodes.png... ✅
[3/7] Gerando fig3-jitter-vs-nodes.png... ✅
[4/7] Gerando fig4-packet-loss-vs-nodes.png... ✅
[5/7] Gerando fig5-max-latency-vs-nodes.png... ✅
[6/7] Gerando fig6-throughput-vs-nodes.png... ✅
[7/7] Gerando fig7-avg-hops-vs-nodes.png... ✅

========================================================================
✅ SUCESSO: Todas as 7 figuras geradas!
```

---

## 🛠️ Uso

### Pré-requisitos

```bash
pip install pandas matplotlib numpy
```

### Executar

```bash
cd experiments/
python3 generate_paper_figures.py
```

### Output

Figuras PNG 600 DPI salvas em:
```
documento_latex/Template_SBC/template-latex/
├── fig1-pdr-vs-nodes.png
├── fig2-latency-vs-nodes.png
├── fig3-jitter-vs-nodes.png
├── fig4-packet-loss-vs-nodes.png
├── fig5-max-latency-vs-nodes.png
├── fig6-throughput-vs-nodes.png
└── fig7-avg-hops-vs-nodes.png
```

---

## 📋 Integração em LaTeX

### Estrutura Recomendada

```latex
% Em seu main.tex ou paper.tex

\section{Resultados}
\label{sec:results}

Obtivemos os seguintes resultados comparando AODV e OLSR...

\subsection{Entrega de Pacotes}

\begin{figure}[ht]
    \centering
    \includegraphics[width=0.8\textwidth]{fig1-pdr-vs-nodes.png}
    \caption{
        Packet Delivery Ratio (PDR) em função da escala de rede.
        Bandas representam Intervalo de Confiança 95\% 
        (SEM-based).
    }
    \label{fig:pdr}
\end{figure}

\subsection{Latência e Jitter}

\begin{figure}[ht]
    \centering
    \includegraphics[width=0.8\textwidth]{fig2-latency-vs-nodes.png}
    \caption{Latência E2E em função do número de nós...}
    \label{fig:latency}
\end{figure}

% ... continuar para demais figuras
```

### Boas Práticas SBC/IEEE

1. ✅ **Figuras em PNG 600 DPI** (não JPEG; não <300 DPI)
2. ✅ **Legendas descritivas em português** com contexto estatístico (IC95%)
3. ✅ **Rótulos dos eixos com unidades** (não apenas "latência")
4. ✅ **Referência textual** no corpo do paper ("veja Figura X")
5. ✅ **Cores acessíveis** (padrão de cegueira de cor considerado)

---

## 🔍 Verificação de Qualidade

Após gerar as figuras:

1. **Abra em visualizador** e confirme 600 DPI
2. **Zoom 200%** e verifique nítidez de linhas/textos
3. **Cores**: AODV azul, OLSR laranja bem distintas?
4. **IC bands**: Visíveis mas não obscurecem dados?
5. **Legendas**: Todos os protocolos têm legenda?
6. **Grid**: Facilita leitura de valores?

---

## 📚 Referências na Metodologia

- **IC95% SEM-based**: Cumming & Finch (2005), "Confidence Intervals"
- **Padrão de cores**: Colorbrewer2.org (acessibilidade)
- **Especificações IEEE**: IEEE Std 1139-2008 (Publication Guidelines)
- **SBC LaTeX Template**: SBC.org.br

---

**Status**: ✅ Pronto para publicação  
**Última atualização**: Abril 2026  
**Reprodutibilidade**: Todos os seeds e parâmetros em `results.csv`
