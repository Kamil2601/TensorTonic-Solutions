from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.mean(x).item()
    median = np.median(x).item()

    c = Counter(sorted(x))
    mode = c.most_common(1)[0][0]

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }

    
    