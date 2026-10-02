import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.array(matrix, dtype="float")
    if norm_type == "l1":
        norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
    else:
        norm = np.max(np.abs(matrix), axis=axis, keepdims=True)

    return matrix / np.where(norm == 0, 1.0, norm)