def collatz_length(n):
    """
    Returns the number of steps for n to reach 1 in the Collatz conjecture.
    The Collatz conjecture states that for any positive integer n, the sequence will eventually reach 1.
    
    Args:
    n (int): A positive integer.
    
    Returns:
    int: The number of steps to reach 1.
    
    Raises:
    ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
