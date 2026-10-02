import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    def pmf_fun(i):
        return math.comb(n, i) * p**i * (1-p)**(n-i)

    all_pmf = [pmf_fun(i) for i in range(k+1)]

    return {
        "pmf": float(all_pmf[-1]),
        "cdf": float(sum(all_pmf))
    }