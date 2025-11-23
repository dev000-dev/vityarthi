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

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

# Example usage
print(is_fibonacci_prime(2))   # True
print(is_fibonacci_prime(3))   # True
print(is_fibonacci_prime(5))   # True
print(is_fibonacci_prime(13))  # True
print(is_fibonacci_prime(1))   # False, not prime
print(is_fibonacci_prime(4))   # False, not prime
print(is_fibonacci_prime(8))   # False, not prime
print(is_fibonacci_prime(7))   # False, not Fibonacci
