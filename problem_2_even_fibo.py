LIMIT = 4 * 10**6
SUMM = 0


def fibi(a, b):
    if a % 2 == 0:
        print(a)

        global SUMM
        SUMM += a
    if b < LIMIT:
        a, b = b, a + b
        return fibi(a, b)


print()
print('All even fibonacci numbers before {}:'.format(LIMIT))

first_number = 1
second_number = 2
fibi(first_number, second_number)
print()
print('The sum of them is:', SUMM)
