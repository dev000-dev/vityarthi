def partition_function(n):
    """
    Calculate the number of distinct ways to write n as a sum of positive integers.
    This function implements the classical partition function p(n).

    Args:
        n (int): The integer to partition (n >= 0).

    Returns:
        int: Number of distinct partitions of n.
    """
    if n < 0:
        return 0
    partitions = [0] * (n + 1)
    partitions[0] = 1  # base case

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

# Example usage
if __name__ == "__main__":
    test_n = 5
    print(f"Number of partitions of {test_n} is {partition_function(test_n)}")
