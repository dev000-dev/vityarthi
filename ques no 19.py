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

def is_highly_composite(n):
    if n <= 1:
        return True  # 1 has 1 divisor, no smaller
    divisors_n = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= divisors_n:
            return False
    return True

# Example usage
print(is_highly_composite(1))   # True
print(is_highly_composite(2))   # True
print(is_highly_composite(3))   # False
print(is_highly_composite(4))   # True
print(is_highly_composite(6))   # True
print(is_highly_composite(12))  # True
print(is_highly_composite(10))  # False, 10 has 4 divisors (1,2,5,10), 6 has 4, but 12 has 6
