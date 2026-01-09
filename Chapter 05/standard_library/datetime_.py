import datetime

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
print(diff.days)

day = datetime.date(2021, 12, 14)
print(day.weekday())
print(day.isoweekday())