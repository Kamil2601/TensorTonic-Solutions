import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x_mean = np.mean(x)
    n = len(x)
    s_squared = 1/(n-1) * np.sum((x-x_mean)**2)
    s = np.sqrt(s_squared)

    return {
        "variance": s_squared.item(),
        "standard_deviation": s.item()
    }