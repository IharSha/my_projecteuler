import time
import math

LIMIT = 2000000
NUMBER = 1
primes = [2]


def is_prime(n):
    if n == 1:
        return False

    for i in primes:
        if math.sqrt(n) + 1 < i:
            return True
        if n % i == 0:
            return False
    return True


start = time.time()
while NUMBER < LIMIT:

    if is_prime(NUMBER):
        primes.append(NUMBER)
    NUMBER += 2

print(sum(primes))
print(time.time() - start)
