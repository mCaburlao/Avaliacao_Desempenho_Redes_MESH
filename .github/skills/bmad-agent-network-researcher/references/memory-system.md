# Memory System

## Purpose

Rastrear seu progresso entre sessions. Cada capability produz artifacts que dependem das anteriores.

## Memory Structure

Base: `{project-root}/_bmad/memory/bmad-agent-network-researcher-sidecar/`

```
bmad-agent-network-researcher-sidecar/
├── index.md                      # Current session state
├── business-domain.md            # Domínio de negócio (CRÍTICA)
├── comparative-matrix.md         # Protocolos vs métricas (CRÍTICA)
├── paper-outline.md              # Estrutura do artigo (CRÍTICA)
└── experiment-log.md             # Histórico de simulações
```

## Files

### index.md
**What:** Current session state and where you are in workflow.

### business-domain.md (CRÍTICA)
**What:** Contexto científico imutável. Por que você pesquisa isso?

### comparative-matrix.md (CRÍTICA)
**What:** Tabela que rastreia cada protocolo vs cada métrica. Seu mapa de rota.

### paper-outline.md (CRÍTICA)
**What:** Estrutura do artigo em progresso. Conecta cada capability ao paper.

### experiment-log.md
**What:** Histórico. Qual config rodou quando?

## Memory Protocol

Each capability saves to memory automatically:

1. **Problem Definition** → Updates `business-domain.md` + `comparative-matrix.md` + `index.md`
2. **Simulator Setup** → Updates `paper-outline.md` (methodology section) + `index.md`
3. **Run Simulation** → Appends to `experiment-log.md` + `index.md`
4. **Analyze Results** → Updates `comparative-matrix.md` (fills in results) + `paper-outline.md` (results section) + `index.md`

## Load Protocol (on activation)

```python
# Pseudo-code for agent initialization

def load_memory():
    index = load("index.md")
    if index.status == "first_time":
        return "new_project"
    else:
        business_domain = load("business-domain.md")
        matrix = load("comparative-matrix.md")
        paper = load("paper-outline.md")
        log = load("experiment-log.md")
        return {
            "business_domain": business_domain,
            "matrix": matrix,
            "paper": paper,
            "experiment_log": log,
            "current_status": index.status
        }
```

On first activation, all files are created from templates (see `/assets/`).

## Notes

- **Public:** All memory files are in git (version control)
- **Portable:** Move sidecar folder wherever; agent finds it
- **Fault-tolerant:** Each file is independent; corruption doesn't cascade
- **Searchable:** All in markdown; grep-friendly
