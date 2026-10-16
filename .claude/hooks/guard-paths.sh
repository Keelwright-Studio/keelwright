#!/bin/sh
# PreToolUse guard for Write|Edit: deny .sync/ and "Claude outputs/", ask before privacy.html.
f=$(jq -r '.tool_input.file_path // ""')
case "$f" in
  */.sync/*|*"/Claude outputs/"*)
    printf '%s' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"This path is a generated artifact and must not be edited (see CLAUDE.md)."}}'
    ;;
  */site/privacy.html)
    printf '%s' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"privacy.html is linked from the store listings; confirm this edit."}}'
    ;;
esac
exit 0
