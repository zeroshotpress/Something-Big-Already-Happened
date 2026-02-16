# Source Policy

> Governs how every claim in the book must be sourced.
> See MASTER-PLAN.md §6 for the authoritative rules.

## 2-Axis Classification

Every citation is classified on two axes:

### Axis 1: Tier (reliability)

| Tier | Definition | Examples |
|------|-----------|----------|
| **Tier-1** | Official sources, original research papers, government documents, top-tier journalism | OpenAI blog, Anthropic announcements, METR reports, Reuters, Bloomberg, WSJ, FT, Fortune, NYT, Science, Nature |
| **Tier-2** | Reputable tech press, think tanks, practitioner blogs | TechCrunch, The Information, Semafor, Stanford HAI, Simon Willison, Dan Shapiro |
| **Tier-3** | Wikipedia, SEO blogs, aggregators | Wikipedia, Medium, InvestorPlace, generic aggregator sites |

### Axis 2: Type (originality)

| Type | Definition |
|------|-----------|
| **Primary** | First-party data, direct quotes, original research, official announcements |
| **Secondary** | Reporting that directly cites/analyzes primary sources |
| **Tertiary** | Summaries, aggregations, encyclopedia entries |

## Rules

1. **Core claims** (numbers, dates, benchmarks, releases, valuations, policy, employment stats) require:
   - Tier-1 AND (Primary OR Secondary)

2. **Context** (background, framing, non-numerical claims):
   - Tier-2 acceptable
   - Primary practitioner sources acceptable

3. **Tier-3 in core claims**: **FORBIDDEN** (0 allowed)

4. **Paywalled sources**: If a core claim cites a paywalled source, a non-paywalled companion (official/government/original report) must be linked.

5. **Secondary source rule**: Only secondary sources that directly quote or cite the primary are acceptable.

## Registry

All citations should be registered in `/references/source-registry.yml` with their tier, type, and scope classification.

## Enforcement

`scripts/source_audit.py` automatically checks these rules. It must EXIT 0 for any release.
