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

def are_amicable(a, b):
    if a == b:
        return False
    return aliquot_sum(a) == b and aliquot_sum(b) == a

# Example usage
print(are_amicable(220, 284))  # True, amicable pair
print(are_amicable(1184, 1210))  # True, another pair
print(are_amicable(6, 6))  # False, same number
print(are_amicable(12, 16))  # False, not amicable
