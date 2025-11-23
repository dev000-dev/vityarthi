def zeta_approx(s, terms):
    """
    Approximate the Riemann zeta function ζ(s) using the first 'terms' of the series.

    Args:
        s (float or complex): The input value for the zeta function (Re(s) > 1 for convergence).
        terms (int): Number of terms to include in the approximation.

    Returns:
        float or complex: Approximate value of ζ(s).
    """
    if terms < 1:
        return 0
    total = 0.0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

# Example usage
if __name__ == "__main__":
    s = 2
    terms = 100
    print(f"Approximate ζ({s}) using {terms} terms: {zeta_approx(s, terms)}")
