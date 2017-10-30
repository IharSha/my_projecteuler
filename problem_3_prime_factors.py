import time
number = 600851475143


def primes(start, n):
    if n >= start:
        for i in range(start, n + 1):
            if n % i == 0:
                print(i)
                n /= i
                start = i
                break

        primes(start, int(n))


timer = time.time()
primes(2, number)
print(time.time() - timer)

