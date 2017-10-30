import time
import math

counter = 1
number = 1
PRIMES = [2]

prime_position = 10001


def is_prime(n):
    if n == 1:
        return False

    for i in PRIMES:
        if math.sqrt(n) + 1 < i:
            return True
        if n % i == 0:
            return False
    return True


start = time.time()
while counter != prime_position:

    if is_prime(number):
        counter += 1
        PRIMES.append(number)
    number += 2

print(PRIMES[-1])
print(time.time() - start)
