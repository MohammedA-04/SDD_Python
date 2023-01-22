# Acitivty 2E | Given "WAtErmvEloN" + Expect Output "trmvloWAEEN"
String = 'WAtErmvEloN'
Lower = []
Upper = []

for s in String:
    if s.islower():
        Lower.append(s)
        # s.append(Upper) | Storage.add(iterator)
    else:
        Upper.append(s)
        #s.append(Lower)

NwString = ''.join(Lower + Upper)
print('Result :', NwString)



