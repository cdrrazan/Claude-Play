# The AI-Agent Playbook

**A clone-and-run starter kit for keeping a codebase trustworthy after thousands of AI-agent edits.**

AI coding agents are fast, but forgetful and overconfident. Over hundreds of changes they re-run dead
experiments, "helpfully" edit things you didn't ask about, and claim code works without reading it. That
quietly rots a codebase. This kit is the discipline that stops the rot — a small set of files and rules
you drop into any repo, new or old.

It is **not a framework you install** and not a code generator. It's a *reliability layer*: it assumes your
code is the source of truth and governs how agents are allowed to make claims about it. It sits happily
*underneath* generation tools like [spec-kit](https://github.com/github/spec-kit) or
[Kiro](https://kiro.dev) — use those to produce code, use this to keep it honest.

> Adapted and structured from the original *Project-Setup Playbook for AI-Agent-Assisted Projects*
> ([gist by subzekt](https://gist.github.com/subzekt/0dfced13befee2ff29f1a61bbbd7f072)). This repo turns
> that playbook into a usable, copy-pasteable kit. See [`docs/research/playbook-analysis.md`](docs/research/playbook-analysis.md)
> for how it compares to spec-kit, Kiro, AGENTS.md, and ADR practice.

---

## What you get

```
.
├── AGENTS.md              # canonical rules an agent reads before touching anything
├── CLAUDE.md              # stub that imports AGENTS.md (Claude Code reads this)
├── docs/
│   ├── decisions.md       # ledger of choices made — dated, with "revisit if"
│   ├── falsified.md       # ledger of ideas KILLED — the piece nothing else has
│   ├── ai/                # durable "why" reasoning (committed)
│   ├── plans/             # ephemeral implementation notes (deleted after use)
│   └── guide/             # the full guidebook, chapter by chapter
├── roles/                 # ready-to-paste prompts: coder · reviewer · auditor
├── templates/             # copy-paste ledger entries, decision record, spec stub
├── evals/                 # eval-harness scaffold (for LLM projects)
└── .claude/hooks/         # OPTIONAL hooks that turn the gates from advice into enforcement
```

## Quick start

**New project (greenfield):**
1. Copy `AGENTS.md`, `CLAUDE.md`, and `docs/decisions.md` + `docs/falsified.md` into your repo.
2. Fill in the *project map* section of `AGENTS.md` (stack, domain terms, how to run tests).
3. Start both ledgers **empty**. Add to them as you go — never backfill.
4. Add linting, a lockfile, and one passing test **now** if this is a code project.
5. Grow `docs/`, `roles/`, `evals/`, and hooks only when their absence first causes friction.

**Existing project (brownfield):**
1. Drop in `AGENTS.md` + the `CLAUDE.md` stub. Change no code.
2. Start `decisions.md` and `falsified.md` empty; fill *forward* from your next decision.
3. Introduce the **reviewer** role on your next PR; add the **auditor** once `falsified.md` has entries.
4. Adopt enforcement hooks last, once the team trusts the rules.

No big-bang migration. Everything here is additive.

## The one-paragraph philosophy

Start with a **minimal kernel** — an instruction file and the two ledgers — and *grow when it hurts.*
Keep a **deterministic core** and let the LLM narrate at the boundary, never compute alone. Separate the
agent that **writes** code from the one that **reviews** it and the one that **audits** it against dead
ideas. And never let a claim about code stand unless it traces to a fresh read.

## Read the guide

| Chapter | What it covers |
|---|---|
| [1. Why this exists](docs/guide/01-why.md) | The rot problem; where this sits vs. spec-kit/Kiro |
| [2. The 15 principles](docs/guide/02-principles.md) | The whole philosophy, one line each |
| [3. The minimal kernel](docs/guide/03-kernel.md) | The four files; greenfield vs. brownfield tracks |
| [4. The two ledgers](docs/guide/04-ledgers.md) | `falsified.md` + `decisions.md`, with upgraded formats |
| [5. The three roles](docs/guide/05-roles.md) | Coder / reviewer / auditor, with prompts |
| [6. The gates](docs/guide/06-gates.md) | Ambiguity + edit gates, as advice **and** as hooks |
| [7. Applied-AI addendum](docs/guide/07-applied-ai.md) | Deterministic core, evals, experiment tracking |
| [8. Adoption & interop](docs/guide/08-adoption.md) | Walkthroughs + running alongside spec-kit/Kiro |

## License

MIT — see [LICENSE](LICENSE). Original playbook ideas © their author; this structured kit is offered
freely for anyone to adapt.
