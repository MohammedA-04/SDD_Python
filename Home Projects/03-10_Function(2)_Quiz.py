"""
Q1 - Two Main Parts of Function is Function Signature and Funciton Body

Ans - Every Function must have both of these as Signature defines funciton names&args
Ans - Function Body holds the code that runs wheneve the funciton is called
"""

# Q2 What's the Funciton Signature Here
## Ans - FS here is Line 10 | def square(num):
def square(num):
    num_squared = num ** 2
    return num_squared


def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    temp_value = other_thing(second_value) # TempV [5] = Otherthing (second_value[5])
    return temp_value

def other_thing(another_value):
    return (another_value + 5) * 3

print(some_thing(13, 10))
# Temp Return so Ans - 5+5*3=30


# Question 6
def surprising_function(value):
    thing = 0
    for counter in range(value+1):
        thing = thing + counter
    return thing

print(surprising_function(5))
# 0,1 = 1
# 1,2 = 3
# 3,3 = 6
# 6,4 = 10
# 10,5 = 15

# Question 7
def a(x, y): # Swapped 12 + 8 = return (x+y) = 20
    x = x + 3 #8
    y = y + 2 #12
    return x+y
x = 5
y = 10
z = a(x, y)
print(z)

def a(x, y): #20
    x = x + 3 #8
    y = y + 2 #12
    return x+y
x = 5
y = 10
z = a(x, y)
print(x) # Call is only for 'x' NOT 'z' print(x) = 5 | Sneaky :)

sentence = "python rocks"
print(sentence[2] + sentence[-3])
# [-3] N-1 Doesn't Apply

sentence = "Greenall"
print(len(sentence))
# print(len(sentence)) = Start with index 1

word = "practice" # Print == 8 Prints as len is 8
for character in word:
    print("Mo-X8")

def apply_rule(character):
    new_character = ""
    if character == "X":
        new_character = "XYF"
    elif character == "Y":
        new_character = "FXY"
    else:
        new_character = character
    return new_character

print(apply_rule("Y"))

# Last Question

def apply_rule(character):
    new_character = ""
    if character == "X":
        new_character = "XYF"
    elif character == "Y":
        new_character = "FXY"
    else:
        new_character = character
    return new_character

def process_string(some_string):
    new_string = ""
    for character in some_string:
        # NS = NS "" + Apply Rule(character) which applies def above in L87
        new_string += apply_rule(character)
    return new_string
print(process_string("XZY")) #xyf z fxy