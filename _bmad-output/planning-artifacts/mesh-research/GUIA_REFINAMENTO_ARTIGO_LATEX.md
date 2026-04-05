# Guia de Refinamento do Artigo LaTeX
## Do Esboço Inicial à Versão Final

**Arquivo:** `documento_latex/Template_SBC/template-latex/artigo-LINHA4.tex`  
**Status:** ✅ Estrutura completa | 🟡 Conteúdo em desenvolvimento  
**Data:** 05 de Abril de 2026

---

## 📋 O Que Foi Criado

✅ **Estrutura SBC Completa:**
- [x] Título, Autores, Afiliação
- [x] Abstract (inglês) e Resumo (português)
- [x] Introdução (2 parágrafos contexto + gap + objetivo)
- [x] Trabalhos Relacionados (6 papers do Mesh.bib integrados)
- [x] Metodologia (simulador, design, métricas, estatística)
- [x] Resultados Preliminares (tabela piloto 100 nós)
- [x] Discussão (interpretação + limitações)
- [x] Conclusão + Próximos Passos
- [x] Referências BibTeX apontando para Mesh.bib

---

## 🎯 O Que Falta (Prioridade)

### Fase 1: HOJE — Personalizações (1-2 horas)

- [ ] **Linha 6:** Substitua `Aluno UFABC` por seu nome
- [ ] **Linha 6:** Substitua `Prof. Orientador` pelo nome do professor
- [ ] **Linha 9:** Atualize email `aluno@ufabc.edu.br` → seu email real

**Por quê:** Seu nome deve aparecer como autor no artigo final.

### Fase 2: SEMANA 1 — Validação de Conteúdo (4-6 horas)

#### ✏️ Seção: Introdução (Linhas ~85-100)

**Tarefa:** Revise os 3 parágrafos para clareza e precisão

**Parágrafo 1 (Contexto):**
- [x] Menciona smart cities ✅
- [x] Menciona mesh networks ✅
- [x] Menciona importância de roteamento ✅
- [ ] **TODO:** Adicione 1 frase sobre população global em smart cities (motivação de escala)

**Parágrafo 2 (Gap):**
- [x] Identifica AODV vs OLSR ✅
- [x] Menciona trade-offs ✅
- [ ] **TODO:** Alinhe linguagem com RFC 3561 (AODV) e RFC 3626 (OLSR)

**Parágrafo 3 (Objetivo):**
- [x] Pergunta clara ✅
- [ ] **TODO:** Adicione frase sobre "30-50% de otimização documentada esperada"

#### ✏️ Seção: Metodologia (Linhas ~115-160)

**Validar:**
- [ ] Versão MeshSim está correta (verifique em `ns-3-dev/VERSION`)
- [ ] Padrão WiFi 802.11g é correto (confirme com seu advisor)
- [ ] Durações de simulação (400s) fazem sentido

**Completar:**
- [ ] **Linha 138:** Adicione URL ou referência a MeshSim repository
- [ ] **Linha 158:** Adicione justificativa técnica: why 1000×1000 area?

#### 📊 Seção: Resultados Preliminares (Linhas ~170-190)

**STATUS CRÍTICO:** Dados piloto estão em `experiments/pilot_100_aodv_olsr/`

- [ ] Valide números na Tabela 1:
  - AODV PDR: 78.2% ← confirme em `out_AODV/flowdata.xml`
  - OLSR PDR: 69.9% ← confirme em `out_OLSR/flowdata.xml`
  
- [ ] **TODO:** Quando tiver GRID-25 + RANDOM-50:
  - Adicione Tabela 2: Grid-25 com AODV/OLSR
  - Adicione Tabela 3: Random-50 com AODV/OLSR

### Fase 3: SEMANA 2-3 — Integração de Dados Reais (Variável)

Assim que terminar as 60+ rodadas de simulação:

- [ ] **Gere gráficos** usando `analyze_all.py`:
  ```bash
  python3 analyze_all.py > results.csv
  # Gere figuras: PDR vs nós, Latência vs nós, Overhead vs nós
  ```

- [ ] **Crie 3 figuras PNG** (600 dpi):
  1. `fig1-pdr-vs-nodes.png` — Curvas AODV/OLSR com IC95%
  2. `fig2-latency-vs-nodes.png` — Latência média + jitter bands
  3. `fig3-overhead-vs-nodes.png` — Evidence de crossover

- [ ] **Insira figuras no LaTeX** (após linha 195):
  ```latex
  \subsection{Análise de Escalabilidade}
  
  \begin{figure}[ht]
  \centering
  \includegraphics[width=0.8\textwidth]{fig1-pdr-vs-nodes.png}
  \caption{Packet Delivery Ratio versus número de nós. Pontos representam...}
  \label{fig:pdr-scaling}
  \end{figure}
  ```

- [ ] **Atualize Resultados** (Seção 5):
  - Remova "Status: Dados piloto coletados..." (linha 192)
  - Adicione tabela agregada 100-1500 nós
  - Adicione interpretação de pontos críticos

- [ ] **Atualize Discussão** (Seção 6):
  - Compare com literatura (RFC specs, papers recentes)
  - Explique mecanismos de divergência observados
  - Mova limitações para subsection próprio

