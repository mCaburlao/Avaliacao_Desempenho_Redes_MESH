# Implementation Guide — LINHA 4 (Memory + Construction Guide Integration)

**Updated:** Abril 2026  
**Status:** ✅ Memory system synchronized with GUIA_CONSTRUCAO_TRABALHO_ADR.md

---

## Memory System Overview

The memory system (`_bmad/memory/bmad-agent-network-researcher-sidecar/`) now tracks **LINHA 4 Scalability** research:

| File | Purpose | Status |
|:---|:---|:---|
| `index.md` | Session state + progress | ✅ Updated |
| `business-domain.md` | Problem domain, stakeholders | ✅ Updated |
| `comparative-matrix.md` | AODV vs OLSR matrix + metrics | ✅ Updated |
| `paper-outline.md` | Article structure (7 sections) | ✅ Updated |
| `experiment-log.md` | Experiment design + phases | ✅ Updated |

---

## Construction Guide Integration

**📖 MAIN REFERENCE:** `GUIA_CONSTRUCAO_TRABALHO_ADR.md` (25 pages, templates included)

This guide provides:
- Seção 1-8: Step-by-step templates for each article section
- Quality gates per section (Peso nota conforme norma UFABC)
- Timeline 6 semanas semana-por-semana
- Checklist Go/No-Go final

**Located:** `_bmad-output/planning-artifacts/mesh-research/GUIA_CONSTRUCAO_TRABALHO_ADR.md`

---

## How Memory + Guide Work Together

### For Researchers (You)

**Phase 1: Planning (Week 1)**
```
1. Read GUIA_CONSTRUCAO_TRABALHO_ADR.md (overview)
2. Review memory files (business-domain, comparative-matrix)
3. Structure your article using templates in guide
```

**Phase 2: Experiments (Week 2-6)**
```
1. Reference experiment-log.md for design
2. Check quality gates in comparative-matrix.md
3. Update experiment-log.md as you complete phases
```

**Phase 3: Analysis (Week 5-6)**
```
1. Use templates from guide Seção 6 (Análise Resultados)
2. Validate against hypotheses in comparative-matrix.md
3. Generate publication-ready figures
```

**Phase 4: Writing (Week 6)**
```
1. Copy-paste templates from guide (Seções 2-7)
2. Customize with your data + context
3. Check quality gates in paper-outline.md
```

### For Network Researcher Agent

**Memory provides context:**
- Problem: business-domain.md
- Metrics: comparative-matrix.md
- Article structure: paper-outline.md
- Experiments: experiment-log.md

**Guide provides details:**
- Templates for each section
- Quality gates + checklists
- Citations + references format
- Writing conventions (Portuguese norma culta)

---

## Quick Start: 3-Step Process

### Step 1: Week 1 — Structure
```
✅ Read GUIA_CONSTRUCAO_TRABALHO_ADR.md Intro (30 min)
✅ Review memory/business-domain.md (5 min)
✅ Copy template Seção 2 (Introdução) from guide
✅ Customize with your context
✅ Save draft v0.1
```

### Step 2: Week 2-6 — Experiments + Analysis
```
✅ Follow experiment-log.md phases:
   ├─ Phase 1: Pilot 100 nodes
   ├─ Phase 2: Intermediate 300-500 nodes
   ├─ Phase 3: Full scale 750-1500 nodes
   └─ Phase 4: Statistical analysis

✅ Update comparative-matrix.md with actual results
✅ Reference paper-outline.md for section structure
```

### Step 3: Week 6 — Writing + Finalization
```
✅ Copy-paste templates from guide (Seções 2-7)
✅ Insert your data + figures
✅ Apply quality gates from guide (checklist final)
✅ Format SBC exact
✅ Entrega impressa + PDF + repositório público
```

---

## Memory Updates Log

### Original Template (Before Guide)
```
index.md: "First Run (New Project)"
business-domain.md: [TBD]
comparative-matrix.md: [No data]
paper-outline.md: [Outline only]
experiment-log.md: [Batch structure only]
```

### After GUIA_CONSTRUCAO Integration (Atual)
```
✅ index.md: LINHA 4 research state + progress (W1-W6)
✅ business-domain.md: Smart cities domain + metrics
✅ comparative-matrix.md: AODV vs OLSR + 5 metrics + hypotheses
✅ paper-outline.md: 7-section article blueprint (SBC format)
✅ experiment-log.md: 4-phase experimental design (140 runs)
```

---

## Key Decision Matrix

### When to Reference What?

**Need:** Design article structure  
→ Read: `paper-outline.md` (memory) + `GUIA_CONSTRUCAO` Seção 1-3

**Need:** Understand protocols & metrics  
→ Read: `comparative-matrix.md` (memory) + `LINHA_4_AODV_vs_OLSR_Detalhado.md`

**Need:** Plan experiments  
→ Read: `experiment-log.md` (memory) + `LINHA_4_MeshSim_QuickStart.md`

**Need:** Domain context  
→ Read: `business-domain.md` (memory) + `LINHA_4_PRD_Escalabilidade.md`

**Need:** Write article section  
→ Read: `GUIA_CONSTRUCAO_TRABALHO_ADR.md` (guide) → Copy template → Customize

---

## Success Criteria (Final)

✅ **Memory synchronized:** All 5 files updated with LINHA 4 data  
✅ **Guide integrated:** Templates link to memory files  
✅ **Phase planning clear:** Week-by-week roadmap in index.md  
✅ **Metrics defined:** 5 metrics in comparative-matrix.md  
✅ **Reproducibility:** RNG seeds + NS-3 version documented  
✅ **Article structure:** 7 sections in paper-outline.md ready for writing

---

## Files Reference (Interconnected)

**Memory System:**
- `index.md` → Overall status
- `business-domain.md` → Problem definition
- `comparative-matrix.md` → Metrics + hypotheses
- `paper-outline.md` → Article structure
- `experiment-log.md` → Experiment phases

**Construction Guide:**
- `GUIA_CONSTRUCAO_TRABALHO_ADR.md` → Templates + quality gates

**Supporting Material:**
- `LINHA_4_PRD_Escalabilidade.md` → Full specification
- `LINHA_4_AODV_vs_OLSR_Detalhado.md` → Protocol analysis
- `LINHA_4_MeshSim_QuickStart.md` → Simulator setup
- `PROXIMOS_PASSOS.md` → 60-day roadmap

**All located in:** `_bmad-output/planning-artifacts/mesh-research/`

---

## Next Action

**Now:** Memory is synchronized with construction guide ✅

**Next:** Execute Week 1 checklist from `PROXIMOS_PASSOS.md`:
1. Advisor meeting + proposal approval
2. Begin article writing (Section 2 Introdução)
3. Setup MeshSim (Week 2)

---

**Memory System: READY FOR EXECUTION**  
**Status: ✅ Fully Integrated with GUIA_CONSTRUCAO_TRABALHO_ADR**
