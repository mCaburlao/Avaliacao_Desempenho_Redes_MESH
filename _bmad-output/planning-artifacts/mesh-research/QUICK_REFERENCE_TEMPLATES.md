# Quick Reference: Templates & Snippets para Artigo
## Copie e Cole Conforme Necessário

---

## 🏷️ TEMPLATES DE SEÇÕES

### [TEMPLATE 1] Parágrafo de Introdução: Contexto + Problema

```markdown
[CONTEXTO]
Redes mesh sem fio multi-hop (Multi-hop Wireless Mesh Networks) 
tornaram-se fundamentais em cenários de [APLICAÇÃO], onde dispositivos 
comunicam-se de forma autônoma sem infra-estrutura centralizada. Essas 
redes são especialmente relevantes em ambientes onde [RAZÃO PRÁTICA], 
como em [EXEMPLO 1], [EXEMPLO 2] e [EXEMPLO 3].

[PROBLEMA CRÍTICO]
Contudo, engenheiros enfrentam decisão fundamental: qual protocolo de 
roteamento escolher? Duas abordagens dominam: [ABORDAGEM 1] (ex: [PROTO 1]) 
que [CARACTERÍSTICA 1], e [ABORDAGEM 2] (ex: [PROTO 2]) que 
[CARACTERÍSTICA 2]. Mas falta investigação empírica rigorosa em escala 
contemporânea sobre como estes protocolos se comportam quando redes crescem 
de [NUM ATUAL] para [NUM FUTURO] nós.
```

**Exemplo Preenchido:**
```markdown
Redes mesh sem fio multi-hop tornaram-se fundamentais em cenários de 
Internet das Coisas, onde dispositivos comunicam-se de forma autônoma 
sem infra-estrutura centralizada. Essas redes são especialmente relevantes 
em ambientes onde a instalação de cabeamento tradicional é impraticável, 
como em monitoramento ambiental distribuído, iluminação inteligente urbana 
e sistemas de rastreamento de ativos.

Contudo, engenheiros enfrentam decisão fundamental: qual protocolo de 
roteamento escolher? Duas abordagens dominam: protocolo reativo 
(ex: AODV) que descobre rotas sob demanda, e protocolo proativo 
(ex: OLSR) que mantém tabelas continuamente atualizadas. Mas falta 
investigação empírica rigorosa em escala contemporânea sobre como estes 
protocolos se comportam quando redes crescem de 100 para 1500 nós.
```

---

### [TEMPLATE 2] Parágrafo: Por que esta pesquisa é novel?

```markdown
Nossa análise complementa este corpo de trabalho fornecendo:

\begin{enumerate}
  \item [PRIMEIRO PONTO ÚNICO] — Diferencial vs [PAPER X];
  \item [SEGUNDO PONTO ÚNICO] — Diferencial vs [PAPER Y];
  \item [TERCEIRO PONTO ÚNICO] — Contribuição não documentada;
  \item [QUARTO PONTO ÚNICO] — Escala ou contexto não explorado antes.
\end{enumerate}
```

**Exemplo (seu caso):**
```latex
Nossas análises complementam este corpo de trabalho fornecendo:

\begin{enumerate}
  \item Avaliação controlada em escala 100-1500 nós com simulação rigorosa;
  \item Comparação direta AODV vs OLSR em condições padronizadas;
  \item Identificação de pontos críticos de transição entre protocolos;
  \item Matriz de recomendação prática para engenheiros de smart cities.
\end{enumerate}
```

---

### [TEMPLATE 3] Seção Metodologia: Design Experimental

```latex
\subsection{Design Experimental}

Nosso design experimental segue abordagem fatorial estruturada:

\begin{itemize}
  \item \textbf{Fator 1 — [NOME]:} [VALOR 1] e [VALOR 2]
  \item \textbf{Fator 2 — [NOME]:} [VALOR 1], [VALOR 2]
  \item \textbf{Fator 3 — [NOME]:} [VALOR 1], [VALOR 2], ..., [VALOR N]
  \item \textbf{Fator 4 — [NOME]:} Mínimo N réplicas por configuração
\end{itemize}

Totalizamos: $[CÁLCULO] = [TOTAL]$ simulações.
```

**Para AODV vs OLSR:**
```latex
\subsection{Design Experimental}

Nosso design experimental segue abordagem fatorial estruturada:

\begin{itemize}
  \item \textbf{Fator 1 — Protocolo:} AODV (reativo) e OLSR (proativo)
  \item \textbf{Fator 2 — Topologia:} Grid (5×5), Random (Poisson)
  \item \textbf{Fator 3 — Escala:} 100, 300, 500, 800, 1000, 1500 nós
  \item \textbf{Fator 4 — Réplicas:} Mínimo 10 por configuração com sementes distintas
\end{itemize}

Totalizamos: $2 \times 2 \times 6 \times 10 = 240$ simulações.
```