### Fase 4: ANTES DE SUBMETER — Checklist Final (2 horas)

- [ ] **Gramática e Prosa:**
  - [ ] Rode spell-check português (VS Code extension PT-BR)
  - [ ] Verifique pontuação em "et al." nas referências
  - [ ] Todas as abreviaturas definidas na primeira ocorrência (IoT, PDR, AODV, etc.)

- [ ] **Formato SBC:**
  - [ ] Margens corretas: 3.5cm topo, 2.5cm bottom, 3.0cm laterais ✅
  - [ ] Font Times 12pt ✅
  - [ ] Sem headers/footers ✅
  - [ ] Títulos seções em negrito 13pt ✅

- [ ] **Referências:**
  - [ ] Todo `\cite{...}` tem entrada em Mesh.bib
  - [ ] Mesh.bib compilado sem erros BibTeX
  - [ ] Nenhuma referência duplicada

- [ ] **Tabelas e Figuras:**
  - [ ] Todas têm captions descritivos
  - [ ] Todas são referenciadas no texto (Figure \ref{...}, Table \ref{...})
  - [ ] Fontes legíveis (mínimo 10pt após escala)

- [ ] **Contagem de Páginas:**
  - [ ] Verifi que os limites de página (típico: 6-8 páginas para IEEE/SBC)

---

## 🔧 Como Compilar e Visualizar

### Opção 1: Overleaf (Recomendado)

1. Vá a https://www.overleaf.com/
2. Upload `artigo-LINHA4.tex` + `Mesh.bib` + `sbc.cls` (template style)
3. Compilar automaticamente → visualizar PDF

### Opção 2: LaTeX Local

```bash
cd documento_latex/Template_SBC/template-latex/

# Compile
pdflatex artigo-LINHA4.tex
bibtex artigo-LINHA4
pdflatex artigo-LINHA4.tex
pdflatex artigo-LINHA4.tex

# View
open artigo-LINHA4.pdf  # macOS
xdg-open artigo-LINHA4.pdf  # Linux
start artigo-LINHA4.pdf  # Windows
```

---

## 📝 Próximas Ações Sequenciais

### HOJE (05/04)
- [ ] Personalize autor/email no LaTeX (5 min)
- [ ] Compile artigo localmente (5 min)
- [ ] Visualize PDF (2 min)
- [ ] Confirme que aparece bem formatado (5 min)

### AMANHÃ (06/04)
- [ ] Leia Introdução em voz alta (verifique fluxo)
- [ ] Compare Introdução com GUIA_CONSTRUCAO (alinhamento)
- [ ] Valide números piloto contra flowdata.xml

### SEMANA 1 (07-12/04)
- [ ] Refinalize Introdução + Metodologia
- [ ] Comece a rodar grid-25 + random-50 (paralelo com escrita)
- [ ] Prepare template de figuras (matplotlib/R script)

### SEMANA 2+ (14/04+)
- [ ] Insira figuras reais conforme dados ficarem prontos
- [ ] Expanda Resultados com análise completa
- [ ] Draft de Conclusão + Contribuições

---

## 📚 Referências Cruzadas Úteis

| Quando Precisar De... | Arquivo | Como Usar |
|:---|:---|:---|
| Validar estrutura SBC | `sbc-template.tex` (original) | Compare com seu artigo-LINHA4.tex |
| Verificar mecanismos AODV | LINHA_4_AODV_vs_OLSR_Detalhado.md | Copie explicações técnicas para Discussão |
| Dados de referência | experiments/pilot_100_aodv_olsr/METADATA_20260404_140424.yaml | Valide parâmetros de simulação |
| Quality gates SBC | GUIA_CONSTRUCAO_TRABALHO_ADR.md | Cross-check pesos de avaliação |
| Template figuras | .github/skills/bmad-agent-network-researcher/assets/ | Use para gráficos finais |

---

## ⚠️ Armadilhas Comuns (Evite!)

| ❌ Erro | ✅ Solução |
|:---|:---|
| Citar papers sem ter lido | Leia abstract + metodologia antes de citar |
| Números de simulação inconsistentes | Documente TODOS os parâmetros em YAML |
| Figuras com resolução baixa | Sempre salve em 600 dpi (print quality) |
| Conclusão que promete mais do que conseguiu | Seja conservador: "achados sugerem" não "provamos" |
| Esquecer de validação estatística | IC 95% é mandatório (não apenas média) |

---

## 🎯 Meta Final

**Entrega:** Artigo completo, formatado SBC, pronto para submissão ou apresentação

**Checklist:**
- ✅ PDF compila sem erros
- ✅ Todas as seções preenchidas (sem TODOs)
- ✅ Dados validados com IC 95%
- ✅ Figuras de alta qualidade
- ✅ Referências formatadas IEEE
- ✅ Reviewer consegue reproduzir: `METADATA.yaml` + `seeds` documentados

---

**Qual é o próximo passo? Quer que eu ajude a:**
1. Compilar o LaTeX localmente e verificar qualidade visual?
2. Extrair dados finais do piloto para validar Tabela 1?
3. Criar script Python para gerar as 3 figuras principais?
4. Refinar a linguagem de qualquer seção específica?
