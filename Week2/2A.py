# Python Program to SWAP 2 Numbers using 3 Variable

a = int(input(" Input First Number  : ")) # Input 1
b = int(input(" Input Second Number : ")) # Input 2

TemporaryVAR = a    # Temp is placeholder to swap value later on
a = b               # [a(1),b(2)] are Equal so new the Value of A is 2
b = TemporaryVAR    # Now is B new value is 1 cuz Temp has value of 1

print("Swapping....")
print(f"Value stored in A is {a}")
print(f"Value stored in A is {b}")


