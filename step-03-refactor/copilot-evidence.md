# Copilot Evidence — Step 03

## Refactor prompt

Used Copilot to refactor the duplicated discount logic by extracting a shared helper function called `apply_discount`. Prompted: "Extract the duplicated discount calculation logic into a helper function named apply_discount while keeping the public function signatures unchanged."

## Why behavior is preserved

The `apply_discount` helper contains the exact same logic that was previously duplicated in both functions: checking if discount is <= 0, calculating the discount amount, subtracting from subtotal, clamping to 0 if negative, and rounding to 2 decimal places. Both `checkout_total` and `invoice_total` now delegate to this helper after computing their subtotals.

## Before vs after summary

Before: Both `checkout_total` and `invoice_total` had identical 8-line blocks for discount calculation. After: The shared logic is extracted into `apply_discount`, and each function simply computes the subtotal and calls the helper. This reduces code duplication and makes the discount logic easier to maintain.
