import datetime

myDate = datetime.date(2020, 1, 1) # custom
print(myDate)

todayDate = datetime.date.today() # current date
print(todayDate)

print(todayDate.year)
print(todayDate.month)
print(todayDate.day)


wday = todayDate.weekday()  # 0 - Monday
print(wday)