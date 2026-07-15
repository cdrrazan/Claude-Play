# Enforcement hooks (optional)

`AGENTS.md` is **context, not enforcement** — an agent *usually* follows it, but compliance isn't
guaranteed. To make a gate a hard constraint, use a
[PreToolUse hook](https://code.claude.com/docs/en/hooks): a check that runs before a tool call and can
block it.

**Adopt hooks last.** Start with the gates as written rules; add enforcement once the team trusts the
discipline and wants it guaranteed rather than requested.

## Example: enforce "the human authors every commit"

The edit gate says agents never commit or push. To enforce it, register a PreToolUse hook on the `Bash`
tool in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": ".claude/hooks/block-agent-commits.sh" }
        ]
      }
    ]
  }
}
```

The script receives the tool call as JSON on stdin; if the command matches `git commit` or `git push`,
it exits non-zero (blocking the call) with a message pointing back to the gate:

```bash
#!/usr/bin/env bash
set -euo pipefail
cmd="$(jq -r '.tool_input.command // empty')"
if printf '%s' "$cmd" | grep -Eq 'git[[:space:]]+(commit|push)'; then
  echo "BLOCKED by edit gate: the human authors every commit (AGENTS.md)." >&2
  exit 2
fi
```

Save it as `.claude/hooks/block-agent-commits.sh`, make it executable (`chmod +x`), and the gate is no
longer a request — it's a rule the tooling enforces.

Other gates can be enforced the same way (e.g. block `Edit`/`Write` outside a task's named files). Check
hook syntax against the [current docs](https://code.claude.com/docs/en/hooks) before relying on it — the
interface evolves.
