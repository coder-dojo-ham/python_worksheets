import datetime

name = input('What is your name: ')

print('Hi ' + name + ' I am Python!')

year = input('What year were you born in: ')

month = input('What month number were you born on: ')

day = input('What day were you born on: ')

dob = datetime.date(int(year), int(month), int(day))

days = datetime.date.today() - dob

print(name + ' did you know that you are ' + str(days.days) + ' days old?')
