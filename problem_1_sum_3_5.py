SUMM = 0
LIMIT = 10000000

for i in range(3, LIMIT):
    if i % 3 == 0 or i % 5 == 0:
        SUMM += i
