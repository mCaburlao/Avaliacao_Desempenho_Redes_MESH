# Paper Outline — IEEE Format 6-10 Pages SBC

**Working Title:** \"Uma Análise Competitiva de AODV e OLSR em Redes MESH Escaláveis\"  
**Target Venue:** IEEE Transactions on Mobile Computing / Computer Networks  
**Status:** ✅ DESIGN COMPLETE | 🔄 READY FOR WRITING  
**Format:** SBC Scientific Article Template (Portuguese)

---

## Paper Structure (7 Sections)

### **1. TÍTULO & RESUMO** — Weight 1

**Key Elements:**
- Comparing AODV (reactive) vs OLSR (proactive)
- Scaling behavior 100-1500 nós
- MESH networks + Smart cities application

**Abstract (250-300 words):**
```
What? Benchmark AODV vs OLSR (100-1500 nodes)
Why? Smart cities need data-driven protocol choice
How? MeshSim simulation, 140 runs, IC 95%
Results? Crossover ~750 nós, overhead linear vs quadratic
Contribution? Modern benchmark + quantified recommendations
```

**Keywords:** AODV, OLSR, Routing, Mesh Networks, IoT, Scalability, NS-3

---

### **2. INTRODUÇÃO** — Weight 2 (MANDATORY)

**Structure:**
1. Context: MESH networks foundation for IoT/smart cities
2. Problem: Engineers unsure which protocol at scale
3. Gap: Benchmarks outdated, lack 100-1500 data
4. Objective: Fill gap with modern rigorous analysis
5. Organization: Sections roadmap

**Page Target:** 1-1.5 pages  
**Template:** See GUIA_CONSTRUCAO_TRABALHO_ADR.md (Seção 2)

---

### **3. EXPLICAÇÃO DO PROBLEMA** — Weight 1 (MANDATORY)

**Subsections:**
- 3.1 Contexto Teórico (AODV vs OLSR algorithms)
- 3.2 Problema Prático (Real-world cases)
- 3.3 Lacuna Literária (What's missing)
- 3.4 Justificativa (Scientific + practical + learning)

**Page Target:** 0.75-1 page  
**Template:** See GUIA_CONSTRUCAO_TRABALHO_ADR.md (Seção 3)

---

### **4. TRABALHOS RELACIONADOS** — Weight 1 (MANDATORY)

**References:**
- RFC 3561/3626 (AODV/OLSR specs)
- Lee et al. 2015 (benchmark 500 nós)
- Passo et al. 2018 (NS-3 analysis)

**Differentiation:** Your work = 100-1500 nós + NS-3 v3.30 + IC 95%

**Page Target:** 0.75-1 page  
**Bibliography:** >10 Qualis references

---

### **5. EXPLICAÇÃO DAS 2 SOLUÇÕES** — Weight 1 (MANDATORY)

**5.1 AODV Details:**
- Algorithms, overhead LINEAR, MeshSim config

**5.2 OLSR Details:**
- Algorithms, overhead QUADRATIC, MeshSim config

**5.3 Comparison Table:**
- All key aspects, winner per scale

**Page Target:** 1-1.5 pages  
**Template:** See GUIA_CONSTRUCAO_TRABALHO_ADR.md (Seção 5)

---

### **6. ANÁLISE DOS RESULTADOS** — Weight 2 (MANDATORY)

**6.1 Design:** Variables, metrics, params  
**6.2 Results:**
- Figure 1: Overhead vs Nodes (CRITICAL - crossover!)
- Figure 2: PDR vs Nodes
- Figure 3: Latency vs Nodes
- Table 1: Raw data
- Table 2: Statistics (mean ± IC 95%)

**6.3 Statistical Analysis:**
- Confidence intervals, hypothesis tests, p-values

**6.4 Discussion:**
- Mechanisms explained, implications for smart cities

**Page Target:** 2-2.5 pages  
**Template:** See GUIA_CONSTRUCAO_TRABALHO_ADR.md (Seção 6)

---

### **7. CONCLUSÕES & TRABALHOS FUTUROS** — Weight 1 (MANDATORY)

**3 Mandatory Paragraphs:**
1. Recap: Research question recap
2. General: Key findings + recommendations by scale
3. Future: Energy, RPL, adaptive switching, etc.

**Page Target:** 0.5-1 page  
**Template:** See GUIA_CONSTRUCAO_TRABALHO_ADR.md (Seção 7)

---

## Formatting (Weight 1 + 2 Writing)

**SBC Template:** Times New Roman 12pt, 2cm margins, 1.5 spacing  
**Page Limit:** 6-10 A4 pages total  
**Writing:** Clarity, conciseness, direct order, Portuguese norma culta

---

## Figures & Tables Strategy

| # | Content | Critical? |
|:---|:---|:---|
| Figure 1 | Overhead vs Nodes (crossover) | ✅ YES |
| Figure 2 | PDR vs Nodes (degradation) | ✅ YES |
| Figure 3 | Latency vs Nodes | ✅ YES |
| Table 1 | Raw results all configs | ✅ YES |
| Table 2 | Statistics IC 95% | ✅ YES |

**All figures must have:**
- Error bars: ±IC 95%
- High DPI (>300)
- Descriptive captions
- Axis labels with units

**Status:** [NOT STARTED | DRAFT | COMPLETE]

### Prior Comparisons
[What comparisons exist? What's missing?]

### Protocol Overviews
[Summary of AODV and RPL]

### Research Gap
[Why THIS comparison is needed]

---

## III. Methodology

**Status:** [NOT STARTED | DRAFT | COMPLETE]

### Simulator
Choice: [ns-3 | OMNET++ | Other]
Justification: [...]

### Scenarios
[From business-domain.md]
- Scenario 1: [...]
- Scenario 2: [...]
- Scenario 3: [...]

### Metrics
[From comparative-matrix.md]

### Statistical Methods
- Confidence level: 95%
- Normality test: [...]
- Statistical tests: [...]
- Effect size reporting: [Yes/No]

### Reproducibility
- Code: [GitHub link]
- Data: [Data repository link]
- Configs: [Versioned in git]

---

## IV. Results

**Status:** [NOT STARTED | COLLECTING DATA | DRAFT | COMPLETE]

### Latency Analysis
[After simulation + analysis]

**Table [X]:** Results
**Figure [Y]:** Visualization

### PDR Analysis
[After simulation + analysis]

**Table:** PDR by scenario
**Figure:** PDR comparison

### Overhead Analysis
[After simulation + analysis]

**Table:** Overhead metrics
**Figure:** Overhead trends

### [Add more subsections as needed]

---

## V. Discussion

**Status:** [NOT STARTED | DRAFT | COMPLETE]

### Finding Interpretation
[What do your results MEAN?]

### Tradeoffs
[No winner everywhere — explain nuances]

### Practical Implications
[Practitioner guidance]

### Limitations
[What could be done better?]

### Threats to Validity
[Confounds? Biases?]

---

## VI. Conclusion

**Status:** [NOT STARTED | DRAFT | COMPLETE]

### Summary
[Recap findings]

### Contributions
[Restate novel aspects]

### Future Work
[Natural next steps]

---

## VII. References

**Status:** [NOT STARTED | COLLECTING | COMPLETE]

- [ ] RFC 3561 (AODV)
- [ ] RFC 6550 (RPL)
- [ ] Simulator docs
- [ ] Related work citations
- [ ] Tools/libraries

---

## Writing Progress

| Section | Status | % Complete | Notes |
|---------|--------|-----------|-------|
| I. Introduction | ⏳ | 0% | Waiting for findings |
| II. Related Work | ⏳ | 0% | Waiting for definition |
| III. Methodology | ⏳ | 50% | Simulator chosen? |
| IV. Results | ⏳ | 0% | Waiting for Capability 4 |
| V. Discussion | ⏳ | 0% | Waiting for analysis |
| VI. Conclusion | ⏳ | 0% | Last section |
| VII. References | 📝 | 30% | Collecting |

---

## Key Milestones

- [ ] **Cap 1 Complete:** Business domain + metrics locked
- [ ] **Cap 2 Complete:** Simulator architecture finalized
- [ ] **Cap 3 Complete:** Raw simulation data collected
- [ ] **Cap 4 Complete:** Statistical analysis done
- [ ] **First Draft:** All sections have content
- [ ] **Revision:** Peer review / self-edit
- [ ] **Final:** Ready to submit

---

## Styling Notes

- **Target Audience:** Networking researchers (assume they know IP, explain MESH/routing concepts clearly)
- **Tone:** Professional, objective, evidence-based
- **Tense:** Past (methods/results), Present (implications)
- **Figures:** ALL labeled, captioned, cited in text
- **Tables:** Caption above, not below
- **References:** IEEE or ABNT format (consistent)

---

## Document Links

- **Domain Context:** [See business-domain.md]
- **Metrics & Results:** [See comparative-matrix.md]
- **Experiment Log:** [See experiment-log.md]

---

**Readiness:** Can you write intro + background without simulation results? Yes → start writing. No → wait for Capability 3 data.
