def count_divisors(n):
    if n <= 0:
        return 0
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

# Example usage
print(count_divisors(12))  # 6 (1, 2, 3, 4, 6, 12)
print(count_divisors(7))   # 2 (1, 7)
print(count_divisors(1))   # 1 (1)
print(count_divisors(0))   # 0
