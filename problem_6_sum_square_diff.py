start = 1
lim = 10
#   bruteforce: 3.33s for 10000000
#   прогрессия: 0 for any...
a = (start + lim)*lim//2
sums = a*a

squares = (2*lim + 1)*(lim + 1)*lim//6

print(sums-squares)
