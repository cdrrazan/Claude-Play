# AGENTS.md — instructions for AI coding agents

This is the canonical instruction file for agents working in this repo. It is tool-neutral. Claude Code
reads `CLAUDE.md`, which imports this file. Keep this file **short** — if it grows past ~200 lines, agents
start ignoring the tail. Add a rule only when you'd otherwise re-explain it.

> Replace the bracketed placeholders below with your project's real details, then delete this line.

---

## The gates (read before doing anything)

**Ambiguity gate.** Confused or ambiguous? **Stop and ask.** If you are running unattended, state the
ambiguity and which assumption you chose — silent resolution of confusion is never acceptable.

**Edit gate.** Questions and problem reports get **diagnosis only** — report findings, change nothing —
until I explicitly say *fix* or *implement*. **Never commit or push.** The human authors every commit.

**Evidence rule.** A claim about the code that doesn't trace to a **fresh read** of the code is labelled
`unverified`. No silent failures. For any pass/fail claim, show the raw output — the command you ran and
what it returned — not a summary that says "it works."

## Project map

- **What this is:** [one-line description of the project]
- **Stack:** [languages, frameworks, key libraries]
- **How to run it:** [command]
- **How to run tests:** [command] — a claim that tests pass must include this command's raw output.
- **How to lint/format:** [command]
- **Domain terms:** [term = meaning; term = meaning] — the words that mean something specific here.
- **Landmines:** [things that look editable but aren't; generated files; external contracts]

## Working rules

- **One canonical value per concept; one choke point per external dependency.** Don't scatter the same
  constant or the same API client across the codebase.
- **Deterministic core.** Business logic is deterministic and testable. The LLM narrates at the boundary;
  it never does the computing that a function should.
- **Stay in scope.** Touch only the files named in the task. No "while I'm here" fixes — raise them
  separately.

## The ledgers (your memory lives here, not in the tool)

- **`docs/decisions.md`** — every deliberate choice gets one home, a date, and a "revisit if." Before
  proposing an approach, check whether it's already decided.
- **`docs/falsified.md`** — every idea we killed, with the mechanism and the numbers. **A tweak of a dead
  idea is the same idea.** Before proposing something, check it isn't already on this list.

## Roles

Non-trivial work runs through separate agents, each with its own prompt in `roles/`:
- **Coder** (`roles/coder.md`) — implements one scoped step. Never commits.
- **Reviewer** (`roles/reviewer.md`) — adversarial, blind to the author's reasoning, tries to refute.
- **Auditor** (`roles/auditor.md`) — checks an idea against `docs/falsified.md` first.

## Reporting format

When you report a result: **verdict first**, then metrics against a *named* baseline, then caveats, then
your recommendation last. Measure what the system actually acts on, not the whole population.
