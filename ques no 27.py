import math

def is_perfect_power(n):
    """
    Checks if a number n can be expressed as a^b where a > 0 and b > 1.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is a perfect power, False otherwise.
    """
    if n <= 1:
        return False
    
    # Iterate over possible exponents b starting from 2
    max_b = int(math.log2(n)) + 2
    for b in range(2, max_b):
        # Binary search to find if there exists integer a such that a^b == n
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            try:
                power = mid ** b
                if power == n:
                    return True
                elif power < n:
                    low = mid + 1
                else:
                    high = mid - 1
            except OverflowError:
                # If overflow, mid is too large, reduce high
                high = mid - 1
    return False
