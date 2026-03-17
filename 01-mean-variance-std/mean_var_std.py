import numpy as np

def calculate(lst):
    """
    Computes the mean, variance, standard deviation, max, min, and sum
    of a 3x3 matrix.

    Args:
        lst (list): A list containing exactly 9 numerical elements to be
                    reshaped into a 3x3 NumPy array.

    Returns:
        dict: A dictionary where each key represents a statistic.
              The values are lists containing three sub-elements:
              - Index 0: Statistics along the columns (axis 0).
              - Index 1: Statistics along the rows (axis 1).
              - Index 2: The statistic for the flattened matrix.

    Raises:
        ValueError: If `lst` does not contain exactly nine elements.
    """
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations