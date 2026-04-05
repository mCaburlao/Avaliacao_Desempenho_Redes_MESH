# Paper Outline Template

**Working Title:** [Your Paper Title]  
**Target Venue:** [Journal/Conference]  
**Status:** OUTLINE | DRAFT | REVISION | FINAL  

---

## I. Introduction

### Hook
[Opening: Why this matters? What's the problem?]

### Background
[Brief explanation of MESH networks and chosen protocols]

### Problem Statement
[What's not known? What gap does this study fill?]

### Contribution(s)
[What's novel? What does reader learn from your work?]

### Paper Organization
"The rest of this paper is organized as follows: Section 2 covers related work.
Section 3 describes our simulation methodology. Section 4 presents results.
Section 5 discusses implications. Section 6 concludes."

---

## II. Related Work

### Existing Comparisons
[Review: what comparisons have been done?]
- Reference: [Citation]
- Reference: [Citation]

### Protocol Overviews

#### Protocol A: [Name]
- Overview: [Summary]
- Key characteristics: [...]
- References: [RFC or papers]

#### Protocol B: [Name]
- Overview: [Summary]
- Key characteristics: [...]
- References: [RFC or papers]

### Research Gap
[Why is THIS specific comparison needed?]

---

## III. Methodology

### Simulator Choice: [e.g., ns-3]
- Justification: [Why this tool?]
- Configuration: [Link to config files]

### Scenarios
[Detailed scenarios from Capability 1]

- **Scenario 1:** [Description + parameters]
- **Scenario 2:** [Description + parameters]
- **Scenario 3:** [Description + parameters]

### Metrics
[From your PRD/Comparative Matrix]

| Metric | Definition | Why measured? |
|--------|-----------|---------------|
| Latency P50 | Median packet delay | Application needs predictability |
| PDR | Packet Delivery Ratio | Network reliability |
| Overhead | % control traffic | Energy consumption in IoT |

### Experimental Design
- Number of runs: [N]
- Random seed: [Fixed value for reproducibility]
- Confidence level: [95%]
- Statistical tests: [e.g., t-test, Mann-Whitney U]

### Reproducibility
✅ All code and config available at [repo URL]  
✅ Raw data at [data repository]  
✅ Analysis scripts included  

---

## IV. Results

### Overall Findings
[Summary paragraph: what did you find?]

### Result 1: Latency Comparison
[Paragraph + Figure/Table]

| Protocol | P50 (ms) | P95 (ms) | P99 (ms) | IC 95% |
|----------|---------|---------|---------|--------|
| A | TBD | TBD | TBD | TBD |
| B | TBD | TBD | TBD | TBD |

**Figure 1:** Latency distribution (box plot or CDF)

### Result 2: Reliability (PDR)
[Paragraph + Figure/Table]

### Result 3: Overhead
[Paragraph + Figure/Table]

### Result 4: Convergence
[Paragraph + Figure/Table]

[Add more subsections as needed]

---

## V. Discussion

### Analysis
[Interpret results: why is Protocol A faster? Why is B more efficient?]

### Tradeoffs
[No protocol wins everywhere. Explain the tradeoffs to reader.]

**Example:**
"AODV achieves 29% lower latency (p<0.001) due to its reactive approach,
which discovers routes on-demand. However, RPL maintains more stable routes
with 15% lower overhead variance, making it more suitable for duty-cycled devices."

### Practical Implications
[What should practitioners do with this information?]

**Example:**
"For time-sensitive applications (emergency communications), AODV is preferred.
For battery-constrained networks (IoT sensors), RPL's predictable overhead is advantageous."

### Limitations
[What could be done better? Future work?]

- Simulator assumptions (idealized radio model)
- Limited to 50 nodes; unclear how results scale
- Fixed mobility model; real patterns may differ

### Threats to Validity
[Are there confounds? Biases?]

---

## VI. Conclusion

### Summary
[Recap findings in 3-4 sentences]

### Contributions
[Restate what readers learned]

### Future Work
[Natural next steps]

---

## VII. References

[Complete bibliography in IEEE or ABNT format]

1. [RFC 3561] Perkins, C. E., et al. "Ad hoc On-Demand Distance Vector..."
2. [RFC 6550] Winter, T., et al. "RPL: IPv6 Routing Protocol for Low-Power..."
3. [Your Related Work]
...

---

## VIII. Appendices (if needed)

### A. Simulator Configuration (YAML)
[Include config file content]

### B. Raw Data Collection Scripts
[Include Python scripts]

### C. Statistical Test Details
[If complex, explain methodology]

---

## Writing Notes

- **Audience:** Researchers in networking. Assume they know IP; explain MESH concepts clearly.
- **Tone:** Professional, objective. Avoid overselling results.
- **Tense:** Past tense for methods/results ("We implemented..."; "Results showed..."). Present/future for implications ("This suggests...").
- **Figures:** All labeled, captioned. All cited in text.
- **Tables:** Same as figures — caption above, not below.

---

## Submission Checklist

- [ ] All figures have captions
- [ ] All tables cited in text
- [ ] References formatted consistently
- [ ] No orphaned paragraphs (review paragraph flow)
- [ ] Reproducibility: code and data publicly available
- [ ] Threat to validity section included
- [ ] Page limit met (if applicable)

---

**Status:** Ready for editing? Review all sections and replace [TBD] with actual content as Capabilities complete.
