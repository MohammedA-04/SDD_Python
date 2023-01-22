#5B User inptus a Year which is converted into a Int
year = int(input("Enter a year: "))

if (year % 4) == 0:
# If the year % 4 and equals 0 then
    if (year % 100) == 0:

# Year is % by 100 I.e. Century
# Century Yr % 400 is a Leap Year
        if (year % 400) == 0:
            print(year, " is a leap year")
        else:
            print(year, " is not a leap year")

# If not NOT a Leap Year then else it coud be Leap otherwise it still isnt
    else:
        print(year, " is a leap year")
else:
    print(year, " is not a leap year")