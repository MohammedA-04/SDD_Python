i = 0
product = 1
count = int(input("Enter Count Number: "))

# For Loop
for i in range(count): #2 Counts
    x = float(input("Enter a real number: "))
    product = product * x
    # Product Numbers are = Count x Product
    # E.g Count is 2
        # RNum is 4 [1x4 = P4]
        # RNum is 8 [P4 X 8 = P8]
            # Product Number of Rnums is 32 [4*8 is 32]
print("The product of the numbers is: ", product)


