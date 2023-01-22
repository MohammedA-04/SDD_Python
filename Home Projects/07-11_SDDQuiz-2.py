# Questions on the Quiz that i got WRONG!

# Answer = False
def func3(x):
    return x % 2 == 0
print(func3(-19))

# Answer = [7,27]
num = [7, 8, 120, 25, 44, 20, 27]
for x in num:
    if x % 2 != 1:
        num.remove(x)
print(num)

# Start 10, 5 ; END = 0 Not Included
for i in range(10,0,-5):
    print(i)

"""
for x in range(1,3):
    print(x)
print(5+2*3)

so prints 1,2 1,2 on third iteration the iterable prints 1,4
"""

# Q5 | Recursion depty by default is 1000 and can be modified
# Q6 | n = 300 & m = n
# Q6 Ans = One Object and Two References

# Q7 |
print('7 Activty\n')
for i in range(5):
    if i == 2:
        continue
    print(i)

# Q8
print('\n8 Activty')
for i in range(10,0,-5):
    print(i)

# Q9
print('\n9 Activty')
my_list = ['Mick', 'Tim', 'Richie', 'Gary', 'Sara', 'Mia']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'John':
        print('Found the name John')
        break
        print('After break statement')

print('Loop is Terminated')

# Q10 | DONE in Word
# Q11 |
print('\n10 Activty')
def func7(c):
    f = c * 1.8 + 32
    return f
print(func7(37))

# Q13 | Remove Index [0] and [4] and [5]
colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Ans removes Red, pink, ylw

# Q14 | Trace and Execute
print('\n10 Activty')
def func6(speed):
    mph = speed / 1.6
    return mph

print(func6(32))

# Q15 | Trace & EXE
"""
print('\n14 Activty')
def func1(x):
    return x % 2 == 0
print(func1("20"))
- TypeError : not all arguments converted during string formatting
"""

# Q16 Addtion of the base condition
for x in range(2):
    for y in range(2):
        print(x,y)

# Q18 Print Statement
print('\n Q18')
colours = ["red", "green", "burnt sienna", "blue"]
print("yellow" in colours)

# Q19 Pynative
print('\n Q19')
PatternRows = 6
for i in range(PatternRows, 1, -1):
    for j in range(1, i):
        print(j, end=' ')
    print("\r")

# Q20 | Ans [25, 36, 49, 64, 81]
print('\n Q20')
def startLast():
   l = list()
   for i in range(1,10):
      l.append(i**2)
   print(l[:5])
   print(l[-5:])
startLast()
