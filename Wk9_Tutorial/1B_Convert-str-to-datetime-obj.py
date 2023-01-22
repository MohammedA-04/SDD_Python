# date_string = "Nov 25 2021 4:30PM"

from datetime import datetime

date_string = "Nov 25 2021  4:30PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)


"""
- %d = Day
- %B = Month
- %Y = Year
- %I : %M%p =  
"""