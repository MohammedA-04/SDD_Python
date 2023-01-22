String = "W@#yn26at^&i9ve"
strCount = 0
digitCount = 0
symCount = 0

for s in String:
    if s.isalpha():
        strCount += 1
    elif s.isdigit():
        digitCount +=1
    else:
        symCount +=1
print(f'Chars = {strCount}, Digit = {digitCount}, Symbol {symCount}')
# Confused my slef with C Programming X++ WRONG
# X+1 CORRECT