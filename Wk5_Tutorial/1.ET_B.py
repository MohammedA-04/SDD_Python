# Same Program Different Way

SquareNum = []
for x in range(1, 11):
    if x % 2 == 1:
        SquareNum.append(x ** 2)
print(SquareNum)

"""
Empty List 
for loop 'x' in range (1,2,3,4,5,6,7,8,9,10)
    if x mod 2 == 1
        then append to the variable named SquareNum (x**2)
            (x**2) needed to be done multiple by it slef
                E.g. 4[2] = 16 ,  3[2] = 9
"""