# What is the output of the following funciton call
## Ans - Emma 25 | Most Recent Line Interpreter Went Thru
def fun1(name, age=20):
    print(name, age)
fun1('Emma', 25)

# What is the output of the following display() funciton call
## Ans -
def display(**kwargs):
    for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000)

# Output Code
## Ans - 15 | print(res)
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)
res = outer_fun(5, 10)
print(res)

# Output Code
## Ans - (8,7)
def add(a, b):
    return a+5, b+5
result = add(3, 2)
print(result)

# Output Code
## Ans - 15
def outer_fun(a, b): #CD
    def inner_fun(c, d): #AB --> A
        return c + d
    return inner_fun(a, b)
    return a #A has no affect
result = outer_fun(5, 10)
print(result)

# Output Code
## Ans - Type Error | IDK
"""
def display_person(*args):
    for i in args:
        print(i)
display_person(name="Emma", age="25") 
"""

"""
*Args    = Prints Number Arg to Function via Tuple
**Kwargs = Prints KeyWOPDS + Nums Arg to Function via Dictonary
"""

# Q8 - *Data | * Is needed that's all
def fun1(*data):
    print(data)

fun1(25,75,55)
fun1(10,20)

# Output Code - Select Correct Funciton Calls
def fun1(name, age):
    print(name, age)

"""
Answer 
- Fun1("Emma", age=23)
- Fun1(age =23, name="Emma")

Other Possible Correct Funtion Calls
- Positional Arg = fun1('Emma', 23)
- Kwargs Argumnt = fun1(name='Emma', age = 23)
- Or Postional Arg doesn't follow kwargs = fun1("Emma", age=23)
"""

# Ans - Name Error | Return Value Function into VAR so we can access it in OUTSIDE the FUNCTION
"""
def fun1(5):
    return num + 25
fun1(5)
print(num)
"""


