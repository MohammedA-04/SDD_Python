# 1C Return Mutliple Values from a function
# >>> Add = 50 [a(40) + b(10)]
# >>> Subtract 30 [a(40) - b(10)]

def calculation(a, b):
    addition = a + b
    subtraction = a-b
    return addition, subtraction

add, sub = calculation(40, 10)
print(add, sub)
