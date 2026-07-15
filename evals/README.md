# evals — the durable asset

For projects that **use** an LLM. Prompts and models are consumables; **evals are what lasts** (principle
14). This folder is your test suite for a probabilistic system.

## How to grow it (don't build it all up front)

You will guess wrong about what breaks. So don't try to write a comprehensive suite before you ship.
Instead:

1. Ship with a **handful** of cases covering the core happy path.
2. **Every time production surprises you**, add that exact case here. A failure that made it to production
   is the most valuable eval you can have — it's a real bug the suite didn't catch.
3. Track results at the **application boundary** — where a decision changes behavior — not deep in the
   engine where the metric flatters you (principle 7).

## Suggested layout

```
evals/
├── cases/            # one file (or row) per case: input + expected/asserted behavior
├── run.<ext>         # the harness that runs cases against the current prompt+model
└── results/          # optional: recorded runs, so regressions are visible
```

Keep the harness **model-agnostic** — it calls your one model choke point (principle 11), so swapping
models is a one-line change and the evals still run.

> Growth folder, not kernel. Only relevant if your product uses an LLM at runtime. Delete this README
> once you add your first real eval.
