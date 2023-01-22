# Python program to demonstrate list comprehension in Python
# (Range from 1 to 11)

SquareNums = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(SquareNums)

"""
Square Number Variable is assgined 
# [x**2 for x in range (1,11) if x % 2 == 1] 
## if x mod 2 == 1 
## All SqNums have R1 when modulus by 2 
then 
### print(SquareNums)
    E.g. [1,9,25,49,81]
"""