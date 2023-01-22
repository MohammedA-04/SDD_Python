# 3B | Write a program to count the number of even and odd numbers from a series numbers
# Numbers [1,2,3,4,5,6,7,8,9,]
"""
[2,4,6,8] are even
[1,3,5,7,9] are odd
"""
GivenNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Even_Count = 0
Odd_Count = 0

for i in GivenNum:
    if i % 2 == 0:
        Even_Count += 1
    else:
        Odd_Count += 1

print(" Even numbers in the list: ", Even_Count)
print("Odd numbers in the list ", Odd_Count)

