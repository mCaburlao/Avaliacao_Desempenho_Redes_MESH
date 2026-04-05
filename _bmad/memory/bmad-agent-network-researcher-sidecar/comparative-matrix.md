# Comparative Matrix — AODV vs OLSR

**Study:** Escalabilidade em Redes MESH 100-1500 nós  
**Status:** ✅ DESIGN COMPLETE | 🔄 EXECUTION READY  
**Last Updated:** Abril 2026 (Guia Construção integrado)

---

## Protocol Comparison (Theoretical)

| Aspecto | AODV | OLSR | Vencedor |
|:---|:---|:---|:---|
| **Paradigma** | Reativo (on-demand) | Proativo (table-driven) | — |
| **Overhead** | LINEAR | QUADRÁTICO | AODV (>750 nós) |
| **Convergência** | Lenta (5-60s) | Rápida (2-20s) | OLSR |
| **Latência** | Média | Baixa | OLSR (<500), AODV (>800) |
| **CPU Escalabilidade** | ✅ BOA | ❌ RUIM | AODV |

---

## Metrics Defined (5 Main)

| Metric | Unit | Definition | Expected AODV | Expected OLSR | Threshold |
|:---|:---|:---|:---|:---|:---|
| **PDR** | % | (rx/tx)×100 | >90% @ 1500n | <75% @ 1500n | >90% viable |
| **Latência E2E** | ms | time(rx)-time(tx) | 10→150ms | 5→250ms | <300ms OK |
| **Overhead** | % | ctrl_pkt/total×100 | 8→32% (linear) | 12→83% (quad) | <50% acceptable |
| **Convergência** | s | time(first_route) | 5-60s | 2-20s | <30s preferred |
| **CPU** | s | wall clock per sim | <10 @ 100n → ~500 @ 1500n | Same | <20h for 140 runs |

---

## Experimental Design

```
Full Factorial:
├─ Scales: 100, 300, 500, 750, 1000, 1250, 1500 nós (7 levels)
├─ Protocols: AODV, OLSR (2 levels)
├─ Replicates: 10 per config (RNG seeds 0-9)
└─ Total: 140 runs
```

**Simulator:** MeshSim (NS-3 v3.30 ICSI)  
**Duration:** 640s per run (30s warmup + 600s measure + 10s cooldown)  
**Traffic:** UDP CBR 1000 pps, 256-byte packets  
**Topology:** Random Poisson 1000m×1000m area

---

## Expected Results (Predictions)

### Overhead Growth (CRITICAL)

```
Nós   | AODV %   | OLSR %   | Crossover Check
------|----------|----------|------------------
100   | 8±1%     | 12±2%    | OLSR better
300   | 12±2%    | 22±3%    | OLSR better
500   | 17±2%    | 36±4%    | OLSR better
750   | 22±3%    | 51±5%    | ~CROSSOVER (750±50)
1000  | 28±3%    | 68±6%    | AODV better
1500  | 32±4%    | 83±7%    | AODV MUCH better
```

**Fits expected:**
- AODV: y = 0.016x + 0.4 (R² > 0.95)
- OLSR: y = 0.00004x² + 0.02x (R² > 0.95)

### PDR Degradation

```
Both maintain >90% until congestion:
- AODV: >91% even @ 1500
- OLSR: drops to ~75% @ 1000, ~42% @ 1500
```

### Latency Trends

- OLSR: Initially lower, then saturates
- AODV: Linear growth with hop count

---

## Hypotheses to Test

```
H₁: "AODV overhead is LINEAR with scale"
  Null: Overhead does NOT scale linearly
  Test: Linear regression R² > 0.90, p < 0.05
  Expected: CONFIRMED

H₂: "OLSR overhead is QUADRATIC with scale"
  Null: Overhead does NOT scale quadratically
  Test: Quadratic fit R² > 0.90, p < 0.05
  Expected: CONFIRMED

H₃: "Crossover point near 750 nós"
  Null: Crossover outside 600-900 range
  Test: Find fitted curve intersection
  Expected: Crossover 700-800 nós (700±50 IC 95%)
```

---

## Recommendation Matrix (Final Output)

```
Escala        | Recomendado | Razão
--------------|-------------|----------------------------------
<200 nós      | OLSR        | Convergência rápida
200-500 nós   | OLSR/flex   | Overhead aceitável (<50%)
500-750 nós   | Transição   | Trade-offs equilibrados
750-1200 nós  | AODV        | Overhead crítico (OLSR >60%)
>1200 nós     | AODV (obr)  | OLSR inviável
```

---

## Quality Gates

✅ All runs have 10 replicas (IC 95% computable)  
✅ No NaN/Inf in results  
✅ RNG seeds logged for reproducibility  
✅ AODV overhead R² > 0.90 linear fit  
✅ OLSR overhead R² > 0.90 quadratic fit  
✅ Crossover within 600-900 node range

## Statistical Rigor

Once Capability 4 runs, fill this:

| Comparison | Protocol A | Protocol B | Test Used | p-value | Significant? | Effect Size | Interpretation |
|-----------|-----------|-----------|-----------|---------|--------------|-------------|-----------------|
| Latency | Mean ± IC | Mean ± IC | t-test | | | | |
| PDR | Mean ± IC | Mean ± IC | Mann-Whitney U | | | | |
| Overhead | Mean ± IC | Mean ± IC | t-test | | | | |

---

## Preliminary Findings

[This section fills in during Capability 4 analysis]

### Discovery Insights
- What surprised you?
- Which protocol won where?
- Any unexpected tradeoffs?

### Nuances & Context
[Real research rarely has a clear "winner." Explain the nuances.]

**Example:**
- "AODV achieves 29% lower latency (p<0.001) in high-mobility scenarios"
- "RPL shows more stable overhead (~15% variance vs 40% for AODV)"
- "Neither protocol shows PDR advantage — both ≈98% in all scenarios"

### Recommendations
[Given your results, which protocol for which use case?]

---

## Scenario Legend

Replace placeholders above:

| Scenario | Type | Nodes | Mobility | Notes |
|----------|------|-------|----------|-------|
| Scenario 1 | [Static/Mobile/Disaster] | [N] | [Model] | [Brief description] |
| Scenario 2 | [Static/Mobile/Disaster] | [N] | [Model] | [Brief description] |
| Scenario 3 | [Static/Mobile/Disaster] | [N] | [Model] | [Brief description] |

---

## Traceability to Paper

When writing your paper:

- **Table [X]:** Comparative matrix → Results section
- **Figure [Y]:** Latency comparison chart → Results section
- **Section [Z]:** Tradeoff discussion → Discussion section

---

## Document Control

- **Immutable Sections:** Metric definitions (once set, don't change)
- **Evolving Sections:** Results (TBD → filled in during simulations)
- **Finalized On:** After Capability 4 analysis complete
- **Next Destination:** Final paper (Section V: Results)

---

**Status Check:** Do all metrics align with your business domain (see `business-domain.md`)?
