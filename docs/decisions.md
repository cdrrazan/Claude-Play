# Decisions Ledger

Every deliberate choice gets **one home, a date, and a "revisit if."** This is where the *why* lives so
that six months and ten thousand agent-edits from now, anyone can see what was chosen and under what
condition to reconsider it.

**Format** (lightweight by default; the bracketed fields are borrowed from
[ADR/MADR](https://adr.github.io/madr/) — use them when a decision is weighty enough to warrant it):

```
## YYYY-MM-DD — <Decision title>
Status: accepted            # proposed | accepted | superseded by <date/title> | deprecated
Because: <the deciding reason>
Rejected <alternative> because: <why>
Consequences: <what this now commits us to — the trade-off we accepted>
Revisit if: <the condition that would reopen this>
```

Keep entries **imperative and specific** — "We use Postgres", not "We should probably use Postgres." Once
a decision is accepted, don't rewrite it; add a **new** entry that supersedes it and mark the old one
`Status: superseded`. The ledger is append-only history, not a live document.

---

## 2026-07-12 — FastAPI over Flask
Status: accepted
Because: We need async request handling and automatic OpenAPI schema generation out of the box.
Rejected Flask because: Sync-first; would require extra extensions for both async and schema, more moving parts.
Consequences: Team commits to Pydantic models everywhere; ties us to Python 3.10+.
Revisit if: We drop the async requirement, or a Flask-native async story matures enough to remove the extensions.

<!--
Add new decisions below, newest at the bottom. This example is illustrative — delete it when you add
your first real decision.
-->
