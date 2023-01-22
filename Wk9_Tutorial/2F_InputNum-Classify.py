# Task 2F - Write a program, asks user for Num and Classifies it
"""
number <2 SMALL
number <10 MEDIUM
number rest LARGE
Use try-except where needed.
"""

Input = print(input(str("Input a Number Please... ")))
Input_int = int(Input)
print(type(Input_int))
#if Input_int >=  10:
   # print("MED")
#else:
   # print("NOT MED")


"""try:
    if Input > 2:
        print("SMALL")
    elif Input < 10:
        print("MEDIUM")
    elif Input < 11:
        print("LARGE")
except Exception:
    print("Sorry", Input)
finally:
    print("bye")"""