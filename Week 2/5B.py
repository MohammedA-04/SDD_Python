first = 1.0
second = "1"
third = "1.1"
# NEEDS TIME
# Which one will print(2.0)
print(first + float(second))            # 2.0 = 1 + 1 [TICK]
print(float(second) + float(third))     # 2.1 = 1 + 1.1

#print(int(first) + int(third))
print(first + int(float(third)))         # 2.0 = 1.0 + 1 [TICK]
print(int(first) + int(float(third)))    # 2= 2 * 1
print(2.0 * int(second))




