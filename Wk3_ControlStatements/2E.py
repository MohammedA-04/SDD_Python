#2E Program HARD
Num = [12,75,150,180,145,525,50]

#print("These are the numbers divisble by 5", DivBy5)
DivBy = [ item for item in Num if item % 5 == 0]
print(DivBy) # 75,150,180,145,525,50

for i in DivBy:
    if i > 150:
        pass #Nested if
    if i > 500:
        print("This Value is... i > 500 =", i)








