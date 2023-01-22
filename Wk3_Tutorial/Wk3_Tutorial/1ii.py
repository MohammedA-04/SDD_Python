num = 75869
count = 0               # C is Qty of Divsion's
while num != 0:         #pt2 to get 'num' floor division until it equals 0
    num = num // 10     # Floor Dvision [Rounds Down]
    count = count + 1   # Increment Counter by 1
print("Total digits are:", count)

