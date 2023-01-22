# Activity 4A
## Write  a program to create a recursive function to calculate the sum of numbers from 0 to 10. A recursive function
## Recurisve = Is a function that calls itself, again and again.
#  Output = 55

def find_sum(number):
   if number == 0:
        return number
   return number + find_sum(number-1)
print(find_sum(10))