# Falsified Ideas Ledger

Ideas we **tried and killed**. This is the piece no other framework has: a committed record of what
*doesn't* work, so no agent (or human) re-runs a dead experiment.

**The rule:** a tweak of a dead idea is the same idea. Before you propose something, check this list. To
resurrect a killed idea you must bring *new evidence* that addresses the mechanism of failure below — not
just a small variation.

Every entry needs the **mechanism** of failure and the **numbers**. "It was slow" is not an entry;
"p99 latency 2.3s vs 400ms budget because each call re-tokenizes the full prompt" is.

| Idea | Verdict | Why (mechanism + numbers) | Date |
|------|---------|---------------------------|------|
| _e.g._ Cache embeddings in Redis | killed | Cache hit rate 4% — inputs are near-unique per request; added 40ms lookup for no benefit | 2026-07-12 |
| _e.g._ Retry failed LLM calls 5× | killed | Failures were deterministic (bad schema), not transient — retries just 5×'d cost, 0% recovery | 2026-07-13 |

<!--
Add new rows at the bottom. Keep killed ideas forever — the ledger's value is that it never forgets.
If a killed idea is later revived with new evidence, don't delete the row: add a decisions.md entry
that cites this row and explains what new evidence reopened it.
-->
