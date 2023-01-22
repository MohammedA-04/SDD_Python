# Act 2D - Reverse TWO Lists simultaneously
# #### E.g. A = [1234] via  a[::-1] Now Equal [4321]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1,list2[::-1]):
    print(i,j)


"""
- Zip = Aggregates TWO Lists
- Two Lists mean Two Iterators + Print Both

- [::1] = START the list from the Last Index 
    E.g. list2[::1]  = 400, 300, 200, 100

- list1 = won't change as dosen't apply to list1
    E.g. list1 = 10, 20, 30, 40
    
- pritn(i.j) 
        i1 , j1
        i2 , j2 and so on....
"""






