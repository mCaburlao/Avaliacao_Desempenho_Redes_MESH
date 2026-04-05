# BMAD Output - Planning Artifacts

**Status:** Active | Last Updated: Abril 2026

---

## 📂 Estrutura de Pastas

```
_bmad-output/
├── implementation-artifacts/     (código, scripts, implementações)
├── planning-artifacts/           (estratégia, planejamento, PRDs)
│   └── mesh-research/            (projeto: Pesquisa em redes MESH)
│       ├── README.md             ← Índice do projeto
│       ├── 1_HANDOUT_1Pagina.md  ← COMECE AQUI (5 min)
│       ├── 2_RESUMO_EXECUTIVO*.md
│       ├── 3_PLANO_Acao_60Dias.md
│       ├── MATRIZ_Rastreabilidade*.md
│       ├── GUIA_Literatura_Essencial.md
│       ├── INDICE_E_GUIA_NAVEGACAO.md
│       └── Relatorio_Linhas_Pesquisa_MESH.md (completo, referência)
└── test-artifacts/               (testes, validação, QA)
```

---

## 🎯 Projetos Ativos

### **MESH Research Planning** (`mesh-research/`)
- **Status:** Phase 1 Complete (Problem Formulation)
- **Data Início:** Abril 2026
- **Owner:** Mestrando em Redes de Computadores (UFABC)
- **Objetivo:** Formular linha de pesquisa para dissertação de mestrado
- **Output:** 5 linhas propostas + recomendação (Linha 2: Segurança em MESH IoT)

**Arquivos:**
- 📄 HANDOUT_1Pagina.md — Resumo executivo (leia primeiro)
- 📋 PLANO_Acao_60Dias.md — Roadmap para implementação
- 📊 MATRIZ_Rastreabilidade — Justificação com rigor
- 📚 GUIA_Literatura_Essencial — Sequência de leitura
- 📖 Relatorio_Linhas_Pesquisa_MESH — Análise completa

**Próximas Fases:**
- [ ] Fase 2 (Setup Simulator) — Semana 3-4
- [ ] Fase 3 (Run Simulation) — Semana 10+
- [ ] Fase 4 (Analyze Results) — Semana 14+

---

## 📋 Convenção de Nomenclatura

### **Planning Artifacts**
```
{TopicName}/
├─ README.md (SEMPRE PRIMEIRO)
├─ HANDOUT_1Pagina.md (executivo)
├─ RESUMO_EXECUTIVO_*.md (síntese)
├─ PLANO_Acao_*Days.md (roadmap)
├─ RELATORIO_*.md (referência completa)
└─ GUIA_Literatura_*.md (estudos)
```

### **Implementation Artifacts**
```
{ProjectName}/
├─ src/ (código fonte)
├─ config/ (configurações)
├─ data/ (datasets, logs)
└─ README.md (instruções)
```

### **Test Artifacts**
```
{ProjectName}/
├─ unit_tests/
├─ integration_tests/
├─ test_results.json
└─ coverage_report.md
```

---

## 🚀 Como Usar Esta Pasta

### **1. Se você é NOVO neste projeto:**
1. Navigate to `mesh-research/`
2. Leia `README.md` (índice)
3. Leia `HANDOUT_1Pagina.md` (5 min overview)
4. Estude `RESUMO_EXECUTIVO_Linhas_Pesquisa.md` (45 min)
5. Comece `PLANO_Acao_60Dias.md` (execute week 1)

### **2. Se você é COLLABORADOR no projeto:**
1. Abra `MATRIZ_Rastreabilidade_Artigos_Linhas.md` para contexto
2. Consult `PLANO_Acao_60Dias.md` para status atual
3. Atualizar via Git (pull → review → push)

### **3. Se você é ADVISOR/REVIEWER:**
1. Leia `HANDOUT_1Pagina.md` (quick brief)
2. Aprofunde em `RELATORIO_Linhas_Pesquisa_MESH.md` (credibilidade)
3. Valide via `MATRIZ_Rastreabilidade_*.md` (rigor)

---

## 📊 Padrão de Documento BMAD

Cada documento planning artifact segue:
```
1. **Sumário Executivo** (topo) — <100 palavras
2. **Tabelas/Visuals** — quick reference
3. **Seções Temáticas** — conteúdo estruturado
4. **Próximos Passos** (rodapé) — actionable
5. **Referências** — citadas quando aplicável
```

---

## 🔄 Workflow Recomendado

### **Durante Planning:**
```
Subagent create → output em _bmad-output/planning-artifacts/{topic}/ 
  ↓
README.md + HANDOUT gerados automaticamente
  ↓
User: Review + feedback → update docs if needed
  ↓
Git add, commit, push
```

### **Durante Execution:**
```
Weekly progress → update PLANO_Acao {CurrentWeek}
  ↓
Blockers → refer back para RELATORIO/GUIA conforme necessário
  ↓
Results → move to implementation-artifacts/ quando ready
  ↓
Git: incremental commits
```

---

## 📈 Métricas & Status

| Projeto | Fase | Docs | Status | ETA |
|:---|:---|:---:|:---|:---|
| **mesh-research** | 1/4 | 8 | ✅ Ready | Semana 10 (proposta) |

---

## 💾 Git Integration

### **Commit Message Pattern:**
```bash
git add _bmad-output/planning-artifacts/mesh-research/*

git commit -m "planning: MESH research - semana 5 CHECKPOINT
- Piloto 50 nós coletado
- Análise Python completada
- Advisor meeting scheduled"
```

### **Recommended Workflow:**
```bash
# Pull latest planning docs
git pull origin main

# Check current status
cat _bmad-output/planning-artifacts/mesh-research/PLANO_Acao_60Dias.md | grep "SEMANA $(date +%U)"

# Update progress daily/weekly
vim _bmad-output/planning-artifacts/mesh-research/progress_log.md

# Commit
git add _bmad-output/planning-artifacts/
git commit -m "planning: [project] - status update"
git push origin main
```

---

## 🆘 Troubleshooting

### **"Não acho o documento X"**
→ Consulte `mesh-research/README.md` (índice)
→ Use `find . -name "*X*"` no terminal

### **"Qual documento devo ler para Y?"**
→ Abra `mesh-research/INDICE_E_GUIA_NAVEGACAO.md`
→ Tem tabela "Quando usar cada documento"

### **"Preciso atualizar a recomendação"**
→ Edit: `Relatorio_Linhas_Pesquisa_MESH.md` (base)
→ Update: `RESUMO_EXECUTIVO_*.md` (síntese)
→ Commit with: `git commit -m "planning: MESH - updated recommendation"`

---

## 📞 Manutenção

- **Owner:** Subagent `@bmad-agent-network-researcher`
- **Review Cycle:** Biweekly (conforme progresso projeto)
- **Version:** 1.0 (Abril 2026)
- **Last Update:** Abril 3, 2026

---

**BMAD Output Directory | Planning Artifacts Management**  
**Última atualização: Abril 2026 | Manter atualizado conforme progresso**
