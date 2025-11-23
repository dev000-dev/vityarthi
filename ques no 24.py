def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None
    k = 1
    current = a % n
    while current != 1:
        current = (current * a) % n
        k += 1
        if k > n:  # Safety check, though order should divide phi(n) <= n-1
            return None
    return k

# Example usage
print(order_mod(2, 5))   # 4
print(order_mod(3, 7))   # 6
print(order_mod(1, 10))  # 1
print(order_mod(2, 4))   # None
print(order_mod(5, 6))   # None
