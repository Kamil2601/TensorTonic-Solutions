import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    xy = [x_el * y_el for (x_el, y_el) in zip(x, y)]
    return float(sum(xy))