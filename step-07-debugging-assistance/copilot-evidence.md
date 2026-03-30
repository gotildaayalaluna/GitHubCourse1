# Copilot Evidence — Step 07

## Debug prompt

Used Copilot to analyze: "Why does this function fail for empty input and outliers? Explain the bugs in summarize_response_times."

## /fix prompt

Used `/fix` with prompt: "Fix this function to correctly compute min, max, and average for non-negative response times while preserving the output schema."

## Root cause summary

Three bugs were identified:
1. Filter condition `value > 0` excluded zero, but 0 is a valid non-negative value. Fixed to `value >= 0`.
2. Initializing `min_value = 0` and `max_value = 0` caused min to always be 0 (no positive value is less than 0). Fixed by using Python's built-in `min()` and `max()` functions.
3. Integer division `//` truncated the average. Fixed to use float division `/` for correct decimal results.
