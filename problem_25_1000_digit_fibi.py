def fibonacchi_1000_digit(amount_of_digits):
    a, b, index = 1, 1, 1
    while a < 10**(amount_of_digits-1):
        a, b, index = b, a + b, index + 1

    return index


print(fibonacchi_1000_digit(1000))
