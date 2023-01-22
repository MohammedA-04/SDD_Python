def StringStrictSubset(s1,s2):
    State = True
    for char in s1:
        if char in s2:
            continue
        else:
            State = False
    return State

s1 = 'tr'
s2 = 'watermelon'
State = StringStrictSubset(s1,s2)
print("tr =", State)

s1 = 'tey'
s2 = 'watermelon'
State = StringStrictSubset(s1,s2)
print("tey =", State)




