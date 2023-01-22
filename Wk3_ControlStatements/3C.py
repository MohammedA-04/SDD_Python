# Write a Python Program that prints each item and its corresponding type
"""
PRINT EACH TYPE
Sample List : Datalist = [1452,11.23, 1+2]
if True 'w3resource'
(0,-1)
[5,12]
"""
DataList = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]

for x in DataList:
    for EachItem in DataList:
        print("Item is : ", EachItem , "is" ,type((EachItem)) )

