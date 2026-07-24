#!/usr/bin/env bash
# Evidence rule, applied to Keel's own claims: prove the shipped enforcement
# hook actually denies agent commits/pushes and leaves everything else alone.
set -euo pipefail

hook=".claude/hooks/block-agent-commits.sh"

deny=(
  'git commit -m "x"'
  'git push origin main'
  'git -C /some/repo push'
  'cd subdir && git commit --amend'
)
allow=(
  'git status'
  'git log --oneline'
  'git diff HEAD~1'
  'echo git commitment'
)

fail=0
for c in "${deny[@]}"; do
  out=$(jq -n --arg c "$c" '{tool_input:{command:$c}}' | bash "$hook")
  if [ -z "$out" ]; then echo "FAIL — should deny: $c"; fail=1; fi
done
for c in "${allow[@]}"; do
  out=$(jq -n --arg c "$c" '{tool_input:{command:$c}}' | bash "$hook")
  if [ -n "$out" ]; then echo "FAIL — should allow: $c"; fail=1; fi
done

if [ "$fail" -eq 0 ]; then
  echo "hook behaves: ${#deny[@]} commands denied, ${#allow[@]} allowed"
fi
exit "$fail"
