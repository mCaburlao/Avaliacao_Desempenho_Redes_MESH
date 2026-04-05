# LINHA 4: Cheat Sheet — Impressão A4

**Print & Carry to Advisor Meetings**

---

## 🎯 THE QUESTION
> **"Como AODV (reativo) vs OLSR (proativo) escalam de 100 para 1500 nós?"**

- Crossover point: ~700 nós (hipótese)
- AODV overhead: LINEAR (escalável)
- OLSR overhead: QUADRÁTICO (não escalável)

---

## 💼 THE DOMAIN
- **Smart Cities 2026** (iluminação 3k nós, ar 800, assets 500)
- **Stakeholders:** Engenheiros IoT, admin cidades, pesquisadores
- **Gap:** Recomendações por # de nós NÃO existem (benchmarking falta)

---

## ⚙️ THE PROTOCOLS

| Aspecto | AODV | OLSR |
|:---|:---|:---|
| Paradigma | Reativo (on-demand) | Proativo (table-driven) |
| Filosofia | "LAZY" (descobre quando precisa) | "EAGER" (saiba tudo) |
| Overhead | LINEAR c/ fluxos | QUADRÁTICO c/ topologia |
| Latência | Alta inicial, depois baixa | Sempre baixa |
| Escalabilidade | ✅ BOA >500 | ❌ RUIM >800 |
| Convergência | Lenta (RREQ flooding) | Rápida (TC preemptivo) |

---

## 📊 THE 5 METRICS

1. **PDR** — % packets delivered (quality)
   - Target: >90% até 1500 nós

2. **Latência E2E** — delay (responsiveness)
   - AODV: 10-150ms (cresce com hops)
   - OLSR: 5-250ms (congestão)

3. **Overhead** — control packets %
   - AODV: 5-30% (linear)
   - OLSR: 10-80%+ (quadrático explosion!)

4. **Convergência** — tempo primeira rota (deployment)
   - AODV: 5-60s
   - OLSR: 2-20s

5. **CPU/Memória** — compute overhead
   - 100 nós: <10s
   - 1500 nós: ~500s

---

## 🔬 THE EXPERIMENT

**Variáveis:**
- Nós: 100, 300, 500, 750, 1000, 1250, 1500
- Protocolo: AODV, OLSR
- Réplicas: 10 cada

**Total:** 140 rodadas × 640s = ~18h compute (paralelo)

**Simulador:** MeshSim (NS-3 baseado)

---

## ✅ MESHSIM SUPORTA?
- ✅ AODV?           SIM
- ✅ OLSR?           SIM
- ✅ WiFi?           SIM
- ✅ Random topo?    SIM
- ✅ PCAP output?    SIM

**Conclusão: MeshSim é perfeito para Linha 4**

---

## 📅 THE TIMELINE

| Semestre | Meta | Semanas |
|:---|:---|:---|
| 1 | Setup MeshSim + proposta + primeiros dados | 13 |
| 2 | Escalar para 500-1000 nós | 13 |
| 3 | Full scale + análise estatística | 13 |
| 4 | Dissertação + paper IEEE | 13 |
| **TOTAL** | **Defesa** | **52** |

---

## 🏆 THE EXPECTED OUTCOME

### Paper (Publication)
```
Title: "Scalability Analysis of AODV and OLSR 
in Dense Mesh Networks: 100-1500 Node Benchmark"

Target: IEEE Transactions on Mobile Computing
```

### Dataset
```
Public repository with all 140 runs:
- PCAPfiles, raw logs, processed CSV
- Fully reproducible (RNG seeds, parameters)
```

### Dissertação
```
70-80 páginas:
1. Introdução
2. Literatura (AODV, OLSR, benchmarks)
3. Metodologia
4. Resultados + análise estatística
5. Discussão + recomendações práticas
6. Conclusão
+ Apêndices (código, configs)
```

---

## 🚀 NEXT 60 DAYS

| Week | What | Deliverable |
|:---|:---|:---|
| 1 | Read docs + advisor approval | Go/No-Go decision |
| 2 | Install MeshSim + pilot 100n AODV | Results .csv |
| 3 | Pilot OLSR + comparison | Gráficos 100n |
| 4 | Batch 300-500n | Data 3 escalas |
| 5-6 | Análise + proposta formal | Formal approval |
| 6-10 | Literature study + refinement | Plan sem 1-4 |

**Goal:** Semana 6 = **Proposta formal aprovada + primeiros gráficos**

---

## 🎓 VIABILIDADE SCORE

| Critério | Score | Evidência |
|:---|:---|:---|
| Pergunta | ✅✅✅ | Novel, measureable, relevant |
| Simulador | ✅✅✅ | MeshSim found locally |
| Cronograma | ✅✅✅ | 12-15m realista |
| Publicação | ✅✅✅ | Benchmarks bem-citados |
| Probabilidade sucesso | ✅✅✅ | AODV/OLSR comportam diferente? YES |
| **OVERALL** | **✅✅✅ Excelente** | **Go ahead** |

---

## 📞 IF YOU GET STUCK

| Problem | Solution |
|:---|:---|
| MeshSim compile error | → LINHA_4_MeshSim_QuickStart.md %troubleshooting |
| Data doesn't look right | → Check LINHA_4_AODV_vs_OLSR_Detalhado.md for expected ranges |
| Advisor wants detail | → Use LINHA_4_PRD_Escalabilidade.md (full spec) |
| Unsure about overflow | → Reread LINHA_4_AODV_vs_OLSR_Detalhado.md (explains philosophies) |

---

## 🎯 DECISION

**You have MeshSim → Escolha LINHA 4**

✅ Install MeshSim (2-3h)  
✅ Pilot run (2h)  
✅ First results (Week 2)  
✅ Advisor approval (Week 3)  
✅ Full execution (Months 2-12)  

**Question?** → Read PROXIMOS_PASSOS.md

---

**LINHA 4 Cheat Sheet | Print & Use | April 2026**
