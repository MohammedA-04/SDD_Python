Number = int(input("Hi User, input a EVEN / ODD integer [0-100]"))
# Input Validate
if Number >= 0 and Number <= 100: print('>>> Valid Input')
else: print('>>> Not Valid Input')

# EVEN OR ODD
# An Even number when divided / 2 gives a remainder of 0
# If Remainder is 1 then ODD Number ; otherwise EVEN Num

if (Number % 2) == 0:
    print("The Number Inputted :", Number, "Is an Even Number".format(Number))
else:
    print("The Number Inputted :", Number, "Is an Odd Number".format(Number))





