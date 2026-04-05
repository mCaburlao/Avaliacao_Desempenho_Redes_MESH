# Experiment Log — LINHA 4 Execution

**Project:** AODV vs OLSR Scalability Analysis (100-1500 nodes)  
**Start Date:** April 2026 (planned)  
**Status:** 🔄 DESIGN COMPLETE | Planning execution phases  
**Simulator:** MeshSim (NS-3 v3.30 ICSI)

---

## Experiment Design (Complete)

**Full Factorial Design:**
```
Scales: 100, 300, 500, 750, 1000, 1250, 1500 nós (7 levels)
Protocols: AODV, OLSR (2 levels)
Replicates: 10 per config (RNG seeds 0-9)
Total: 140 runs
Estimated CPU: ~18-24h @ 8 cores parallel
```

---

## Phase 1: Pilot (Week 2-3)

Target: 100-node validation  
- AODV: 10 runs, seeds 0-9
- OLSR: 10 runs, seeds 0-9

---

## Phase 2: Intermediate (Week 4-5)

Target: Scales 300-500 (40 runs)  
Validate overhead models (linear vs quadratic)

---

## Phase 3: Full Scale (Week 5-6)

Target: Scales 750-1500 (80 runs)  
Complete all 140 experiments

---

## Phase 4: Analysis (Week 5-6)

- Compute IC 95%
- Hypothesis tests
- Publication-ready plots

---

## Reproducibility

✅ NS-3 v3.30 ICSI (exact)  
✅ RNG seeds 0-9 fixed  
✅ All params in YAML  
✅ Hardware documented  
**Description:** [Quick summary]  
**Example:** "Static network baseline — 50 nodes, no mobility, 3 replicates"

**Scenarios:**
- Scenario 001: Protocol A, nodes=50, mobility=static, seed=42
- Scenario 002: Protocol B, nodes=50, mobility=static, seed=42
- Scenario 003: Protocol A, nodes=50, mobility=static, seed=43 (replicate)
- Scenario 004: Protocol B, nodes=50, mobility=static, seed=43 (replicate)
- Scenario 005: Protocol A, nodes=50, mobility=static, seed=44 (replicate)
- Scenario 006: Protocol B, nodes=50, mobility=static, seed=44 (replicate)

**Total Scenarios:** 6  
**Status:** ✅ COMPLETE  
**Output Location:** `./experiments/batch_001/scenario_*/`  
**Random Seeds:** 42, 43, 44 (3 replicates)  
**Total Duration:** 15 minutes  
**Files Generated:**
- scenario_001/protocol_aodv_results.csv
- scenario_001/protocol_rpl_results.csv
- scenario_001/simulation.log
- scenario_001/metadata.json
- [repeats for scenarios 002-006]

**Notes:**
- ✅ All scenarios completed successfully
- ✅ No crashes or hangs
- ✅ Raw data validated (non-empty files, correct columns)
- ⚠️ Scenario 004 took 2m45s (slower than expected) — check log

---

## Batch 02: [Describe]

**Date:** [When?]  
**Description:** [Quick summary]  
**Example:** "Random waypoint mobility — 50 nodes, speed 5 m/s, 2 replicates"

**Scenarios:**
[List scenarios as above]

**Total Scenarios:** [N]  
**Status:** ⏳ IN PROGRESS or ✅ or ❌  
**Output Location:** `./experiments/batch_002/scenario_*/`  
**Random Seeds:** [...]  
**Total Duration:** [or "still running"]  
**Files Generated:**
- [List expected output files]

**Notes:**
- [Any issues?]
- [Warnings?]
- [Observations?]

---

## Batch 03: [Describe]

[Repeat pattern]

---

## Batch XX: [Continue as needed]

---

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Batches | [N] |
| Total Scenarios | [N] |
| Completed Scenarios | [N] |
| Failed Scenarios | [0] |
| Average Duration per Scenario | [X minutes] |
| Total Experimental Time | [X hours] |
| Unique Random Seeds Used | [N] |

---

## Aggregated Results

Once you've run all batches, summarize here:

- **Protocol A — Latency:**
  - Mean ± Std: [TBD ms]
  - Aggregate over all batches: [all scenarios]

- **Protocol B — Latency:**
  - Mean ± Std: [TBD ms]
  - Aggregate over all batches: [all scenarios]

- **Protocol A — PDR:**
  - Mean ± Std: [TBD %]

- **Protocol B — PDR:**
  - Mean ± Std: [TBD %]

[Add other metrics]

---

## How to Use This Log

1. **Before Running Batch:** Add entry with description
2. **After Running Batch:** Update status, location, duration, notes
3. **During Analysis (Cap 4):** This log helps you find which results to load
4. **For Paper:** You can cite batches: "We ran 3 batches (18 scenarios total)"
5. **For Reproducibility:** Anyone reading this log can replicate your experiments

---

## Reproducibility Checklist

For each batch, verify:
- [ ] Config YAML saved with results
- [ ] Random seed(s) documented
- [ ] Output files non-empty and well-formed
- [ ] Simulation logs capture any errors
- [ ] Metadata JSON created for each scenario
- [ ] Total duration reasonable (no hangs/crashes)

---

## Next Steps

1. Update this log as you complete each batch (Capability 3)
2. Use log output locations in Capability 4 (analysis scripts)
3. Mention batches in Methods section of paper
4. Archive this log in final paper repository

---

**Status:** Ready to run Capability 3 (Run Simulation)?
