# 4C Write Program accpets String only and calclulates num of digits or letters
    # isdigit() - Checks whether its a digit or not
    # isalpha() - Checks whether its a Alphabet [a-z] or not

UserInput = str(input(" Please input something... "))
Digit=Char=0

for Inputs in UserInput:
    if Inputs.isdigit():
        Digit += 1
    elif Inputs.isalpha():
        Char +=1
    else:
        pass # Pass Code
print("Numbers: " ,Digit)
print("Characters:",Char)
