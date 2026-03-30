# Usage Guide

This module provides utility functions for working with lists: chunking and computing moving averages.

## Quickstart

### Chunking a List

Use `chunk_list` to split a list into smaller sublists of a given size:

```python
from exercise import chunk_list

# Split a list into chunks of 3
data = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = chunk_list(data, 3)
print(chunks)  # [[1, 2, 3], [4, 5, 6], [7, 8]]
```

### Computing Moving Average

Use `moving_average` to calculate the rolling average over a sliding window:

```python
from exercise import moving_average

# Calculate 3-day moving average
prices = [10.0, 12.0, 11.0, 13.0, 15.0]
averages = moving_average(prices, 3)
print(averages)  # [11.0, 12.0, 13.0]
```

## Edge Cases

### Empty List

Both functions handle empty lists gracefully:

```python
chunk_list([], 5)      # Returns: []
moving_average([], 3)  # Returns: []
```

### Window Larger Than List

If the moving average window is larger than the input list, an empty list is returned:

```python
moving_average([1.0, 2.0], 5)  # Returns: []
```

### Invalid Size/Window

Both functions raise `ValueError` if size or window is zero or negative:

```python
chunk_list([1, 2, 3], 0)     # Raises ValueError: size must be > 0
moving_average([1.0], -1)    # Raises ValueError: window must be > 0
```
