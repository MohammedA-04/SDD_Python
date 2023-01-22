# Act 2C - Turn each item of list into a Square **2 using Loop or comprehension
## To Square something by **2 Output should be [1, 4, 9, 16, 25, 36, 49]

# For Loop Method
print('\n\n')
aList = [1, 2, 3, 4, 5, 6, 7]

for i in aList:
    print(i**2)

# Other Method - Comprehension
print('\nComprehension')
aList = [1, 2, 3, 4, 5, 6, 7]
aList = [x * x for x in aList]
print(aList)