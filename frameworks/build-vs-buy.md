# Build vs. Buy Decision Framework

## Evaluation Dimensions

Score each dimension 1-5 for both the Build and Buy option.

### 1. Total Cost of Ownership (TCO) — 3-year view
- **Build**: Development cost + infrastructure + ongoing maintenance + opportunity cost of engineers
- **Buy**: License/subscription + implementation + customization + integration + switching cost
- Don't forget: Build costs are almost always underestimated by 2-3x. Buy costs hide in integration and customization.

### 2. Time to Value
- How fast do we need this?
- Build: typically 6-18 months to production-ready
- Buy: typically 2-6 months including integration
- **If time-to-value is critical and a commercial solution exists, default to buy.**

### 3. Strategic Control
- Is this a core differentiator or commodity capability?
- **Core differentiator** (what makes you win): lean toward build
- **Commodity** (everyone needs it, not a competitive edge): lean toward buy
- Ask: "Would a competitor using the same vendor tool eliminate our advantage?" If no, it's commodity.

### 4. Team Capability
- Do we have the skills to build and maintain this?
- Can we hire/retain the talent needed?
- Will building this grow capabilities we want long-term, or distract from higher-value work?

### 5. Vendor Risk
- Is the vendor financially stable? Will they exist in 3 years?
- How locked in will we be? What's the exit cost?
- Do they have a roadmap aligned with our needs?
- How many of their customers look like us?

## Decision Tree

```
Is this a core differentiator?
├── YES → Do we have the team to build it?
│   ├── YES → Can we build it in a reasonable timeframe?
│   │   ├── YES → BUILD
│   │   └── NO → PARTNER (co-develop or build on a platform)
│   └── NO → Can we hire the team?
│       ├── YES (and worth it) → BUILD
│       └── NO → BUY + invest in understanding it deeply
└── NO → Does a commercial solution exist that fits >70% of needs?
    ├── YES → BUY
    └── NO → Is this worth building at all?
        ├── YES → BUILD minimal, don't over-engineer
        └── NO → DON'T DO IT
```

## The Partner Option

Often overlooked. Consider partnering when:
- You need strategic control but lack capability to build from scratch
- A vendor has a strong platform but you need significant customization
- You want to co-develop with a vendor who values your use case
- Time-to-value matters but so does long-term differentiation

## Common Mistakes

### Building What You Should Buy
- **"We can build it better"**: Maybe, but should you? Every hour your team builds commodity tooling is an hour not spent on differentiation.
- **"It's cheaper to build"**: Only if you ignore maintenance, on-call, documentation, onboarding, and opportunity cost.
- **"We need full control"**: Of what, exactly? Most teams overestimate their need for customization.

### Buying What Doesn't Fit
- **"It checks all the boxes"**: Demo-ware is not production-ware. Run a real POC with your data.
- **"Everyone uses it"**: "Everyone" may not have your scale, data complexity, or integration needs.
- **"The vendor will customize it for us"**: Customization turns a product into a project. You lose upgrade paths.
- **"We'll adapt our process to the tool"**: Sometimes valid, often a recipe for low adoption.

### Failing to Decide
- **Endless evaluation cycles**: Set a decision deadline. 80% confidence is enough — waiting for 100% is a decision to do nothing.
- **Pilot purgatory**: "Let's pilot three tools for 6 months" — pilot ONE, with clear success criteria and a kill date.

## Evaluation Scorecard

| Dimension | Weight | Build Score (1-5) | Buy Score (1-5) | Build Weighted | Buy Weighted |
|-----------|--------|-------------------|-----------------|----------------|--------------|
| TCO (3-yr) | ___ | | | | |
| Time to Value | ___ | | | | |
| Strategic Control | ___ | | | | |
| Team Capability | ___ | | | | |
| Vendor Risk | ___ | | | | |
| **Total** | | | | | |

Weights should sum to 100. Adjust weights based on your context — there's no universal formula.

## Red Flags

**Don't build if**: Your team is already stretched, the problem is well-solved commercially, or you can't commit to maintaining it for 3+ years.

**Don't buy if**: No vendor fits >50% of your needs, vendor lock-in threatens your strategy, or the integration cost exceeds the build cost.

**Revisit the decision annually**: Markets change, teams grow, vendors pivot. What was right to buy last year might be right to build now.
