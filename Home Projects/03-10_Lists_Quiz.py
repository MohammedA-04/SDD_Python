# Question 1+2
stuff = [12, True, "test", 2.71, "ok", 8]
print(stuff[1:4]) #Index 0 = 12, so [2] = "test"

# Question 3
stuff = [5, 1.3, ["cat", "dog", "fish"], "fox", [], 3.14, False]
print(stuff[2][1])

# stuff[2] = Entire List | stuff[2][0] = cat | stuff[2][2] = fish
## Q4 | stuff[2][0][2] = cat -> 't' [Index 2 Char 3 of Cat]

# Q5 | Print Answer = 7 (7 Items)
stuff = [5, 1.3, ["cat", "dog", "fish"], "fox", [], 3.14, False]
print(len(stuff))

# Q7 | pop removes end of a List
stuff = [5, 1.3, ["cat", "dog", "fish"], "fox", [], 3.14, False]
a = stuff.pop() # False
b = stuff.pop() # 3.14
c = stuff.pop() # []
d = stuff.pop() # fox
e = stuff.pop() # list animals
f = stuff.pop() # 1.3
print(f) # F = stf.pop = 1.3 so print 1.3

def fancy_function(my_list):
    thing = 20
    for something in my_list:
        something = something - 2
        thing = thing - something
    return thing
print(fancy_function([5,4,4,3]))

# For 20-3 =17  // [5-2 =3]
# For 17-2 =15  // [4-2 =2]
# For 15-2 =13  // [4-2 =2]
# For 13-1 =12  // [3-2 =1]

# No IDEAO
def fact():
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    return fact(4)

