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

# Example usage
print(mod_exp(2, 10, 1000))  # 2^10 % 1000 = 1024 % 1000 = 24
print(mod_exp(3, 4, 7))      # 3^4 % 7 = 81 % 7 = 4
print(mod_exp(5, 0, 13))     # 5^0 % 13 = 1 % 13 = 1
print(mod_exp(7, 5, 11))     # 7^5 % 11 = 16807 % 11 = 5
