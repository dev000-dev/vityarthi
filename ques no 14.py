def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    primes = [p for p in range(2, limit + 1) if is_prime(p)]
    twins = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twins.append((primes[i], primes[i + 1]))
    return twins

# Example usage
print(twin_primes(20))  # [(3, 5), (5, 7), (11, 13), (17, 19)]
print(twin_primes(50))  # Includes more pairs
