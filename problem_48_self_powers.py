sum_of_them = 0
for i in range(1, 1000):
    sum_of_them = (sum_of_them + i**i) % 10**10

print(sum_of_them)
