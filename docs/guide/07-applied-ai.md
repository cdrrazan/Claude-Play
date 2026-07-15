# 7. Applied-AI addendum

If your project *uses* an LLM (an agent, a RAG pipeline, a classifier, a chatbot) — not just an LLM that
helps you build it — these four rules apply on top of everything else.

## Deterministic core; LLM narrates at the boundary

> Principle 13: **deterministic core; the LLM narrates at the boundary, never computes alone.**

The logic that *matters* — pricing, permissions, state transitions, anything with a right answer — lives
in **deterministic, testable code.** The LLM sits at the *edge*: it turns messy input into structured
calls to that core, and turns structured results into prose. It never does the arithmetic that a function
should do, because you can't unit-test a vibe.

This is what keeps an LLM app debuggable. When something's wrong, you can point at a function and a test —
not at a prompt and a shrug.

## Model-agnostic plumbing

> Principle 11: **one canonical value per concept; one choke point per external dependency.**

Route every model call through **one** client/adapter. When you switch models — and you will — you change
one file, not fifty. The model is a swappable part, not a foundation.

## Evals are the durable asset

> Principle 14: **evals are the durable asset; prompts and models are consumables.**

Prompts get rewritten. Models get deprecated. The thing that *lasts* is your **eval harness** — the set of
cases that tell you whether the system still works. This matches the emerging discipline of
[eval-driven development](https://evaldriven.org/): treat evals like tests for probabilistic systems.

**Grow the harness from real failures.** Don't try to write a comprehensive eval suite up front — you'll
guess wrong about what breaks. Every time production surprises you, add that case to `evals/`. The harness
that grows from actual failures is the one that catches the next one. (See [`evals/`](../../evals/).)

## Measure what the system acts on

> Principle 7: **measure what the system actually acts on, not the population.**

If your agent only escalates 5% of tickets, your accuracy number has to be about *that 5%*, not the whole
population where "do nothing" is trivially 95% right. Track experiments at the **application boundary** —
where a decision actually changes behavior — not buried in the engine where the metric flatters you.

→ Next: [Adoption & interop](08-adoption.md)
