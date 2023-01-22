# Write an algorithm to find the greatest among two different numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Input Validation
if num1 >= 0 and num1 <= 100:
   print('>>> Input 1 is a Valid Input')
if num2 >= 0 and num2 <= 100:
   print('>>> Input 2 is a Valid Input')
   
# Compare both the number
if num1>num2:
   print(num1," = [1st Number] is the largest number.")
else:
   print(num2," = [2nd Number] is the largest number.")

