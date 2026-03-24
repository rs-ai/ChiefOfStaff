# AI Eval Framework

> Evals are not a separate activity. They're embedded at every stage of the deployment lifecycle.
> No eval = deployment not complete.

## Three Layers

### Layer 1: Solution Evals (Does the AI work?)

| Eval | What It Measures | When | Example |
|------|-----------------|------|---------|
| **Accuracy** | Correct outputs vs. known answers | Before deploy + ongoing | Customer inquiry routed correctly 92% |
| **Hallucination rate** | Making things up? | Before deploy + ongoing | Knowledge base returns verified sources |
| **Edge case handling** | Unusual inputs | Before deploy | Edge case input handled gracefully |
| **Latency** | Fast enough? | Before deploy + ongoing | Response under 3 seconds |
| **Cost per interaction** | Affordable at scale? | Ongoing | $0.04 vs. $5.50 human |

**Test set:** During Build, create 20-50 real examples with known correct answers. This IS your eval set. Save it in the library.

### Layer 2: Adoption Evals (Are people using it?)

| Eval | What It Measures | When | Example |
|------|-----------------|------|---------|
| **Active usage rate** | % of target users using weekly | Weekly from launch | 45/60 target users = 75% |
| **Repeat usage** | Do they come back? | Weekly | Flat = problem |
| **Workflow integration** | In the flow or side tool? | Monthly | Separate app = risk |
| **User sentiment** | Do they trust it? | Monthly | Thumbs up/down |
| **Support tickets** | What's breaking? | Ongoing | Volume declining = stable |

**The 70% rule:** Target >70% of intended users actively using within 8 weeks. If adoption flatlines, diagnose immediately.

### Layer 3: Business Impact Evals (Was it worth it?)

| Eval | What It Measures | When | Example |
|------|-----------------|------|---------|
| **Time saved** | Before vs. after | Monthly | 12 min → 2 min |
| **Quality improvement** | Error rate change | Monthly | Routing errors down 30% |
| **Cost impact** | $ saved or generated | Quarterly | 400 hours/month saved |
| **Customer impact** | NPS, complaints, resolution | Quarterly | Complaints down 15% |

## Where Evals Sit in the Deployment Lifecycle

| Deployment Stage | Eval Activity |
|-----------------|---------------|
| **1. Discovery** | Capture baseline metrics. No baseline = no proof later. |
| **2. Assessment** | Include "measurability" in go/no-go. If you can't measure it, don't build it. |
| **3. Scoping** | Implementation team identifies test data. Business stakeholder defines "good enough" threshold. |
| **4. Build** | Create test set. Run eval. Iterate until threshold met. |
| **5. Rollout** | Launch live dashboard. Weekly adoption check. |
| **6. Handoff** | Save eval set + baseline + results in library. |

## Mandatory Eval Template (Per Deployment)

```
## Eval Record: [Use Case Name]

### Baseline (captured during Discovery)
- Current time per task: ___
- Current error rate: ___
- Current cost per task: ___
- Sample size: ___

### Test Set (captured during Build)
- Number of test cases: ___
- Accuracy on test set: ___%
- Known failure modes: ___
- Acceptable accuracy threshold: ___%
- Test set location: [link in library]

### Live Metrics (tracked during Rollout)
- Active users / target users: ___ / ___
- Weekly usage trend: ↑ ↓ →
- User sentiment (thumbs up %): ___%
- Avg time per task (after): ___
- Top 3 failure modes observed: ___

### Business Impact (reviewed quarterly)
- Time saved per month: ___ hours
- Quality improvement: ___%
- Cost impact: $___
- Customer impact: ___

### Eval Verdict
- [ ] Solution meets accuracy threshold
- [ ] Adoption >70% of target users
- [ ] Measurable business impact demonstrated
- [ ] Eval set saved in library for reuse
```

## Getting Expert Help

- **Cloud AI platforms** — most major cloud providers offer built-in evaluator catalogs with pre-built eval templates (e.g., Azure AI Foundry, AWS Bedrock, Google Vertex AI)
- **Open source** — RAGAS (RAG evals), DeepEval, Promptfoo (prompt testing)
- **LLM-as-judge** — use one AI to evaluate another's outputs at scale
- **External consultants** — major management consulting firms often have specialized AI evaluation practices
