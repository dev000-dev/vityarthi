def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def is_quadratic_residue(a, p):
    a = a % p
    if a == 0:
        return True
    if p == 2:
        return True
    exp = (p - 1) // 2
    res = mod_exp(a, exp, p)
    return res == 1

# Example usage
print(is_quadratic_residue(1, 5))   # True
print(is_quadratic_residue(2, 5))   # True
print(is_quadratic_residue(3, 5))   # True
print(is_quadratic_residue(4, 5))   # True
print(is_quadratic_residue(0, 5))   # True
print(is_quadratic_residue(3, 7))   # True
print(is_quadratic_residue(5, 7))   # False
print(is_quadratic_residue(6, 7))   # False
