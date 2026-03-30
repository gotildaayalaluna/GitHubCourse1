# Copilot Evidence — Step 02

## /explain output summary

Used `/explain` on `parse_scoreboard` to understand the bugs. The function had several issues:
1. No handling for spaces around names/scores (e.g., "alice : 10" would fail)
2. No try/except for malformed segments - crashes on invalid input like "invalid"
3. The duplicate name logic was wrong - it just overwrote values instead of keeping the maximum score

## /fix prompt used

Used `/fix` to correct the parsing bugs. Fixed by:
- Adding `.strip()` to handle whitespace around names and scores
- Wrapping parsing in try/except to skip malformed segments
- Using `max(board[name], value)` to keep the highest score for duplicate players

## /generate prompt used

Used `/generate` to create the `top_player` helper function that returns the player with the highest score. For ties, it sorts alphabetically and returns the first player.

## What you changed manually afterward

Verified the implementation handles edge cases: empty strings, whitespace-only input, malformed segments, and tie-breaking by alphabetical order.
