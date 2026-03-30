def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """Split a list into smaller chunks of a specified size.

    Parameters:
        values: The list of integers to be chunked.
        size: The maximum size of each chunk. Must be greater than 0.

    Returns:
        A list of lists, where each inner list contains at most `size` elements.
        The last chunk may contain fewer elements if the list doesn't divide evenly.

    Raises:
        ValueError: If size is less than or equal to 0.

    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """Calculate the moving average of a list of values.

    Parameters:
        values: The list of float values to compute the moving average over.
        window: The size of the sliding window. Must be greater than 0.

    Returns:
        A list of floats representing the moving averages. Returns an empty
        list if the window size is larger than the input list.

    Raises:
        ValueError: If window is less than or equal to 0.

    Example:
        >>> moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
        [2.0, 3.0, 4.0]
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result