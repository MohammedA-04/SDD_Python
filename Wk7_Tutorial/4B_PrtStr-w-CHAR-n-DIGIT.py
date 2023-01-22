str1 = "John25 knows Python &nd Work5 at G00gle as Data Scienti5t"
print("The original string is : " + str1)

res = []
# split string on whitespace --> reverts to original
temp = str1.split()
# Any string has a alpha AND digit is appended via item for loop into res[]
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

# Now res[] has list of thing in them but for print in iterations
print("\nDisplaying words with alphabets and numbers")
for i in res:
    print(i)

