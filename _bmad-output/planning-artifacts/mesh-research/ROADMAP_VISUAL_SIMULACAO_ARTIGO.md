# Roadmap Visual: Da Simulação ao Artigo Publicável
## Integração Completa LINHA 4 (05/04 - 30/04)

**Objetivo:** Transformar dados de simulação em artigo científico publicável no formato SBC

**Status:** ✅ Planejamento 100% | ✅ Piloto 50% | 🟡 Análise 0% | 🟡 Escrita 20%

---

## 📊 Timeline Semana-a-Semana

```
SEMANA 1 (05-12 Abril)
├─ [HOJE]    Personalizar LaTeX + compilar PDF
├─ [TER]     Validar dados piloto vs flowdata.xml
├─ [QUA]     Refinar seções: Introdução + Metodologia
├─ [QUI]     Iniciar grid-25 e random-50 na máquina
├─ [SEX]     Revisar literatura (RFC 3561 AODV + RFC 3626 OLSR)
└─ [FIM]     ENTREGA: Draft Intro+Metodologia completo

SEMANA 2 (14-19 Abril)
├─ [SEG]     Completar rodadas de simulação (grid-25, random-50) = 60 total
├─ [TER]     Executar analyze_all.py → results.csv
├─ [QUA]     Gerar 3 figuras com generate_paper_figures.py
├─ [QUI]     Inserir figuras no LaTeX (artigo-LINHA4.tex)
├─ [SEX]     Expandir Resultados com interpretação + tabelas
└─ [FIM]     ENTREGA: Artigo com dados piloto + grid/random

SEMANA 3 (21-26 Abril)
├─ [SEG-TER] Rodar escalas maiores (800, 1000, 1500 nós) — ~30-40 hrs sim
├─ [QUA]     Re-executar analyze_all.py (2 variedades topologia)
├─ [QUI]     Gerar figuras FINAIS (300-1500 nós range)
├─ [SEX]     Completar Discussão + Conclusão
└─ [FIM]     ENTREGA: Artigo COMPLETO com todos dados

SEMANA 4 (28-30 Abril)
├─ [SEG]     Revisão final: Prosa, referências, formatação SBC
├─ [TER]     Validação estatística: IC 95%, effect sizes
├─ [QUA]     Preparar versão FINAL em PDF
└─ [JOV]     PRONTO PARA SUBMISSÃO OU APRESENTAÇÃO ✅
```

---

## 🔄 Fluxo de Dados: Simulação → Análise → Artigo

