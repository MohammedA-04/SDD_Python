# 1D Subtract a week (7 days)  from a given date in Python

from datetime import datetime, timedelta

given_date = datetime(2021, 11, 25) # Variable = datetime mod(YY, MM, DD)
print("Given date | ", given_date)


days_to_subtract = 7 # Variable to subtract the days from the Week
res_date = given_date - timedelta(days=days_to_subtract)
# New Variable = given date - timedelta module (kwarg_day= Variable Subtract)
print("New Date   | ", res_date)

