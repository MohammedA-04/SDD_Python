x=5                       # x += 5 means x = x + 5 (10)
y=2                       # Y *= 2 means Y = Y * 2 (4)
x += 5
y *= 2

print(x - y)                        # 10-4=6
print(x * y)                        # 10*4=40  # (10 % 4) = R2 [2x4=8 | 10-8=r2]
print(x % y)                        # mod calc do how many y can get into x for (x % y) with r as Answer..
print(x // y)                       # 10/4 = 2.5... RD DOWN = 2
print(x ** y)                       # 10 power 4 [10x10x10x10]
print(x >= y)                       # 10 is bigger than 2 = True
print(x != y)                       # 10 is not equal to y = True
print(x <= 10 and y == 2)           # [10<=10 = T] AND [y == 2 = F] = False
print(x <= 10 and not (y == 2))     # [10<=10 = T] AND (not[y == 2 = F] = T) = True
print(x is not y)                   # 10 is not 4 YES TRUE
print(1 + int('2'))                 #SAME
print(str(1) + '2')                 #SAME





# / = float,No Rounding due-to Decimal
# // = int(floor),RoundsDown