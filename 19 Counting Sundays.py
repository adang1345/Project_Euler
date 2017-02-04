"""Count the number of Sundays that fell on the first of a month during 20th century"""

from datetime import datetime, timedelta

start = datetime(1901, 1, 6)  # start testing at 6 Jan 1901, which is known to be Sunday
end = datetime(2000, 12, 1)  # stop testing at or before 1 Dec 2000

current_date = start
num_sundays = 0
while current_date <= end:
    if current_date.day == 1:  # add 1 to counter if current date is 1st of month
        num_sundays += 1
    current_date += timedelta(7)  # increment current date by 7 to reach the next Sunday

print(num_sundays)
