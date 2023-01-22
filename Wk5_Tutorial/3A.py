# Act 3A - Find Value 20 in List and Replace w 200 on the 1st occurance of '20'
list1 = [5,10,15,20,25,20]
index = list1.index(20)
list1[index] = 200
print(list1)

""""
- List1 = [List Values]
- Index Variable = List1.Index(20) 
    I.e. Return first index of value ['20']
- Assigning New Value to Var 'Index' in ''list1''
"""

# Another Ex
# So you call the VAR and change it's value
list2 = [5,10,25,20,25,20]
index = list2.index(10)
list2[index] = 100
print()
print(list2)