days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cur_day = 0
sundays = 0
cur_year = 1900
last_one = 2001
while cur_year < last_one:
    for i in days:
        if (cur_year % 4 == 0 or cur_year == 2000) and i == 28:
            cur_day += i + 1
        else:
            cur_day += i
        if (cur_day + 1) % 7 == 0:
            sundays += 1
    cur_year += 1
    if cur_year == last_one:
        if cur_day % 7 == 0:
            sundays -= 1
print(sundays - 2)
