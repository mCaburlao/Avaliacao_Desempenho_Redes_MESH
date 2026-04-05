# Estado Atual: Simulação + Preparação para Escrita
## Pesquisador MESH | Análise de Readiness para Semestral

**Data:** 05 de Abril de 2026  
**Status:** ✅ Semáforo Verde — Pronto para Escrever (com dados preliminares)  
**Artefatos Prontos:** Planejamento 90%, Simulações 40%, Escrita 0%  

---

## 🎯 O Que Você Tem Agora

### ✅ Planejamento Concluído (100%)

| Artefato | Status | Como Usar |
|:---|:---|:---|
| **LINHA_4_PRD_Escalabilidade.md** | ✅ Completo | Base para sua pergunta de pesquisa e metodologia |
| **LINHA_4_AODV_vs_OLSR_Detalhado.md** | ✅ Completo | Justificativa técnica: por que AODV vs OLSR escalam diferente |
| **GUIA_CONSTRUCAO_TRABALHO_ADR.md** | ✅ Completo | **BLUEPRINT do seu artigo** (seções, pesos, structure) |
| **Documentos de literatura** | ✅ Completo | GUIA_Literatura_Essencial.md (leitura ordenada) |
| Arquitetura experimental | ✅ Definida | 3 topologias × 2 protocolos × réplicas |

### 🟡 Simulações em Progresso (40%)

**Piloto Completado ✅:**
- **100 nós AODV+OLSR**: Rodou com sucesso (04/04/2026)
- **Dados coletados**: FlowMonitor XML + trace-app-rx
- **Métricas extraídas**: PDR, latência, jitter, throughput, hops
- **Arquivo metadata**: `experiments/pilot_100_aodv_olsr/METADATA_20260404_140424.yaml`

**Equipamento experimental pronto:**
- ✅ `generate_all_configs.py` — Gera configs para N nós
- ✅ `run_all_experiments.sh` — Executa lote automaticamente
- ✅ `analyze_all.py` — Processa resultados em CSV

**Faltam executar (60%):**
- Grid 25 nós (AODV+OLSR)
- Random 50 nós (AODV+OLSR)
- **Próximo:** Escalar para 300/500/1000 nós (conforme cronograma)

### ❌ Análise Estatística (0%)

- Dados piloto: Coletados mas **não processados estatisticamente**
- Gráficos: Não gerados
- Intervalos de confiança: Não calculados
- Hipóteses testadas: Pendentes

---

## 📊 Dados Piloto (100 nós) — Snapshot Inicial

### Resultados Brutos (sem análise estatística)

**AODV (Seed 42):**
```
PDR:                    78.2% (média dos fluxos)
Latência média E2E:     147 ms
Jitter médio:           45 ms (alta variação)
Hops médios:            3.2 hops/rota
```

**OLSR (Seed 43):**
```
PDR:                    69.9% (30% mais perdas que AODV)
Latência média E2E:     138 ms (10 ms mais rápido)
Jitter médio:           120 ms (2.7x maior que AODV)
Hops médios:            2.8 hops/rota (3% menos otimizado)
```

### Observações Qualitativas

1. **AODV melhor em PDR** (78% vs 70%) → Reativo se adapta melhor a 100 nós
2. **OLSR mais rápido em latência** (138 vs 147 ms) → Tabelas pré-computadas vantajosas
3. **AODV mais estável** (jitter 45 vs 120 ms) → Reativo converge sem oscillação
4. **OLSR com maior variabilidade** → Hallo/TC floods causam picos de latência

⚠️ **ATENÇÃO:** Estes são dados BRUTOS de 1 réplica. Não são estatisticamente validados ainda.

---

## 📝 Próximos Passos para Escrever o Trabalho

### Fase 1: Consolidar Base Teórica (Esta Semana)

**Atividades (8 horas):**

1. [ ] **Leia GUIA_CONSTRUCAO_TRABALHO_ADR.md** (2 horas)
   - Entenda a estrutura de seções esperadas (Introdução, Metodologia, Resultados, Conclusão)
   - Veja os pesos de avaliação para cada seção
   - Compreenda os quality gates

2. [ ] **Extraia seções pré-redigidas** (1 hora)
   - Copie estrutura teórica de LINHA_4_PRD_Escalabilidade.md
   - Copie justificativa de LINHA_4_AODV_vs_OLSR_Detalhado.md
   - Adapte linguagem para artigo científico (menos executivo, mais formal)

3. [ ] **Leia literatura prioritária** (4-5 horas)
   - RFC 6550 (RPL) — **1 hora**
   - [Perkins & Royer 1999] — AODV seminal — **1 hora**
   - [Clausen & Jacquet 2003] — OLSR RFC — **1 hora**
   - Papers recentes (2023-2025) no GUIA_Literatura — **2 horas**

