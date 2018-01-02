def total_divisors(n):
    count = 2  # accounts for 'n' and '1'
    i = 2
    while i**2 < n:
        if n % i == 0:
            count += 2
        i += 1
    count += (1 if i**2 == n else 0)
    return count


ans = 0
prv_total_divisors = 0

for i in range(2, 10000000):
    if i % 200000 == 0:
        print(i)
    total_divs = total_divisors(i)
    if total_divs == prv_total_divisors:
        ans += 1
    prv_total_divisors = total_divs

print(ans)
