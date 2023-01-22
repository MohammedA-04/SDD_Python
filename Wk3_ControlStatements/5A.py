# Prime Number
# PM is Number > 1 which can has only two factors
    # Factor is the numbers * to make up a any number
    # Any number with more than 2 fcators isn't a Prime Number


UserInput = input("Input Number Between 0-100?")


"""for i in range(UserInput):
    PM = True
        for 
    if i % UserInput == 0 :
        print("Numbers which are Prime Numbers.. = ", UserInput)
    else:
        print("None of these numbers are Prime Numbers")"""

min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)