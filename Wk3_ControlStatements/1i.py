# Print list in reverse via a Loop [10, 20, 30, 40, 50]

# Solution 1 = Using a reversed Function and For Loop
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)    # Reversing da List
for item in new_list:         # Iterate Reversed List
    print(item)

# Solution 2 = Using a Loop and Len() Function
list1 = [10, 20, 30, 40, 50]    # Get List Size (list1)
size = len(list1) - 1           # len(list1) -1: Index' Starts wiv 0
for i in range(size, -1, -1):   # Iterate List1 in Reverse Order
    print(list1[i])             # Start from last item to first

