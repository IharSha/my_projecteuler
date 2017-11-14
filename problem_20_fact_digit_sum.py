def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


factorial_100 = factorial(100)
digit_sum = 0
for digit in str(factorial_100):
    digit_sum += int(digit)
print(digit_sum)
