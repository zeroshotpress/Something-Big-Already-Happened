# Voice & Style Guide

> Writing rules for all chapter content.
> See MASTER-PLAN.md §8 for authoritative rules.

## Tone

Authoritative but accessible. Like a well-researched longform journalism piece (think: Michael Lewis, John Carreyrou, or a deep-dive New Yorker feature).

## Banned AI-Voice Words

These words betray AI-generated prose. **Zero tolerance.**

```
delve, moreover, furthermore, it is worth noting, it is important to consider,
robust, comprehensive, crucial, landscape, navigate, leverage, multifaceted,
tapestry, serves as a testament, in the ever-evolving, pivotal, underscore,
nuanced, paradigm shift, at the heart of, in an era where, vibrant
```

## Banned Patterns

These formulaic patterns may appear at most **2 times per chapter**:

```
"X was not merely Y. It was Z."
"The implication was stark/sharp/clear."
"This was not X. This was Y."
```

## Burstiness

Sentence-length standard deviation must be **> 8**. This means mixing:
- Very short sentences (3-5 words)
- Medium sentences (10-20 words)
- Long, complex sentences (30+ words)

Monotonous sentence length is the hallmark of AI prose.

## Required Techniques

- **Contractions**: Use them. "It's" not "it is." "Didn't" not "did not."
- **Incomplete sentences**: Permitted. Encouraged, even.
- **Expansion via scenes**: When a chapter needs more words, add human scenes, vignettes, and practical tool descriptions. **Never** add more analysis.

## Quote Hygiene

- Direct quotes (blockquote): **max 25 words each**
- Same source: **max 200 words total** across all chapters
- Shumer essay: **2-3 direct quotes only**, everything else paraphrased

## Chapter Structure (6-Stage Blueprint)

Every chapter follows this structure:

1. **Cold Open Scene** (300-600 words): Date + place + person + one sensory detail
2. **Claim** (1-2 sentences): The chapter's thesis
3. **Evidence** (70-75% of chapter): Data, charts, expert testimony
4. **Counterpoint** (200-400 words): "Why this might be wrong" + 1-2 falsification conditions
5. **Prediction Scorecard + So-What Tool** (300-500 words)
6. **Closing Hook** (1-2 paragraphs): Bridge to next chapter

## Enforcement

`scripts/voice_audit.py` checks banned words, patterns, and burstiness. Must EXIT 0.
`scripts/quote_audit.py` checks quote lengths and per-source totals. Must EXIT 0.
