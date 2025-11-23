def multiplicative_persistence(n):
    if n < 10:
        return 0
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

# Example usage
print(multiplicative_persistence(39))  # 3: 3*9=27, 2*7=14, 1*4=4
print(multiplicative_persistence(25))  # 2: 2*5=10, 1*0=0
print(multiplicative_persistence(4))   # 0: already single digit
print(multiplicative_persistence(77))  # 4: 7*7=49, 4*9=36, 3*6=18, 1*8=8
print(multiplicative_persistence(0))   # 0: single digit
