import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    res = np.empty((len(A[0]), len(A)))

    for i in range(len(A)):
        for j in range(len(A[i])):
            res[j, i] = A[i][j]

    return res