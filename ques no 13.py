    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    # Assuming p is prime, as per the problem statement
    mersenne = (1 << p) - 1  # 2^p - 1
    return is_prime(mersenne)

# Example usage
print(is_mersenne_prime(2))   # True, 2^2 - 1 = 3, which is prime
print(is_mersenne_prime(3))   # True, 2^3 - 1 = 7, which is prime
print(is_mersenne_prime(5))   # True, 2^5 - 1 = 31, which is prime
print(is_mersenne_prime(7))   # True, 2^7 - 1 = 127, which is prime
print(is_mersenne_prime(11))  # False, 2^11 - 1 = 2047, which is not prime (2047 = 23 * 89)
print(is_mersenne_prime(13))  # True, 2^13 - 1 = 8191, which is prime

