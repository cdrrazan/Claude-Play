# 5. The three roles

> Principle 8: **implementer, reviewer, and auditor are different agents.**

The reason is simple and now well-documented: **a single model that checks its own work is an echo
chamber.** It rationalizes its own choices. Splitting the work across separate agents — each with a
different job and a different view — breaks that. This "adversarial" split is no longer a fringe idea; it
shows up in [Anthropic's own best-practices](https://code.claude.com/docs/en/best-practices) and in the
documented [adversarial code review](https://asdlc.io/patterns/adversarial-code-review/) pattern.

The three prompts are ready to paste from [`roles/`](../../roles/).

## Coder — [`roles/coder.md`](../../roles/coder.md)

Implements **one scoped step** of an already-approved plan. Touches only the named files. No "while I'm
here" fixes. **Never commits.** Stops on ambiguity. For any "it works" claim, shows the command and its
raw output.

## Reviewer — [`roles/reviewer.md`](../../roles/reviewer.md)

Runs in a **fresh context**, sees **only the diff and the acceptance criteria — not the coder's
reasoning.** Its job is to **refute** the change, not bless it. Verdict is one of `ship` / `fix-first` /
`can't-verify`.

**The one nuance to get right:** a reviewer told to "find problems" will invent them, driving
over-engineering — this is a documented failure mode. So the reviewer here is scoped to **correctness and
requirements only**, and is explicitly told to say "ship" plainly when the work is sound rather than
manufacture nitpicks. Adversarial, but not theatrical.

## Auditor — [`roles/auditor.md`](../../roles/auditor.md)

Vets an *idea* before a coder touches it. **Step 0 is always the dead-list check:** read
[`falsified.md`](../falsified.md), and if the idea (or a tweak of a killed one) is there, stop. Then check
it against accepted decisions. Then, if it's genuinely new, name the cheapest test that would falsify it.

## How they fit together

```
   idea ──► AUDITOR ──► (worth-testing?) ──► approved plan
                                                  │
                                                  ▼
                                                CODER ──► diff
                                                  │
                                                  ▼
                              REVIEWER (blind) ──► ship / fix-first / can't-verify
                                                  │
                                                  ▼
                                        human authors the commit
```

You don't need all three for a one-line change — that's principle 15. Reach for the reviewer when a change
is non-trivial; reach for the auditor once `falsified.md` has enough entries that re-runs become a real
risk.

→ Next: [The gates](06-gates.md)
