limit = 10**7
table = [1 for i in range(limit + 1)]

for i in range(1, limit + 1):
    N = i
    while N < limit:
        table[N] += 1
        N += i

C = 0

for n in range(1, limit + 1):
    if table[n-1] == table[n]:
        C += 1

print(C)
