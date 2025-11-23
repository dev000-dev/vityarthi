def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i and n // i != n:
                total += n // i
    return total

# Example usage
print(aliquot_sum(12))  # 16 (1+2+3+4+6)
print(aliquot_sum(6))   # 6 (1+2+3)
print(aliquot_sum(1))   # 0
print(aliquot_sum(28))  # 28 (1+2+4+7+14), perfect number
