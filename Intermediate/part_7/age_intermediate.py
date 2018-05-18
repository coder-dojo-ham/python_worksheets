import datetime

year = input('What year were you born in: ')

month = input('What month number were you born on: ')

day = input('What day were you born on: ')

dob = datetime.date(int(year), int(month), int(day))

days = datetime.date.today() - dob

print('Did you know that you are ' + str(days.days) + ' days old?')
