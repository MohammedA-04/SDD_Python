""""
a.	Get a string made of the first 2 and the last 2 characterss from a user input string.
If the string length is less than 2, return empty string instead.

For example:
User input String : ‘watermelon’ DONE
Expected Result : 'waon'

User input String: 'wa'
Expected Result : 'wawa' DONE

User input String: 'w'
Expected Result : Empty String  CHECK THIS

Hint: use string slicing and concatination.
"""
# Provided a given string
string = 'watermelon'
First_Char_2 = string[0:2]
Last_Char_2 = string[8:10]
print(First_Char_2 + Last_Char_2)
print(First_Char_2*2)

# with a User Input
strIN = str(input('Please type in watermelon or wa or w'))
for char in strIN:
    if strIN == 'watermelon'  or 'Watermelon':
        newstrIN = strIN[0:2]
        newstrIN1 = strIN[8:10]
        newstrIN2 = newstrIN + newstrIN1
    print(newstrIN2)
    break

    elif strIN == 'wa' or 'Wa':
          newstrIN = strIN[0:2]
    print(newstrIN)
    break

    elif strIN == 'w' or 'W':
        newstrIN = strIN[0:0]
    print(newstrIN)
    break

# Using only if ONLY
strIN1 = str(input('Please type in watermelon or wa or w:'))
for char in strIN1:
    if strIN1 == 'watermelon' or 'Watermelon':
        newstrIN  = strIN1[0:2]
        newstrIn2 =strIN1[8:10]
        n3 = newstrIN + newstrIn2
    print(n3)
    break

strIN2 = str(input('Please type in watermelon or wa or w'))
for char in strIN2:
    if strIN2 == 'wa'  or 'Wa':
        newstrIN = strIN2[0:3]
    print(newstrIN)
    break

strIN3 = str(input('Please type in watermelon or wa or w'))
for char in strIN3:
    if strIN3 == 'w'  or 'W':
        newstrIN = strIN3[0:0]
    print(newstrIN)
    break