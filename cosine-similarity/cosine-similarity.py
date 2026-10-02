import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    ab = np.sum(a*b).item()
    a_norm = np.sqrt(np.sum(a*a)).item()
    b_norm = np.sqrt(np.sum(b*b)).item()

    if a_norm == 0 or b_norm == 0:
        return 0.0
    else:
        return float(ab/(a_norm * b_norm))