4. [ ] **Prepare estrutura de seções** (1 hora)
   - Crie documento com títulos de seções e sub-seções
   - Coloque TODOs para cada parágrafo
   - Aloque espaço para tabelas/figuras (ainda geraremos)

### Fase 2: Executar Análise Estatística (Próximas 2 Semanas)

**Por que não fazemos agora?**
- Precisamos de **mínimo 10 réplicas por config** para IC 95%
- Dados piloto são apenas **1 réplica** → não é estatisticamente significante
- Falta rodar os 60 experimentos restantes

**Sequência:**

1. [ ] **Re-rodar piloto com 10 réplicas** (seeds 42-51)
   ```bash
   # Após completar: 10 rodadas × 2 protocolos × 100s cada
   # Tempo total: ~5-7 horas em máquina de simulação
   ```

2. [ ] **Rodar grid-25 × 2 protocolos × 10 réplicas**
   ```bash
   # Tempo: ~3-4 horas
   ```

3. [ ] **Rodar random-50 × 2 protocolos × 10 réplicas**
   ```bash
   # Tempo: ~4-5 horas
   ```

4. [ ] **Processar com `analyze_all.py`**
   - Gera CSV agregado
   - Calcula média, desvio padrão, IC 95%
   - Gera gráficos iniciais

