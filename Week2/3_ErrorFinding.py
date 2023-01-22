num1 = 4
num2 = 3
num3 = 2

num1 += num2 + num3   # Newest Value due to Top-Down
print(num1)           # Num1 *NEW VALUE Is [9]* = Num1 + [Num2 + Num3]

num1 = num1**(num2 + num3)  # 9PWR[5] = 59,049[9x9x9x9x9]
print(num1)
# A** =B | Is the same as A = A**B
num1 **= num2 + num3  # New Value of Num1 is 59,049
print(num1)           # 59,049**[5] is 717897987691852588770249

num1 = '5' + '5'      # String [5,5] = 55
print(num1)

print(4.00/(2.0+2.0)) # 4/4 = 1
# notice operator precedence
# [2] + [9] * [36-8] / 10  then [2] + ([9]*(28/10 =2.8)= 25.2)
num1= 2 +  9 * ((3 * 12) - 8 ) / 10
print(num1)

num1=24//4//2         # 24 // 4 = 6 // 2 = 3
print(num1)
num1 = float(10)      # Number 10
print (num1)
num1 = float('3.14')  # Float instead of Int
print (num1)

print('Bye' == 'BYE')                         # FALSE
print(10 != 9 and 20 >= 20)                   # True + True = True
print(10+6*2**2!=9 //4-3 and 29>=29/9)        # 2!=9 = T | 29>=1 = T
print(5%10 + 10<50 and 29 <= 29)              # T + T = T
print((0<6) or (not(10==6) and (10<0)))       # T or ((not(True) = FALSE) and (FALSE)))
                                              #Pt2. T or (F and F) = True
