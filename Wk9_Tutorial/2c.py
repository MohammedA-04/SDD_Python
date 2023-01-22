# Add a week [7dys] and 12 hours to the given date

from datetime import datetime, timedelta, time

given_date = datetime(2020, 3, 22)
given_time = time(00,00,00)
print(given_time)

days_add = 7
hrs_add = 12

new_date = given_date + timedelta(days=days_add)
new_time = given_time + timedelta(hours=12)
#day_n_time = new_date  new_time
#print(new_date)