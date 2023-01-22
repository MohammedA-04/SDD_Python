# Activity 1: Code Execution and Tracing
# / How is the Ex using datetime module to print current date
# // Try to print current time:

from datetime import date
now = date.today()
print (now.day)
print (now.month)
print (now.year)
print (now.ctime()) # / ctime = Wed Nov 23 00:00:00 2022

# Displaying 3 Sentences above in ONE line
# / 23 11 2022
print (now.day, now.month, now.year)


# Fromat the date and time into human readable string
# / We use the strftime() datetime module
"""
Today = datetime.now()
print (Today.strftime(“%a, %B, %d, %y”))

- %a | Stands for Day
- %B | Stands for Month
- %d | Stands for Date
- %y | Stands for Year 
"""

