# Executive Narrative Framework

## The "So What?" Rule

Every data point, chart, or finding must answer: **"So what? What should we do about it?"**

| Weak | Strong |
|------|--------|
| "Churn increased 12% last quarter" | "Churn increased 12% — concentrated in mid-market. Root cause is onboarding friction. Recommendation: deploy guided onboarding for mid-market by Q3, projected to recover $2.4M ARR" |
| "Model accuracy is 94%" | "Model accuracy hit 94%, above our 90% threshold — we're ready to move from pilot to production with Team X" |
| "We processed 2M records" | "We processed 2M records and identified 340 high-risk accounts requiring immediate review — here's the action plan" |

## Narrative Structure: SCR

Use **Situation - Complication - Resolution** for every executive communication.

### Situation (1-2 sentences)
Where are we? What's the context? Assume they forgot the last meeting.

### Complication (1-2 sentences)
What changed? What's the tension? Why does this need attention now?

### Resolution (the bulk of your time)
What do you recommend? What's the evidence? What do you need from them?

**Example:**
> **Situation**: We launched the demand forecasting pilot in the Northeast region 8 weeks ago, targeting a 15% reduction in overstock costs.
>
> **Complication**: The pilot exceeded targets (22% reduction) but revealed that our inventory data in the Southeast region has quality issues that would block expansion.
>
> **Resolution**: Recommend proceeding with Northeast production rollout (Q3) while running a 6-week data remediation sprint for Southeast. Investment needed: $180K for data engineering. Expected ROI: $3.2M annually once both regions are live.

## Anti-Patterns

### 1. The Dashboard Dump
Showing 15 charts and asking "any questions?" is not a narrative. Executives don't explore data — they need conclusions and recommendations.

**Fix**: Pick the 2-3 data points that support your narrative. Everything else is appendix.

### 2. Technical Jargon
"We fine-tuned a transformer model with RAG architecture achieving 0.92 F1 score" means nothing to a CFO.

**Fix**: Translate to business language. "The system correctly identifies 92% of at-risk contracts, up from the team's current 65% manual review accuracy."

### 3. Feature Lists
"We built real-time dashboards, automated ETL pipelines, and a self-service analytics portal" is not a story.

**Fix**: Lead with the outcome. "Sales managers can now see pipeline health in real-time, reducing forecast variance from 30% to 12%."

### 4. Burying the Lead
Spending 10 minutes on methodology before getting to results.

**Fix**: Lead with the conclusion. "We should invest $500K in X because it will return $3M. Here's why."

### 5. No Clear Ask
Presenting information without stating what you need from the audience.

**Fix**: End every presentation with a specific ask: approve, fund, decide, unblock.

## Templates

### Board Update (1 page max)

**Headline**: [One sentence: what happened and what it means]

**Key metrics**: [3-4 metrics with trend arrows, vs. target]

**Progress**: [2-3 bullet points on what shipped/delivered]

**Risks**: [1-2 risks with mitigation plans — never hide bad news]

**Next quarter**: [2-3 priorities with expected outcomes]

**Ask**: [What you need from the board, if anything]

### Investment Case (1-2 pages)

1. **Problem** (2 sentences): What business pain are we solving?
2. **Proposed solution** (3-4 sentences): What are we building/buying and why this approach?
3. **Expected impact**: Revenue/cost impact with assumptions stated
4. **Investment required**: Total cost, timeline, team needs
5. **Risks and mitigations**: Top 3 risks with specific mitigation plans
6. **Alternative considered**: What else we evaluated and why this option wins
7. **Ask**: Specific approval or decision needed, with deadline

### Quarterly Review Narrative

1. **One-line summary**: "Q[X] was [ahead/on track/behind] plan because [one reason]"
2. **Wins** (3 max): What delivered measurable impact?
3. **Misses** (be honest): What didn't land? Why? What changed?
4. **Key learning**: What do we now know that changes our approach?
5. **Next quarter focus**: Top 3 priorities ranked by impact
6. **Resource needs**: Any changes to team, budget, or timeline

## Principles

- **Executives are time-poor and context-poor**: They have 47 other things competing for attention. Earn your minutes.
- **Confidence is not arrogance**: State your recommendation clearly. "I believe we should..." not "maybe we could consider..."
- **Bad news travels better early**: A risk flagged early is leadership. A risk revealed late is a failure.
- **Numbers without narrative are noise**: Always pair data with interpretation and action.
- **Silence after your ask is powerful**: State what you need, then stop talking.
