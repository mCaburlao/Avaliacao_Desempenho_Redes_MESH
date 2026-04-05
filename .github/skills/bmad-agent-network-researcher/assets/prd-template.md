# PRD Template: MESH Network Protocol Comparison Study

**Document ID:** PRD-{YYYYMMDD}-001  
**Author:** [Your Name]  
**Date:** [Current Date]  
**Status:** DRAFT | FINAL | APPROVED  

---

## 1. Executive Summary

[What is the core research question? Why does it matter?]

**Example:** 
"This study compares AODV and RPL protocols in disaster recovery networks.
Hypothesis: AODV maintains lower latency; RPL provides faster convergence.
Significance: First comparative analysis in this specific scenario."

---

## 2. Problem Statement

### 2.1 Business Context
[Real-world application. Not theoretical.]

- **Application Domain:** [e.g., disaster networks, IoT, mobile ad-hoc]
- **Stakeholders:** [Who needs this research?]
- **Critical Constraints:** [Latency budget? Reliability target?]

### 2.2 Current State
[What's known? What gap exists?]

- **Existing Research:** [Citations to prior comparisons]
- **Gap:** [What's NOT been studied?]

### 2.3 Scientific Hypothesis
[Your core claim.]

---

## 3. Protocols Under Study

### Protocol A: [Name]
- **Citation:** [RFC or paper]
- **Category:** [Reactive/Proactive/Hybrid]
- **Why:** [Why compare this one?]
- **Expected Strengths:** [...]
- **Expected Weaknesses:** [...]

### Protocol B: [Name]
- **Citation:** [RFC or paper]
- **Category:** [Reactive/Proactive/Hybrid]
- **Why:** [Why compare this one?]
- **Expected Strengths:** [...]
- **Expected Weaknesses:** [...]

---

## 4. Experimental Scenarios

### Scenario 1: [Name]
- **Topology:** [nodes, structure]
- **Mobility Model:** [static, random waypoint, gauss-markov]
- **Traffic Pattern:** [CBR, bursty, realistic]
- **Duration:** [time]

### Scenario 2: [Name]
[...]

### Scenario 3: [Name]
[...]

---

## 5. Metrics & Success Criteria

| Metric | Definition | Unit | Target | Priority |
|--------|-----------|------|--------|----------|
| Latency (P50) | Median packet delay | ms | <100 | HIGH |
| Latency (P95) | 95th percentile | ms | <200 | HIGH |
| PDR | Packet Delivery Ratio | % | >95% | HIGH |
| Overhead | Routing control traffic | % of total | <20% | MEDIUM |
| Convergence | Time to find path | seconds | <5 | MEDIUM |

---

## 6. Reproducibility Commitment

✅ Published simulator code  
✅ Fixed random seeds  
✅ Configuration files in git  
✅ Raw data available  
✅ Analysis scripts reproducible  

---

## 7. References

[List all protocols, related work, tools you'll use]

---

**Status:** READY FOR CAPABILITY 2 (Setup Simulator)?
