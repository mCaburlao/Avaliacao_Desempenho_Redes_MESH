# First-Run Onboarding (Init)

## Trigger

On first activation (no memory files found), display onboarding menu.

## Menu Flow

```
╔════════════════════════════════════════════════════════════════╗
║   Bem-vindo ao Pesquisador Especialista em Redes MESH!        ║
║                                                                ║
║  Sou seu especialista em pesquisa de protocolos de roteamento ║
║  Our job: Fazer sua pesquisa rigorosa, reproducível e pronta  ║
║           para publicação.                                     ║
╚════════════════════════════════════════════════════════════════╝

Vejo que é sua PRIMEIRA sessão. 

O que você quer fazer?

  [1] 🆕 Novo projeto de pesquisa
      → Começar do zero com uma idea
  
  [2] 📋 Carregar projeto TEMPLATE
      → Usar exemplo pré-preenchido como starting point
  
  [3] ❓ Ver meus 4 capabilities
      → Listar o que eu posso fazer

Escolha (1-3):
```

## Path 1: Novo Projeto

```
Ótimo! Vamos estruturar sua pesquisa.

Para começar, preciso de clareza em 3 pontos:

1️⃣  DOMÍNIO DE NEGÓCIO
   "Por que você estuda MESH networks?"
   
   Contexto (ex: IoT, disaster networks, mobile ad-hoc):
   > _

2️⃣  PROTOCOLOS
   "Quais 2 protocolos você quer comparar?"
   
   Protocolo A (ex: AODV, DSR, OLSR):
   > _
   
   Protocolo B (ex: RPL, BATMAN, Babel):
   > _

3️⃣  APLICAÇÃO CRÍTICA
   "Qual métrica importa mais? (latência, PDR, overhead, convergence)?"
   
   Sua prioridade:
   > _

[Após respostas]

Perfeito! Criei seus arquivos de memória:
✅ business-domain.md — seu contexto
✅ comparative-matrix.md — protocolos vs métricas
✅ paper-outline.md — estrutura do artigo
✅ experiment-log.md — histórico (vazio por enquanto)

Próximo passo? Digite:
  1 → Refinar domínio (Capability 1: Define Problem)
  2 → Ver meus capabilities
  0 → Voltar ao menu principal
```

## Path 2: Carregar Template

```
Ótimo! Você pode:

[A] Usar EXEMPLO PADRÃO
    → "AODV vs RPL em Redes de Desastres"
    → Popula todos os templates com valores reais
    → Você edita depois conforme precisar

[B] Carregar TEMPLATE VAZIO
    → Estrutura base para você preencher

Escolha (A/B):
```

### Path 2A: Standard Example

```
Carregando template: AODV vs RPL em Redes de Desastres...

✅ business-domain.md — Pre-filled com contexto de desastres
✅ comparative-matrix.md — AODV vs RPL vs 6 métricas
✅ paper-outline.md — Estrutura de artigo científico
✅ experiment-log.md — Vazio, pronto para suas simulações

Arquivos criados em:
  {project-root}/_bmad/memory/bmad-agent-network-researcher-sidecar/

Você pode editar esses arquivos em qualquer editor de texto.
Quando terminar, volte aqui e escolha:
  1 → Capability 1: Refine Problem
  2 → Capability 2: Setup Simulator
  3 → Ver todos os capabilities

Próximo?
```

### Path 2B: Empty Template

```
Carregando template vazio...

✅ business-domain.md — Estrutura com placeholders
✅ comparative-matrix.md — Table schema vazio
✅ paper-outline.md — Outline structure
✅ experiment-log.md — Vazio

Preencha os templates conforme progride.
Qualquer dúvida, volte aqui e escolha "Ver abilities".

Próximo passo:
  1 → Capability 1: Define Problem (ajuda interativa)
  2 → Ver meus capabilities
```

## Path 3: Ver Capabilities

```
Meus 4 capabilities organizados no workflow:

┌─────────────────────────────────────────────────────────────┐
│ CAPABILITY 1: DEFINE PROBLEM                                │
│ ──────────────────────────────────────────────             │
│ Você: Define domínio, protocolos, cenários, métricas        │
│ Eu: Orquestra bmad-domain-research + cria PRD formal        │
│ Output: PRD + Comparative Matrix                            │
│ Time: ~1-2 horas                                            │
│                                                             │
│ Status em seu projeto: [1/4 ✅ | 2/4 🔄 | 1/4 ⏳]           │
│                                                             │
│ Começar? [S/N]                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAPABILITY 2: SETUP SIMULATOR                               │
│ ──────────────────────────────────────────────             │
│ Você: Escolhe simulador (ns-3? OMNET++? SimPy?)             │
│ Eu: Desenha arquitetura + gera código skeleton              │
│ Output: Simulator code pronto + config template             │
│ Time: ~2-3 horas                                            │
│                                                             │
│ Pré-requisito: Capability 1 completo                        │
│ Status: 🔒 Locked (complete Cap 1 first)                    │
│                                                             │
│ Começar? [S/N]                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAPABILITY 3: RUN SIMULATION                                │
│ ──────────────────────────────────────────────             │
│ Você: Roda experimentos no seu terminal                     │
│ Eu: Gero scripts shell + metadata tracking                  │
│ Output: Raw data (CSV/logs) com auditoria completa          │
│ Time: Depende (pode pedir mais / menos scenarios)           │
│                                                             │
│ Pré-requisito: Capability 2 completo                        │
│ Status: 🔒 Locked (complete Cap 2 first)                    │
│                                                             │
│ Começar? [S/N]                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAPABILITY 4: ANALYZE RESULTS                               │
│ ──────────────────────────────────────────────             │
│ Você: Fornece dados brutos                                  │
│ Eu: Gera scripts Python → gráficos + estatísticas           │
│ Output: Análise publishável (gráficos + tabelas + síntese)  │
│ Time: ~1-2 horas                                            │
│                                                             │
│ Pré-requisito: Capability 3 completo                        │
│ Status: 🔒 Locked (complete Cap 3 first)                    │
│                                                             │
│ Começar? [S/N]                                              │
└─────────────────────────────────────────────────────────────┘

Qual capability você quer explorar?
(ou [0] voltar ao menu inicial)
```

## Main Menu (After First Run)

```
╔════════════════════════════════════════════════════════════════╗
║   Pesquisador Especialista em Redes MESH                      ║
║   Status: QUALIFIED — You're working on "AODV vs RPL" study   ║
║   Last update: 2026-04-02 14:30 (Capability 2 in progress)    ║
╚════════════════════════════════════════════════════════════════╝

O que você quer fazer?

  [1] Capability 1: Define Problem (refinement)
  [2] Capability 2: Setup Simulator
  [3] Capability 3: Run Simulation
  [4] Capability 4: Analyze Results

  [M] Ver Memory (index.md, domain, matrix, outline)
  [S] Status atual (qual está completo?)
  [R] Resetar projeto (start novo)

Escolha (1-4, M, S, R):
```

---

## Implementation Notes

- Display menu at every activation
- Remember choice (save to index.md)
- Lock capabilities until prerequisites are met
- Offer "Back to menu" at every step
- On error, explain and offer retry
