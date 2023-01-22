# Activity 1A |  Function to count the length of a string passed as a parameter
"""print('Activity 1A')
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('SoftwareDesignAndDevelopment'))
print(string_length('Software Design And Development'))"""

# Activity 1B | Create a new-string made of an input string 1st, middle and last char
"""print('\nActivity 1B')
string = 'melon'
print("Original String is", string)

l1 = string[0]          # Get First character
strlen = len(string)    # Get string len
MI = int(strlen/2)      # Get Middle Index number
l1 = l1 + string[MI]    # Get Middle character and add it to result

l1 = l1 + string[strlen - 1] # Get last character and add it to result
print("New String:", l1)"""

# Activity 1C | Substring "Huddersfield" in a given string by ignoring the case
"""print('\nAcitivty 1C')
str1 = "Welcome it to Huddersfield. Huddersfield  isawesome, isn't it Huddersfield?"
sub_string = "Huddersfield" # Qty Hudd's appears

temp_str = str1.lower() # convert string to Lowercase

# use count function .count
count = temp_str.count(sub_string.lower())
print("The Huddersfield count is:", count) """

# Activity 1D | Two ways to reverse a given string by using negative slicing & BIF Reversed
"""print('\nActivity 1D')
print('Solution 1 : Negative Slicing')
str1 = "HuDDeRsfiElD"
print("Original String is:", str1)
str1 = str1[::-1] # [::-1 Count from D to H -1 Each Time]
print("Reversed String is:", str1)

print('\nSolution 2 : Built-in function')
str1 = "HuDDeRsfiElD"
print("Original String is:", str1)
str1 = ''.join(reversed(str1))
print("Reversed String is:", str1) """

# Activity 1E | Splitting given string on hyphens and display each substring
"""str1 = "Sun-sets-in-the-west"
print("Original String is:", str1)

# Split string - .spilt using "-" character
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)"""

# Activity 1F | Remove Empty Strings from a list of strings
""" Solution 1 - Using Loop and If conditions 
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for str in str_list:
    # check for not-empty string
    if str:
        res_list.append(str)
    # If there is something in str_list when 'str' loops thru
    # appends not-empty string
print(res_list) """

""" Solution 2 - BIF in Filter() 
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Use built-in function 'FILTER' to filter empty value
# E.g., To filter 'None' in str_list
new_list = list(filter(None, str_list))
print("After removing empty strings")
print(new_list) """

# Activity 1G | 4 Pieces of code that each produce one following errors
"""
- Syntax Error = Semantic Error
- Indent Error = Incorrect Indentation
- Type Error   = Wrong Operation applied to Func or Object
- ZeroDivisionError = Second operand of division is an error

Q1G Syntax Error
int(value) = 12.3
print(int)

#Q1G Indent Error
list = ['Dog', 'Cat', 'Mouse']
    print(list) 

#Q1G Indent Error
ltr = str('House') / 2
print(ltr) 

#Q1G ZeroDivision Error
x = 5
y = 0
z = x/y
print(z) """