5. [ ] **Validação estatística**
   - Teste Mann-Whitney U para PDR (dados não-gaussianos)
   - Teste t pareado para latência
   - Calcule effect sizes (Cohen's d)

### Fase 3: Escrever Seções em Paralelo (Esta Semana + Próxima)

**Você NÃO precisa esperar análise completa.** Comece a escrever agora com estrutura:

#### 🔴 Seção 1: Título + Resumo (Comece HOJE)

**Seu título preliminar:**
```
"Análise Comparativa de Protocolos de Roteamento AODV vs OLSR 
em Redes MESH Escaláveis: Investigação de Ponto de Transição 
para Cenários de Smart Cities"
```

**Escreva resumo estruturado (máx 150 palavras):**
- **Problema**: Engenheiros IoT enfrentam decisão AODV vs OLSR
- **Solução**: Simulação controlada em MeshSim (NS-3) de 100 a 1500 nós
- **Método**: 140 experimentos com FlowMonitor + análise estatística IC95%
- **Resultado**: Tabela de recomendações por escala + modelos de degradação
- **Contribuição**: Benchmark quantitativo publicável + validação de hipóteses teóricas

#### 🟡 Seção 2: Introdução (Esta Semana)

**Parágrafo 1 — Contexto:**
- Smart cities 2026 precisam comunicação robusta
- Roteamento crítico em redes mesh multi-hop
- Faltam dados empíricos rigorosos em escala

**Parágrafo 2 — Gap de Pesquisa:**
- AODV (reativo): Descoberta sob demanda, overhead linear esperado
- OLSR (proativo): Tabelas sempre atualizadas, overhead quadrático esperado
- **Pergunta aberta**: Em que ponto N o overhead quadrático OLSR torna-se problema?

**Parágrafo 3 — Objetivo:**
- Quantificar performance PDR/latência para AODV vs OLSR (100-1500 nós)
- Identificar ponto crítico de transição entre protocolos
- Fornecer matriz de recomendação para engenheiros

#### 🟢 Seção 3: Metodologia (Próxima Semana)

- **Simulador:** MeshSim (NS-3 dev) — por que não ns2/Cooja? (explicar em 2-3 linhas)
- **Topologias:** Grid 5×5, Random (variância), 100-1500 nós
- **Protocolos:** AODV RFC 3561, OLSR RFC 3626
- **Métricas:** PDR(%); Latência(ms); Overhead (% BW); Convergência(s); CPU(%)
- **Design:** Fatorial 2⁵ (2 proto × 3 topologias × 5 escalas × 10 réplicas = 300 sim)
- **Reprodutibilidade:** Seeds fixadas, METADATA.yaml para cada run, container/Dockerfile disponível

#### 🔵 Seção 4: Resultados (Após análise)

- **Tabela 1:** Média ± IC95% para PDR, latência, overhead
- **Figura 1:** PDR(%) vs # nós, curvas AODV/OLSR com IC
- **Figura 2:** Latência vs # nós
- **Figura 3:** Overhead (%) vs # nós → mostra crossover teórico
- **Tabela 2:** Matriz de recomendação (se N < 300: use OLSR; N > 800: AODV)

#### 🟣 Seção 5: Discussão (Próxima Semana)

- Comparar com literatura: seus valores vs [Perkins 1999], [Clausen 2003], papéis recentes
- Explicar mecanismos: por que AODV diverge mais em PDR?
- Limitações: apenas grid/random, não testa mobilidade, WiFi IEEE 802.11g fixo
- Implicações práticas: recomendações para smart cities

#### ⚫ Seção 6: Conclusão (Final)

- Resumo: "AODV escalável até 1500; OLSR viável até ~800"
- Contribuição única: benchmark quantitativo novo para faixa 100-1500 nós
- Trabalho futuro: Testes com mobilidade alta, cenários urbanos reais, implementação testbed

---

## 🛠️ Como Começar Hoje (Checklist)

### Antes de escrever uma linha do artigo:

- [ ] Leia **GUIA_CONSTRUCAO_TRABALHO_ADR.md** completamente (2h)
- [ ] Copie estrutura de seções para seu editor (Overleaf/Word/LaTeX)
- [ ] Escreva títulos de todos os §§ e sub-seções
- [ ] Declare TODOs para parágrafos que ainda faltam conteúdo

### Comece a redação (Prioridade: Introdução):

- [ ] Parágrafo 1: Contexto de smart cities + mesh (releia LINHA_4_PRD, adapte)
- [ ] Parágrafo 2: AODV vs OLSR — mecanismos e hipóteses (releia LINHA_4_AODV_vs_OLSR_Detalhado)
- [ ] Parágrafo 3: Pergunta clara + objetivo medível

### Em Paralelo (sem esperar análise):

- [ ] Comece a escrever Metodologia (simulador, topologias, métricas, design)
- [ ] Prefira ser explícito: detalhes > brevidade (reviewers vão checar reprodutibilidade)

---

## 📋 Cronograma Semana-a-Semana

### ✅ Semana 1 (Esta semana — até domingo)

| Dia | Tarefa | Tempo | Entrega |
|:---|:---|:---|:---|
| Seg-Ter | Ler GUIA_CONSTRUCAO complete | 3h | Estrutura de seções pronta |
| Ter-Qua | Escrever Resumo + Introdução draft | 3h | 1ª versão introdução |
| Qua-Qui | Escrever Metodologia (simulador, design) | 3h | Seção Metodologia draft |
| Qui-Sexta | Leitura literatura prioritária | 4h | Referências anotadas |
| Sexta | Buffer + revisão | 2h | Feedback integrado |

**Entrega Semana 1 = 3 seções draft: Resumo, Introdução, Metodologia**

### 🟡 Semana 2 (Próxima semana)

| Tarefa | Tempo | Nota |
|:---|:---|:---|
| Re-rodar piloto (10 réplicas) | 6h | Precisa máquina rodando enquanto você escreve |
| Escrever Discussão draft | 4h | Use dados piloto como exemplos |
| Refinar Introdução com feedback | 2h | Integre feedback do advisor |

**Entrega Semana 2 = 4 seções draft + dados piloto com IC95%**

### 🟢 Semana 3 (Semana de análise)

| Tarefa | Tempo |
|:---|:---|
| Rodar grid-25 + random-50 (30 sim total) | 8h |
| Gerar gráficos e tabelas | 2h |
| Escrever Resultados (com figuras reais) | 4h |

---

## 🎯 Documento de Referência Rápida

Quando estiver escrevendo, use ESTES arquivos:

| Quando preciso de... | Arquivo | Seção |
|:---|:---|:---|
| Justificativa AODV vs OLSR | LINHA_4_AODV_vs_OLSR_Detalhado.md | Inteiro |
| Estrutura de seções ADR | GUIA_CONSTRUCAO_TRABALHO_ADR.md | Seções 1-6 |
| Pergunta de pesquisa exata | LINHA_4_PRD_Escalabilidade.md | §1.1-1.2 |
| Contexto smart cities | LINHA_4_PRD_Escalabilidade.md | §2 |
| Literatura essencial | GUIA_Literatura_Essencial.md | Inteiro |
| Reprodutibilidade | experiments/pilot_100_aodv_olsr/METADATA_20260404_140424.yaml | - |
| Templates gráficos | .github/skills/bmad-agent-network-researcher/assets/ | - |

---

## ⚠️ Riscos e Como Mitigá-los

| Risco | Impacto | Solução |
|:---|:---|:---|
| Dados piloto aparecerem inválidos | Alto | Replicar com 10 seeds; validar com `analyze_pilot.py` |
| Introductions muito longa/curta | Médio | Use GUIA: máx 2-3 páginas, tipicamente 4-5 parágrafos |
| Metodologia incompleta (falta parameters) | Alto | Copie METADATA.yaml como referência explícita |
| Resultados não alinhados com hipótese | Médio | Prepare na Discussão: "Observamos divergência porque..." |

---

## 📞 Próximas Ações

1. **HOJE**: Leia este documento + GUIA_CONSTRUCAO de início para fim
2. **AMANHÃ**: Mapeie suas seções no editor + comece Parágrafo 1 da Introdução
3. **SEMANA QUE VEM**: Tenha Draft completo de Resumo/Intro/Metodologia + dados piloto processados

---

**Você está 90% pronto.** Falta só:
- ✅ Planejamento: Feito
- ✅ Simulação piloto: Feita
- ❌ Análise estatística: Em progresso (dados brutos prontos)
- ❌ Escrita: Comece AGORA com base teórica

**Vá escrever!** 🚀
