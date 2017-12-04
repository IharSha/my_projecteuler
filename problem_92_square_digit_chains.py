def square_digit_sum(n):
    sum1 = 0
    while n != 0:
        next_digit = n % 10
        n //= 10
        sum1 += next_digit * next_digit
    return sum1


def chain_ending(n):
    while n not in (1, 89):
        n = square_digit_sum(n)
    return n


ending_89 = set(i for i in range(1, 568) if chain_ending(i) == 89)

counter = 0
ten_millions = 10**7

for i in range(1, ten_millions):
    if square_digit_sum(i) in ending_89:
        counter += 1

print(counter)
