summ = 1000
for i in range(1, summ):
    for j in range(i, summ):
        if i**2 + j**2 == (summ - i - j)**2:
            c = summ - i - j
            print(c*i*j)
            break