---

### [TEMPLATE 4] Tabela de Comparação Protocolos

```latex
\begin{table}[ht]
\centering
\caption{Comparação [PROTO A] vs [PROTO B] — [ESCALA]}
\label{tab:[REFERENCE]}
\begin{tabular}{|l|r|r|r|}
\hline
\textbf{Métrica} & \textbf{[PROTO A]} & \textbf{[PROTO B]} & \textbf{Diferença} \\
\hline
[MÉTRICA 1] & [VALOR A] & [VALOR B] & [DELTA/PERCENT] \\
[MÉTRICA 2] & [VALOR A] & [VALOR B] & [DELTA/PERCENT] \\
[MÉTRICA 3] & [VALOR A] & [VALOR B] & [DELTA/PERCENT] \\
\hline
\end{tabular}
\end{table}
```

**Exemplo:**
```latex
\begin{table}[ht]
\centering
\caption{Resultados — 100 Nós (Seed Única, Topologia Grid)}
\label{tab:results-100-grid}
\begin{tabular}{|l|r|r|r|}
\hline
\textbf{Métrica} & \textbf{AODV} & \textbf{OLSR} & \textbf{Diferença} \\
\hline
PDR (\%) & $78.2$ & $69.9$ & $+11.8\%$ \\
Latência Média (ms) & $147$ & $138$ & $-6.1\%$ \\
Overhead (\%) & $8.3$ & $14.7$ & $-43.5\%$ \\
Convergência (s) & $2.1$ & $1.3$ & $+61.5\%$ \\
\hline
\end{tabular}
\end{table}
```

---

### [TEMPLATE 5] Inserir Figura

```latex
\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{[FILENAME].png}
\caption{[TÍTULO]. [DESCRIÇÃO BREVE DO QUE SE VÊ]. 
Pontos representam [O QUE CADA PONTO SIGNIFICA]. 
Bandas sombreadas indicam [IC 95%].}
\label{fig:[REFERENCE]}
\end{figure}
```

**Exemplo (seu caso):**
```latex
\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{fig1-pdr-vs-nodes.png}
\caption{Packet Delivery Ratio (PDR) em função do número de nós. 
Linha contínua e quadrados indicam AODV, traços à mão livre e círculos 
indicam OLSR. Bandas sombreadas representam intervalo de confiança 95\%.}
\label{fig:pdr-scaling}
\end{figure}
```

---

### [TEMPLATE 6] Parágrafo de Interpretação (após inserir figura)

```markdown
A Figura \ref{fig:[LABEL]} apresenta [O QUE A FIGURA MOSTRA]. 
Observamos que [FATO 1]. Isto sugere [MECANISMO 1]. 
Adicionalmente, [FATO 2] indicando [IMPLICAÇÃO]. 
Este resultado alinha-se com [LITERATURA/TEORIA] conforme 
reportado por \cite{[REFERENCE]}.
```

**Exemplo:**
```latex
A Figura \ref{fig:pdr-scaling} apresenta a taxa de entrega de pacotes 
em função da escala de rede. Observamos que PDR de AODV permanece acima 
de 75\% até 800 nós, enquanto OLSR degrada para aproximadamente 65\% 
na mesma escala. Isto sugere que o overhead de controle de OLSR (HALLO e TC 
floods) consome banda excessiva em redes maiores. Este resultado alinha-se 
com predições teóricas \cite{wireless_benyamina_2012}.
```

---

## 📚 FORMATO DE CITAÇÃO

### [TIPO 1] Citação Indireta (parafrase)

```latex
Roteamento em redes mesh é crítico para performance \cite{wireless_akyildiz_2005,wireless_sichitiu_2004}.
```

### [TIPO 2] Citação Direta ("segundo o autor")

```latex
Segundo \cite{wireless_akyildiz_2005}, ``redes mesh sem fio apresentam 
desafios únicos em escalabilidade''.
```

### [TIPO 3] Múltiplas Referências

```latex
Trabalhos recentes \cite{research_lee_2024, optimizing_ruete_2024} 
exploram aplicações de mesh em smart cities.
```

### [TIPO 4] Comparação de Trabalhos

```latex
Enquanto \cite{mesh_passos_2005} forneceu baseline histórico, 
\cite{performance_khalifeh_2018} propõem comparação entre tecnologias.
```

---

## 🧮 FÓRMULAS LATEX (Estatística)

### [FÓRMULA 1] Intervalo de Confiança 95%

```latex
IC_{95\%} = \bar{x} \pm 1.96 \times \frac{\sigma}{\sqrt{n}}
```

Onde: $\bar{x}$ = média, $\sigma$ = desvio padrão, $n$ = tamanho amostra