```
                        ┌─────────────────────┐
                        │   MeshSim (NS-3)    │
                        │ AODV + OLSR x Nós   │
                        └──────────┬──────────┘
                                   │
                          ✅ COMPLETO (piloto)
                                   ▼
                        ┌─────────────────────┐
                        │   flowdata.xml      │
                        │   trace-app-rx      │
                        │   METADATA.yaml     │
                        └──────────┬──────────┘
                                   │
                          🟡 Piloto (1 réplica)
                          ⏳ Escala (não iniciado)
                                   ▼
┌─────────────────────────────────────────────────────────────┐
│            analyze_all.py                                   │
│  (Processa XML → CSV com média, std, IC95%)                │
│  INPUT:  experiments/pilot_100_aodv_olsr/                  │
│  OUTPUT: experiments/results.csv                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
              🟡 Pendente (prox semana)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│        generate_paper_figures.py                            │
│  (CSV → PNG 600dpi publication-ready)                      │
│  OUTPUTS:                                                   │
│  ├─ fig1-pdr-vs-nodes.png                                  │
│  ├─ fig2-latency-vs-nodes.png                              │
│  └─ fig3-overhead-vs-nodes.png                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
              🟡 Pendente (prox semana)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│     artigo-LINHA4.tex (SBC Format)                          │
│  SEÇÕES:                                                    │
│  ├─ Título + Resumo ✅                                      │
│  ├─ Introdução ✅ (refinando)                               │
│  ├─ Trabalhos Relacionados ✅ (usando Mesh.bib)            │
│  ├─ Metodologia ✅ (refinando)                             │
│  ├─ Resultados 🟡 (inserir figuras semana 2)               │
│  ├─ Discussão 🟡 (expandir semana 2-3)                     │
│  └─ Conclusão 🟡 (finalizar semana 3)                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
              ✅ ESTRUTURA PRONTA (hoje)
              🟡 CONTEÚDO EM PROGRESSO
                       ▼
┌─────────────────────────────────────────────────────────────┐
│     artigo-LINHA4.pdf (Versão Final)                       │
│                                                             │
│  ✅ Compilado sem erros                                    │
│  ✅ Referências formatadas (IEEE)                          │
│  ✅ Figuras 600 dpi integradas                            │
│  ✅ Metodologia reproduzível documentada                   │
│  ✅ Estatísticas com IC 95%                                │
│                                                             │
│  PRONTO PARA:                                              │
│  ├─ Submissão em conferência IEEE                         │
│  ├─ Apresentação em ADR (seminário)                       │
│  └─ Discussão com advisor                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist Executável

### HOJE (05/04) — 30 minutos

- [ ] Abra artigo-LINHA4.tex em VS Code ou Overleaf
- [ ] **Linha 6:** Substitua `Aluno UFABC` → seu nome completo
- [ ] **Linha 6:** Substitua `Prof. Orientador` → nome do professor
- [ ] **Linha 9:** Substitua `aluno@ufabc.edu.br` → seu email
- [ ] Compile:
  ```bash
  cd documento_latex/Template_SBC/template-latex/
  pdflatex artigo-LINHA4.tex
  bibtex artigo-LINHA4
  pdflatex artigo-LINHA4.tex
  ```
- [ ] Abra `artigo-LINHA4.pdf` e verifique:
  - Seu nome no topo ✅
  - Título aparece correto ✅
  - Formatação SBC OK ✅

### AMANHÃ (06/04) — 1-2 horas

- [ ] Extraia dados piloto real:
  ```bash
  cd experiments/pilot_100_aodv_olsr/
  python3 analyze_pilot.py  # Gera métricas por fluxo
  ```
- [ ] Valide números na Tabela 1 do artigo:
  - AODV PDR 78.2% ← confira em `out_AODV/flowdata.xml`
  - OLSR PDR 69.9% ← confira em `out_OLSR/flowdata.xml`
- [ ] Se números não batem, ajuste script e re-execute

### SEMANA 1 (07-12/04) — 6-8 horas

**Paralelo A: Simulação em máquina**
- [ ] Inicie batch de rodadas:
  ```bash
  cd experiments/
  bash run_all_experiments.sh &  # Roda em background
  ```
- [ ] Monitore arquivo `results_progress.log`

**Paralelo B: Escrita**
- [ ] Abra artigo-LINHA4.tex
- [ ] Seção Introdução (Linhas ~85-100):
  - Review prosa (fluxo lógico)
  - Valide: Contexto → Gap → Objetivo
  - Adicione 1 frase sobre escala de smart cities (motivação)
- [ ] Seção Metodologia (Linhas ~115-160):
  - Review: Simulador, design, métricas, estatística
  - Valide: Todas as escolhas justificadas?
  - Adicione: "MeshSim repository: github.com/... [se publicado]"
- [ ] Salve primeira versão refinada

### SEMANA 2 (14-19/04) — 10-12 horas

**Pré-requisito:** Simulations concluídas (grid-25, random-50, 100 nós e acima)

- [ ] Execute `analyze_all.py`:
  ```bash
  python3 experiments/analyze_all.py > experiments/results.csv
  ```
  
- [ ] Gere figuras:
  ```bash
  python3 experiments/generate_paper_figures.py
  # Outputs: fig1-pdr-vs-nodes.png, fig2-latency-vs-nodes.png, fig3-overhead-vs-nodes.png
  ```

- [ ] Insira figuras no LaTeX:
  - Abra artigo-LINHA4.tex
  - Depois linha 195 (após dados piloto), adicione:
    ```latex
    \subsection{Análise Comparativa de Escalabilidade}
    
    \begin{figure}[ht]
    \centering
    \includegraphics[width=0.8\textwidth]{fig1-pdr-vs-nodes.png}
    \caption{Packet Delivery Ratio (PDR) em função do número de nós. 
    Pontos representam...}
    \label{fig:pdr-scaling}
    \end{figure}
    ```

- [ ] Expanda Seção Resultados:
  - Adicione tabela agregada 100-1500 nós
  - Interprete figuras (2-3 parágrafos)
  - Destaque pontos críticos de transição

- [ ] Refine Discussão:
  - Compare com literatura (RFC 3561, RFC 3626)
  - Explique mecanismos observados
  - Cité papers relevantes do Mesh.bib

### SEMANA 3 (21-26/04) — 12-14 horas

**Pré-requisito:** Todas escalas simuladas (100-1500 nós)

- [ ] Compile análise final com todas escalas
- [ ] Re-gere figuras (agora com dados 100-1500 nós)
- [ ] Atualize artigo:
  - Tabela final com 6 escalas × 2 protocolos
  - Figuras with full range 100-1500 nós
  - Identificar crossover point no texto

- [ ] Finalize Discussão:
  - Estatística rigorosa: effect sizes, test Mann-Whitney U
  - Limitações explícitas (sem mobilidade, topologia SB etc.)
  - Direções futuras claras

- [ ] Escreva Conclusão final:
  - Resumo em 1 parágrafo
  - Contribuição única (benchmark novo 100-1500)
  - Implicações práticas (matriz de recomendação)
  - Próximos passos

### SEMANA 4 (28-30/04) — 4-6 horas

**Revisão Final**

- [ ] Leitura crítica completa (voz alta):
  - Fluxo lógico correto?
  - Todos os números batem com figuras?
  - Sem repetição desnecessária?

- [ ] Validação SBC Format:
  - Margens corretas (3.5/2.5/3.0 cm)
  - Font Times 12pt ✅
  - Sem headers/footers ✅
  - Page count dentro dos limites

- [ ] Verificação de Referências:
  - Todo `\cite{...}` tem entrada em Mesh.bib
  - Bibtex compila sem warnings
  - Nenhuma referência duplicada

- [ ] Validação Estatística Final:
  - IC 95% em todas as tabelas
  - Effect sizes documentados
  - P-values para testes reportados

- [ ] Compile versão FINAL:
  ```bash
  pdflatex artigo-LINHA4.tex
  bibtex artigo-LINHA4
  pdflatex artigo-LINHA4.tex
  pdflatex artigo-LINHA4.tex  # Resolver cross-refs
  ```

- [ ] Salve como `artigo-LINHA4-FINAL.pdf`

---

## 📁 Arquivos-Chave

| Arquivo | Função | Status |
|:---|:---|:---|
| `artigo-LINHA4.tex` | Artigo principal | ✅ Criado |
| `Mesh.bib` | Referências | ✅ Pronto |
| `experiments/analyze_all.py` | Análise estatística | ✅ Pronto |
| `experiments/generate_paper_figures.py` | Gera figuras PNG | ✅ Criado |
| `experiments/results.csv` | Saída análise | 🟡 Gerado quando simulação terminar |
| `fig1-pdr-vs-nodes.png` | Figura PDR | 🟡 Gerado semana 2 |
| `fig2-latency-vs-nodes.png` | Figura Latência | 🟡 Gerado semana 2 |
| `fig3-overhead-vs-nodes.png` | Figura Overhead | 🟡 Gerado semana 2 |

---

## 🎯 Métricas de Qualidade (antes de submeter)

```
QUALIDADE DE CONTEÚDO:
✅ Introdução: <3 páginas, contexto+gap+objetivo claro
✅ Trabalhos Relacionados: 6+ papers, bem integrados
✅ Metodologia: Reproduzível? Sim, METADATA.yaml + seeds
✅ Resultados: Tabelas + 3 figuras 600 dpi
✅ Discussão: Comparação literatura, mecanismos, limitações
✅ Conclusão: Contribuição clara + implicações + futuros

