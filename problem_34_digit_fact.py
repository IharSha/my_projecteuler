from math import factorial

"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""


# 10^{n-1} <= x < 10^n --> x==7, factorial(9)*7 upper bound

factorials = [factorial(i) for i in range(10)]
for i in range(3, factorials[9]*7):
    summ = 0
    number = i
    while number != 0:
        digit = number % 10
        number //= 10
        summ += factorials[digit]
        if summ > i:
            break
    if summ == i:
        print(i)
