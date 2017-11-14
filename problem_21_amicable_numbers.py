import math

number = 3
PRIMES = [2]

maximum_number = 10000


def is_prime(n):
    if n == 1:
        return False

    for prime in PRIMES:
        if math.sqrt(n) + 1 < prime:
            return True
        if n % prime == 0:
            return False
    return True


def dividers_sum(n):
    even_dividers_sum = 1
    if n in PRIMES:
        return even_dividers_sum
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            even_dividers_sum = even_dividers_sum + j + n//j
            if j**2 == n:
                even_dividers_sum -= j

    return even_dividers_sum


while PRIMES[-1] < maximum_number:

    if is_prime(number):
        PRIMES.append(number)
    number += 2

amicable_numbers = []
for number in range(2, maximum_number + 1):
    if number in amicable_numbers:
        continue
    second_number = dividers_sum(number)
    if second_number > number:
        second_sum_dividers = dividers_sum(second_number)
        if second_sum_dividers == number and number != second_number and second_number <= maximum_number:
            amicable_numbers.append(number)
            amicable_numbers.append(second_number)


print(sum(amicable_numbers))
