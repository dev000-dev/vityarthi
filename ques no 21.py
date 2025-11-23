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
        return None  # No inverse exists
    else:
        return x % m

# Example usage
print(mod_inverse(3, 7))   # 5, because 3*5 ≡ 1 mod 7
print(mod_inverse(2, 5))   # 3, because 2*3 ≡ 1 mod 5
print(mod_inverse(2, 4))   # None, no inverse
print(mod_inverse(5, 11))  # 9, because 5*9 ≡ 1 mod 11
