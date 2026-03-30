
# Copilot Evidence — Step 01

## Prompt 1

Used Copilot to implement `normalize_username` - trimming whitespace, converting to lowercase, replacing spaces with underscores, removing invalid characters, and collapsing repeated underscores.

## Why you accepted/rejected the suggestion

Accepted because the suggestion correctly implemented all the rules specified in the docstring: trim, lowercase, replace spaces with underscores, remove non-alphanumeric characters (except underscore), collapse repeated underscores, and strip leading/trailing underscores.

## Final check

Also implemented `build_slug` which converts titles to URL-friendly slugs by lowercasing, replacing non-alphanumeric sequences with hyphens, and stripping leading/trailing hyphens. Both functions passed validation.
