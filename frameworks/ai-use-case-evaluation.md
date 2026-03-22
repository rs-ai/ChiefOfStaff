# AI Use Case Evaluation Framework

## Evaluation Dimensions

Rate each dimension **High / Medium / Low** for every proposed use case.

### 1. Business Value
- **High**: Directly impacts revenue, cost savings >$1M/yr, or regulatory requirement
- **Medium**: Improves efficiency, moderate cost savings, competitive advantage
- **Low**: Nice-to-have, unclear ROI, internal convenience only

### 2. Technical Feasibility
- **High**: Proven approach, existing models/tools, team has done similar work
- **Medium**: Requires some R&D, known techniques but new to the team
- **Low**: Research-grade, no proven approach, novel problem space

### 3. Data Readiness
- **High**: Clean, labeled, accessible data exists today; pipelines in place
- **Medium**: Data exists but needs cleaning, joining, or labeling effort
- **Low**: Data doesn't exist, is siloed, or has serious quality/governance issues

### 4. Organizational Readiness
- **High**: Executive sponsor, end-users are asking for it, change management plan exists
- **Medium**: Sponsor exists but end-users are skeptical; no change plan yet
- **Low**: No sponsor, active resistance, or competing priorities block adoption

### 5. Implementation Risk
- **High risk**: Safety-critical, regulatory exposure, high-visibility failure mode
- **Medium risk**: Moderate impact if wrong, recoverable errors, internal-facing
- **Low risk**: Low-stakes decisions, human-in-the-loop, easy to roll back

## Decision Matrix

| Business Value | Tech Feasibility | Data Ready | Org Ready | Decision |
|---------------|-----------------|------------|-----------|----------|
| High | High | High | High | **Proceed to production** |
| High | High | High | Med/Low | **Proceed but invest in change mgmt** |
| High | Med | Med+ | Med+ | **Pilot with defined success criteria** |
| High | Low | Any | Any | **R&D spike — time-box 4 weeks** |
| Med | High | High | High | **Proceed if capacity allows** |
| Med | Med | Med | Med | **Pilot only if strategic** |
| Low | Any | Any | Any | **Kill — don't waste cycles** |

## Pre-Evaluation Checklist

Before scoring, answer these:

1. **Who is the end user?** (Not the sponsor — the person whose workflow changes)
2. **What do they do today without AI?** (Baseline matters)
3. **What does "good enough" look like?** (Perfect is the enemy of deployed)
4. **Who owns this after launch?** (If nobody, it's dead on arrival)
5. **What happens when the model is wrong?** (Error cost defines risk tolerance)

## Common Pitfalls

- **Solution looking for a problem**: Start with the business pain, not the technology
- **Overweighting technical feasibility**: A technically brilliant model nobody uses is worthless
- **Ignoring end-user adoption**: Deployment, UX, and workflow integration are where most projects die
- **Confusing a demo with a product**: A Jupyter notebook is not production-ready
- **No baseline measurement**: If you can't measure current performance, you can't prove AI improved it
- **Scope creep via "while we're at it"**: Each use case gets its own evaluation — no bundling

## Quick Kill Signals

Stop immediately if any of these are true:
- No identifiable end user who will change their behavior
- The data doesn't exist and creating it takes >6 months
- The error cost is high but there's no human-in-the-loop design
- The executive sponsor leaves and nobody picks it up
- The team can't articulate the business metric that will move
