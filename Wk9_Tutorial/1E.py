# Find the day of the week of given date
# Given given_date(2021,11,13) --> Output: Sunday


# / Solution 1
from datetime import datetime
given_date = datetime(2021, 11, 13)

# Getting Weekday as int
# / Given date variable.today.weekday
print(given_date.today().weekday())

# To get the english name of the weekday
# // Given date variable.sftrftime('A'))
print(given_date.strftime('%A'))

# // Solution 2 via calendar module

import calendar # Import calendar module and Below the datetime module
from datetime import datetime

given_date = datetime(2021, 11, 13)
# / Weekday VAR = calendar.day_name[GivenDate_VAR.weekday()]
# // Calendar is a module

weekday = calendar.day_name[given_date.weekday()]
print(weekday)

