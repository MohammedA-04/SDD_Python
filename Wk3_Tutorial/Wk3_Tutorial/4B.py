# Write a program iterates from 1 to 50

for i in range(51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i %3 == 0:
            print("Fizz")
        elif i %5 == 0:
            print("Buzz")
        else:
            print("Not x3 or x5... = ", str(i))



