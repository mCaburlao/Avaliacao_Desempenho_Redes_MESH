# Comparative Matrix Template

**Study:** [Your Protocol Comparison]  
**Created:** [Date]  
**Status:** IN PROGRESS | COMPLETE  

---

## Overview

This matrix tracks every protocol against every metric. It's your **single source of truth** throughout the project.

- **Rows:** Metrics
- **Columns:** Protocols
- **Cells:** Results (after simulation runs)

---

## Matrix

| Metric | Unit | Protocol A | Protocol B | Winner | Notes |
|--------|------|-----------|-----------|--------|-------|
| **Latency P50** | ms | TBD | TBD | - | [To be filled after Capability 3] |
| **Latency P95** | ms | TBD | TBD | - | [To be filled after Capability 3] |
| **Latency P99** | ms | TBD | TBD | - | [Optional detail] |
| **PDR (Scenario 1)** | % | TBD | TBD | - | [Static network] |
| **PDR (Scenario 2)** | % | TBD | TBD | - | [Mobile: random waypoint] |
| **PDR (Scenario 3)** | % | TBD | TBD | - | [Mobile: disaster] |
| **Overhead (Static)** | % | TBD | TBD | - | [% control traffic] |
| **Overhead (Mobile)** | % | TBD | TBD | - | [% control traffic] |
| **Convergence Time** | sec | TBD | TBD | - | [Time to find path] |
| **Route Stability** | path changes/min | TBD | TBD | - | [Lower = more stable] |

---

## Confidence Intervals

Once data is available, report as: **Mean ± IC(95%)**

**Example:**
```
Protocol A Latency P50 = 12.3 ± 1.2 ms  (N=100, α=0.05)
Protocol B Latency P50 = 8.7 ± 0.9 ms   (N=100, α=0.05)
```

---

## Statistical Significance

| Comparison | Test Used | p-value | Significant? | Effect Size |
|-----------|-----------|---------|--------------|-------------|
| A vs B (Latency) | t-test | 0.001 | ✅ YES | Cohen's d = 1.76 |
| A vs B (PDR) | Mann-Whitney U | 0.023 | ✅ YES | r = 0.42 |
| A vs B (Overhead) | t-test | 0.156 | ❌ NO | Cohen's d = 0.34 |

---

## Preliminary Conclusion

[After all results are in, fill this section]

**Winner:** [If there is one, depending on your priorities]

**Nuance:** [Protocols have tradeoffs — best protocol depends on scenario]

**Example:**
- "AODV wins on latency (29% lower, p<0.001)"
- "RPL wins on overhead consistency (~15% lower variance)"
- "Neither wins on PDR — both ≈98% in all scenarios"
- "Recommendation: Use AODV for latency-critical apps; RPL for predictable control budgets"

---

## Related Documents

- **Problem Definition:** See `business-domain.md`
- **Experimental Results:** See Capability 4 outputs (analysis/)
- **Paper Section:** Table [X] in final article

---

**Next?** After Capability 3 completes, return here to fill in results.