QUALIDADE TÉCNICA:
✅ Statística: IC 95% em todas métricas
✅ Referências: 100% citations têm entrada BibTeX
✅ Figuras: 600 dpi, legendas descritivas, fonte legível
✅ Tabelas: Format SBC (sem tons de cor, sem bordas extras)

QUALIDADE FORMATAÇÃO SBC:
✅ Font: Times 12pt
✅ Margens: 3.5/2.5/3.0 cm
✅ Espaçamento: 6pt antes parágrafos
✅ Page count: 6-8 páginas (típico IEEE)
```

---

## 🚀 Próximas Ações Imediatas (Hoje)

1. **[5 min]** Personalize autor/email no LaTeX
2. **[5 min]** Compile PDF e verifique visualmente
3. **[10 min]** Leia Introdução em voz alta (check flow)
4. **[10 min]** Valide números piloto contra flowdata.xml

**Total: 30 minutos HOJE**

---

## 📞 Suporte

Quando você tiver dúvidas:

| Dúvida | Onde Encontrar Resposta |
|:---|:---|
| "Como estruturar Introdução?" | GUIA_CONSTRUCAO_TRABALHO_ADR.md |
| "Quais papers devo citar?" | GUIA_Literatura_Essencial.md |
| "Como validar dados piloto?" | ESTADO_SIMULACAO_E_PREPARACAO_ESCRITA.md |
| "Como refinar uma seção?" | GUIA_REFINAMENTO_ARTIGO_LATEX.md |
| "Que métricas coletar?" | LINHA_4_PRD_Escalabilidade.md |
| "Por que AODV vs OLSR divergem?" | LINHA_4_AODV_vs_OLSR_Detalhado.md |

---

**Status Final Esperado (30 de Abril):**

✅ Artigo in LaTeX SBC format  
✅ Todas 8 seções completas  
✅ 3 figuras de publicação (600 dpi)  
✅ Dados 100-1500 nós com IC 95%  
✅ Reprodutibilidade garantida via METADATA  
✅ Pronto para submissão ou apresentação  

**Vamos começar! 🚀**
