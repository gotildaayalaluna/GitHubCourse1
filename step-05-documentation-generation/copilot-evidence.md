# Copilot Evidence — Step 05

## Documentation prompt

Used Copilot with prompt: "Generate a complete Python docstring for this function including purpose, args, returns, raises, and an example." Applied to both `chunk_list` and `moving_average` functions.

## What you edited after Copilot output

Refined the example outputs to match actual function behavior. Added the USAGE.md quickstart showing practical use cases (chunking data, calculating moving averages) and edge case documentation for empty lists, oversized windows, and invalid inputs.

## Accuracy check

Verified documentation accuracy by running the examples in Python REPL to confirm the docstring examples produce the documented outputs. Tested edge cases (empty list, window > list length, size=0) to ensure the raises/returns documentation is correct.
