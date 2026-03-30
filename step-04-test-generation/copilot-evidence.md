# Copilot Evidence — Step 04

## Prompt used for test generation

Used Copilot with prompt: "Generate Python unittest cases for the sanitize_tags function including edge cases for empty input, duplicate tags with mixed case, tags with punctuation, whitespace trimming, and first-seen order preservation."

## Extra edge case Copilot missed

Added test for tags that become completely empty after cleanup (like "!!!" or "@#$"). Also added a test combining multiple edge cases: valid tags, invalid tags, and duplicates in the same input to verify the function handles all rules simultaneously.

## Final test count

9 test methods with 9 assertions covering: empty input, basic normalization, duplicate tags with mixed case, punctuation removal, whitespace trimming, empty-after-cleanup tags, first-seen order preservation, mixed valid/invalid/duplicate input, and hyphenated tags.