### [FÓRMULA 2] Teste Mann-Whitney U

```latex
p\text{-value} = P(U > U_{\text{crítico}}) \quad \text{(distribuição não-paramétrica)}
```

### [FÓRMULA 3] Effect Size (Cohen's d)

```latex
d = \frac{\mu_1 - \mu_2}{\sqrt{\frac{(\sigma_1^2 + \sigma_2^2)}{2}}}
```

Interpretação: $|d| < 0.2$ = pequeno, $0.2 \leq |d| < 0.5$ = médio, $|d| \geq 0.8$ = grande

---

## ⚠️ FRASES DE CUIDADO (Evite Exageros!)

### ❌ Evite:
```latex
AODV é definitivamente superior a OLSR.
Provamos que OLSR nunca funciona em escala.
Este é o primeiro trabalho a estudar roteamento em mesh.
```

### ✅ Use:
```latex
Resultados sugerem que AODV apresenta melhor PDR em escalas > 800 nós.
Nossas medições indicam que overhead de OLSR torna-se problema em redes grandes.
Este é o primeiro trabalho a comparar sistematicamente AODV vs OLSR 
em escala 100-1500 nós com simulação contemporânea.
```

---

## 📊 SNIPPETS DE DISCUSSÃO

### [SNIPPET 1] Interpretação Que Diverge de Expectativa

```latex
Diferente da expectativa inicial apontada por \cite{[REFERENCE]}, 
observamos que [SEU ACHADO]. Uma possível explicação é que 
\cite{[OUTRO REFERENCE]} reporta mecanismo similar em [CONTEXTO]. 
Isto sugere que [SUA INTERPRETAÇÃO].
```

### [SNIPPET 2] Limitação

```latex
Uma limitação importante é que nossas simulações não consideraram 
[FATOR NÃO TESTADO]. Trabalho futuro deverá investigar [EXTENSÃO].
```

### [SNIPPET 3] Alinhamento com Literatura

```latex
Nossos achados complementam investigações de \cite{[REFERENCE]} 
que encontrou [ACHADO DA LITERATURA] em contexto [CONTEXTO]. 
Aqui mostramos que este padrão se mantém em escala $[NUM]$ nós.
```

---

## 🔍 CHECKLIST ANTES DE SUBMETER

```latex
% Copie esta lista para um documento separado e marque conforme avança:

[ ] Todos os \cite{...} têm entrada em Mesh.bib?
[ ] Font Times 12pt em todo o documento?
[ ] Margens: 3.5/2.5/3.0 cm? (use régua ou mediador PDF)
[ ] Figuras 600 dpi?
[ ] Tabelas sem fundo colorido ou bordas excessivas?
[ ] Abreviações definidas na primeira ocorrência (IoT, PDR, etc)?
[ ] Nenhuma Seção vazia (TODO)?
[ ] Conclusão resume contribuição única?
[ ] Números de Tabelas/Figuras sequenciais (Fig 1, 2, 3)?
[ ] Todas Tabelas/Figuras referenciadas no texto?
[ ] Contagem de páginas OK (6-8 típico)?
```

---

## 💾 COMMANDS LaTeX ÚTEIS

```latex
% Comente um parágrafo temporariamente:
% \begin{comment}
% Seu texto aqui...
% \end{comment}

% Destaque um TODO para depois revisar:
\textbf{TODO:} Inserir Figura 2 aqui

% Scientific notation:
$10^{-6}$ para microsegundos

% Aproximadamente igual:
$\approx$ (use em comparações)

% Plus-minus (para IC):
$100 \pm 5$ para representar IC

% Reference figura/tabela:
Como mostrado em Figure \ref{fig:label} ...
Conforme Tabela \ref{tab:label} ...
```

---

## 🎯 Checklist Rápido Diário

**Cada vez que senta para escrever:**

- [ ] Abra artigo-LINHA4.tex
- [ ] Verifique qual seção é HOJE (vide ROADMAP_VISUAL_SIMULACAO_ARTIGO.md)
- [ ] Copie template apropriado desta guia (acima)
- [ ] Preencha com seu conteúdo específico
- [ ] Compile com `pdflatex` para checar sintaxe
- [ ] Salve backup (ou use Git: `git add -A && git commit -m "Sessão [DATA]"`)

---

**Quando estiver travado:**
- Leia GUIA_CONSTRUCAO_TRABALHO_ADR.md (inspiração)
- Releia LINHA_4_PRD_Escalabilidade.md (dados de referência)
- Veja papel recente do Mesh.bib e copie tom/estrutura
- Escreva em português natural primeiro, depois troca termos técnicos

**Tempo estimado por template:** 5-15 minutos (dependendo de aprofundamento)

Boa sorte! ✍️
