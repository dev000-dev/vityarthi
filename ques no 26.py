def lucas_sequence(n):
    """
    Generates the first n Lucas numbers.
    Lucas numbers start with 2, 1, and each subsequent number is the sum of the previous two.
    
    Args:
    n (int): The number of Lucas numbers to generate.
    
    Returns:
    list: A list of the first n Lucas numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    
    sequence = [2, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence
