from time import clock


PRIMES = [2]


def is_prime(n):
    if n == 1:
        return False

    for prime in PRIMES:
        if prime*prime > n:
            return True
        if n % prime == 0:
            return False
    return True


number_for_prime = 1
while len(PRIMES) < 1024:
    if is_prime(number_for_prime):
        PRIMES.append(number_for_prime)
    number_for_prime += 2
print(PRIMES)


number = 1
start = clock()
while True:
    counter = 1
    triangle_number = (1 + number) * number // 2
    summ = triangle_number
    for i in PRIMES:
        if i * i > triangle_number:
            counter *= 2
            if i * i == triangle_number:
                counter += 1
            break

        exponent = 1
        while triangle_number % i == 0:
            exponent += 1
            triangle_number /= i
        if exponent > 1:
            counter *= exponent
        if triangle_number == 1:
            break
    if counter >= 500:
        print()
        print("Number:", number)
        print("triangle number:", summ)
        print("Divisible amount:", counter)
        break
    number += 1
print(clock() - start)
