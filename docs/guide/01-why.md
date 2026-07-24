# 1. Why this exists

## The problem: agent-edit rot

An AI coding agent will make a hundred changes to your repo in an afternoon. Most are fine. But agents
have three failure modes that compound over time:

1. **They forget.** An agent has no memory of the experiment you ran last week that failed. So it proposes
   it again. And again. Each time costs you the review to notice it's a re-run.
2. **They over-reach.** Asked to fix one thing, an agent "helpfully" refactors three others. Each
   unrequested change is a review you didn't budget for and a risk you didn't sign up for.
3. **They're confidently wrong.** An agent will tell you "the tests pass" without running them, or "this
   handles the edge case" without reading the code that supposedly handles it.

None of these is fatal once. All of them are corrosive across thousands of edits. The codebase slowly
fills with re-litigated decisions, scope creep, and claims nobody verified. That's **agent-edit rot.**

## The fix: a reliability layer, not a framework

Keel doesn't generate code and doesn't tell you how to architect your app. It installs a small
discipline that directly counters the three failure modes:

- **Against forgetting** → two committed **ledgers**: what we decided, and what we killed.
- **Against over-reach** → **scoped roles** and an **edit gate** that keeps agents in their lane.
- **Against confident wrongness** → an **evidence rule** and a **blind adversarial reviewer.**

It treats your **code as the source of truth** and governs how agents are allowed to make claims about
it. That's the whole idea.

## Where this sits vs. spec-kit and Kiro

You may already use — or be considering — a spec-driven tool like
[GitHub spec-kit](https://github.com/github/spec-kit) or [AWS Kiro](https://kiro.dev). Those are
**generative**: they make a *specification* the source of truth and generate the code from it. Keel is
**epistemic**: it assumes the code is the source of truth and keeps agents honest about it.

They answer different questions:

| | Question it answers | Source of truth |
|---|---|---|
| **spec-kit / Kiro** | "How do I produce code from intent?" | The spec |
| **Keel** | "How do I keep a codebase trustworthy after thousands of edits?" | The code |

So this is **not a competitor** to spec-kit or Kiro — it's the reliability layer that sits *underneath*
whatever generation workflow you use. Use spec-kit to write the feature; use the ledgers, roles, and gates
here to make sure that feature — and the next ten thousand agent edits after it — stays honest.

## The five-year-old version

Imagine robot helpers building a LEGO castle with you. They build *really* fast, but: they **forget**
(yesterday the thin-piece drawbridge fell off; today a robot tries thin pieces again), they **do too
much** (asked to fix a window, one rebuilds two towers you liked), and they **fib without meaning to**
("the castle is sturdy!" — without ever wiggling it).

Keel is the **house rules taped to the wall**: two notebooks — what we *decided* and what we *tried and
it broke* — so nobody builds the thin drawbridge twice; three jobs for three robots — one builds, one
checks the work without hearing the builder's excuses, one checks the notebooks before anyone starts —
so nobody grades their own homework; and simple rules — confused? stop and ask; say "it's sturdy"? show
the wiggle test. And **only the human glues**: robots suggest, you make it permanent.

→ Next: [The 15 principles](02-principles.md)
