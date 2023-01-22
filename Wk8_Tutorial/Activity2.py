# Activity 2A
"""
class FormulaError(Exception): pass

def UserInputs(inputz):

  input_to_list = inputz.split()
  if len(input_to_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  num1, ops, num2 = input_to_list
  try:
    num1 = float(num1)
    num2 = float(num2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return num1, ops, num2

def calculate(num1, ops, num2):

  if ops == '+':
    return num1 + num2
  if ops == '-':
    return num1 - num2
  if ops == '*':
    return num1 * num2
  if ops == '/':
    return num1 / num2
  raise FormulaError('{0} is not a valid operator'.format(ops))


while True:
  UserInputs = input('>>> ')
  if UserInputs == 'quit':
    break
  num1, ops, num2 = UserInputs(inputz)
  result = calculate(num1, ops, num2)
  print(result)
"""

# Actual Calculator
""" Fully Working Not Copied Sarcasm
class FormulaError(Exception): pass


def parse_input(user_input):
  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2


def calculate(n1, op, n2):
  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise FormulaError('{0} is not a valid operator'.format(op))


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)
"""

# Activity 2B - Fix Errors
"""
def calculate_sum(list_of_expenditure):
    total = 0
    no_values = len(list_of_values)
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total / no_values
        print("Average:", avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")


try:
    list_of_values = [100, 200, 300, 400, 500]
    num_values = len(list_of_values) # = 5
    calculate_sum(list_of_values)    # 1500
except NameError:
    print("Name error occured")
except:
    print("Some error occured")
"""

# Activity 2C - Fix Errors
balance = 1000
amount = "300Rs"


def take_card():
    print("Take the card out of ATM")


try:
    if balance >= int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")
except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()

# Activity 2D
for number in range(10):
# use a if the number is a multiple of 3, otherwise use b

try:
    if (number % 3) == 0:
        message = message + 'a'
    else:
        message = message + 'b'
except NameError:
    print("Name Error")
except:



print(message)
