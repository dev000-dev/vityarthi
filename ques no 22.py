def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        return None
    # Check if moduli are pairwise coprime (optional, but for simplicity assume they are)
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(remainders, moduli):
        M_i = M // m
        y = mod_inverse(M_i, m)
        if y is None:
            return None  # Not coprime
        x += r * M_i * y
    return x % M

# Example usage
print(crt([2, 3, 2], [3, 5, 7]))  # 23
print(crt([1, 2], [3, 4]))         # None, since 3 and 4 not coprime
print(crt([1, 1], [2, 3]))         # 1
