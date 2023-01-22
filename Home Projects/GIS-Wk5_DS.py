# Task 1 - Create Loop to print contents of following list via Loop
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for x in my_list:
    print(x)
"""

# Task 2 - Task 1 via a While Loop
# Made Mistake supposed to used [] be used instead of {}...
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
I = 0
while I < len(my_list):
    print(my_list[I])
    I += 1
"""

# Task 3 - Loop thru Tuple using Len and Range Functions
"""
my_tuple =  ("CFS2160",  "CFM2175", "CFS2101")
for I in range(len(my_tuple)):
    print(my_tuple[I])
"""

# Task 4 - Loop print Values & Calculates avg score
"""
my_dictonary = {"CFS2160" : 89, "CFM2175": 87 , "CFS2101" : 99}
for Value in my_dictonary.values():
    print(Value)
print( "Average", sum(my_dictonary.values()) / len(my_dictonary))
"""

# Task 5 - Create Loop that prints the values in the Key Set
"""
my_dictonary = {"CFS2160" : 89, "CFM2175": 87 , "CFS2101" : 99}
for key in my_dictonary.keys():
    print(key)
"""