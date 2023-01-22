# def name(): // Creating Your Own Function Just like built-in funcitons

# Ex1
print("Example 1")
def greet():
    print("Hi there")
    print("Welcome aboard")
greet()

# Ex2
print("\nExample 2") # greet('Parameter')
def greet(First_Name, Last_name):
    print(f"Hi {First_Name} {Last_name}")
    print("Welcome aboard\n")
    #greet('Arguments')
greet("Mohammed", "Ahmed")
greet("Shan", "Ahmed")


# Ex3
print("\nExample 3\n"
      "Done! Written Hi, Mohammed in Content.txt... \n")
# In Function 2 Types:-
    # 1- Perform a task
    # 2- Return a value
def round(Name):
    return f"Hi {Name}"

Msg = round("Mohammed")
file = open("content.txt", "w") # W = Write
file.write(Msg)

# Ex4
print("Ex 4")
def increment(num, by):
    return num + by
    # result = increment(2,1) = 3
    # print(result)
    # by=1 is kwarg helps you read code easier!
print(increment(2,by=1))

# Ex5
"""
# NB: def incrment(Required Parameter, Optional Parameter):
def increment(number, by=1):
    return number + by
print(increment(2,5))
"""

# Ex6
"""
def multiply(*numbers): #Number(S) // [] = List | () = Tuple, E.g. Immutable
    total = 1
    for number in numbers:
        total *= number # Ttl = Ttl * Number
    return total
print(multiply(2,3,4,5))
"""

# Ex7
"""
def save_user(**user):
    print(user["Name"])
# {Dictonary w Key : Values}
save_user(ID=1, Name="Mo", Age=18)
"""

# Ex8 Variable Scope
# Name Error Msg Not Defined unless parameter is added (name)
# IF NOT CALLED, while later.py release memory allocated for LOCAL-Var
# Output is 'a' | Cuz it's Global Variable & Outside UDF
"""Msg = "a" | # Global Var // Perma-Memory // Outisde UDF
def greet(name):
    Msg = "b"
greet("Mo")
print(Msg)
"""

# Excercise Interview Tough Question
def fizz_buzz(input):
    if (input % 3== 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input
print(fizz_buzz(5))