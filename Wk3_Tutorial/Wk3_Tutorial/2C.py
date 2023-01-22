# Program Accept Number via User & Calculate Sum of x numbers
i = 0
Sum = 0
count = int(input("What is the amount of numbers you wanna input?"))
for i in range(count):
    x = int(input("Enter a number: "))
    Sum = Sum + x
print ("Product Number is", Sum)