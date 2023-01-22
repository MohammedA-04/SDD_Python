# Activity 1B
""" Activity 1B
def fn(x):
    try:
        print(5/x)
    except ZeroDivisionError:
        print("Except Block")
    else:
        print("Else Block")
    finally:
        print("Finally Block")
fn(0)

Output is Except Block and Finally Block this is because 0 is not 5/x
and the Finally Block will be executed regardless of the exceptions """

# Activity 1C
"""
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print("a/b = ", c)
    # Using exception object with the except statement
except Exception as e:
    print("Something went wrong, please check your input")
    print(e)
else:
    print("Hi I am else block")
"
Anything bar a int number will be raised into the Exception block 
Then the else block will also exe
But in case of an error the print function in the exception block executes only
"""


# Activity 1D
"""
grades = input("Please enter your grades, separated by commas: ").split(",")

try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("The grades you entered were in an invalid format.")

Following source code create a short program that prompts the user for a list of grades separated by commas. 
Split the string into individual grades and use a list comprehension to convert each string to an integer. 
It is using a try statement to inform the user when the values they entered cannot be converted.

Explaination: Inside the try clause a list comprehension is used to convert each string to an integer 
and the results are assigned to grades. 
If you need a reminder on how list comprehensions work, take another look at here:

Inside the except clause the message informs the user that their data was in an invalid format.
In a more complete application, the rest of our code working with grades would likely go in an else clause, 
ut we don't have to worry about that here. """

# Activity 1E - Investigate what happens when there is a return in both try and finally clause of a try statment
"""
def func():
try:
	return "Returned from the try clause!"
finally:
	return "Returned from the finally clause!"
print(func())

- Here finally clause is always running so that prints ad interrupts try clause 
- Puts the return in the try clause on HOLD until it runs it own return 
- Finally ends the function execution so we never come back to the try clause
"""

# Acidity 1F
"""
def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non existing index of a list
            do_stuff_with_number(0)

catch_this()

- For loop to loop through each item w range of 20 indexes
- Exception Clause says to avoid IndexError by using function from do_stuff_with_number 
"""