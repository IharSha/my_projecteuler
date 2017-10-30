import time

n = 220


def evenly_divisible_20(number):
    while True:
        for i in range(11, 20):
            if number % i:
                break
        else:
            return number
        number += 220


start = time.time()
print(evenly_divisible_20(n))
print(time.time() - start)
