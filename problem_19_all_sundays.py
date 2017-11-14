days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_the_week = 2
sundays = 0
cur_year = 1901
last_one = 2001
while cur_year < last_one:
    for i in days:
        if (cur_year % 4 == 0 or cur_year == 2000) and i == 28:
            day_of_the_week = (day_of_the_week + i + 1) % 7
        else:
            day_of_the_week = (day_of_the_week + i) % 7
        if day_of_the_week == 0:
            sundays += 1
    if cur_year == 2000:  # we shouldn't count jan the first in 2001 if it's Sunday
        if day_of_the_week == 0:
            sundays -= 1
    cur_year += 1
print(sundays)

# or if datetime.datetime(y,m,1).weekday() == 6: count += 1 :)
# or 1200/7 = 171
