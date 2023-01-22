x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

"""
x(0) |  a(0) | b(-5)
if a(0) > 0    [False]
    if b(-5) < 0   [Ignore Till Else Final]
         x = x + 5 [x(5)]
    elif a(0) > 5 
        X = X + 4 is.. 4 [Ignore]
    else 
        x = X + 3 is.. 3 [Ignore]
else [Execute]
    then x is 2
    print (x)
>>> 2         
"""