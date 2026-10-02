import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.array(X, dtype="float")
    X_mean = np.mean(X, axis=0)
    X_c = X - X_mean

    N = len(X)
    cov = (X_c.T @ X_c) / (N-1)

    return cov