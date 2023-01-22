"""
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))  # throws  ZeroDivisionError exception, program terminated abnormally.
c = a / b
print("The answer of a divide by b: ", c)

# ### We can handle the above exception using the try…except block. ##
# ####################################################################

try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("The answer of a divide by b:", c)
except:
    print("Can't divide with zero. Provide different number")


## It is good practice to specify an exact exception that the except clause should catch ##
###########################################################################################
try:
     a = int(input("Enter value of a: "))
     b = int(input("Enter value of b: "))
     c = a / b
     print("The answer of a divide by b:", c)
except ValueError as arg:
     print("Entered value is wrong")
     print(arg)
except ZeroDivisionError:
     print("Can't divide by zero")
"""
# Exception objects are full-fledged Python objects – You can give a name to a raised Exception with 'as'


# ## Handle multiple exceptions with a single except clause ##
# ############################################################

# try:
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c = a / b
#     print("The answer of a divide by b:", c)
# except(ValueError, ZeroDivisionError):
#     print("Please enter a valid value")


# ## Using try with finally, code in finally block guarantees of execution.##
# ###########################################################################
# try:
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c = a / b
#     print("The answer of a divide by b:", c)
#
# except(ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
#
# finally:
#     print("Inside a finally block")
#
# ## Using try with else clause. The else block is executed if there is no exception in try. ##
# #############################################################################################


# try:
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c = a / b
#     print("a/b = %d" % c)
#
# except(ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
#
# else:
#     print("We are in else block ")
#
# finally:
#     print("Inside a finally block")

#
#
# ## Raising Exception ##
# #######################
# def simple_interest(amount, year, rate):
#     try:
#         if rate > 100:
#             raise ValueError(rate)
#         interest = (amount * year * rate) / 100
#         print('The Simple Interest is', interest)
#         return interest
#     except ValueError:
#         print('interest rate is out of range', rate)
#
#
# print('Case 1: ', simple_interest(800, 6, 8))
#
# #print('Case 2: ', simple_interest(800, 6, 800))
