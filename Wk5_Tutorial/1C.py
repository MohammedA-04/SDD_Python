# Activity 1C Execute and Trace
# Addition of elements in a List

# Creating a List
## Prints an Empty List

List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
## Append is used to Add Element to the list
## In the brackets is the value appended

List.append(1)  # Here appends & adds 1 to list called 'List'
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List using Iterator
## Iterator will go through Index 1 to 4(n-1) and Append It
## E..g List [1,2,4, 1,2,3]

for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
## Append Values (5,6) to 'List'
## E.g. List [1,2,4,1,2,3,(5,6)]

List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
## New list 'List2' is Appended to 'List1'
## List [1,2,4,1,2,3,(5,6), ['Thank', 'You']]

List2 = ['Thank', 'You']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# Addition of Element at specific Position (Insert Method)
## Another way Appending via Insert
## List [1,2,4,1,2,3,(5,6) ['Thank You', 'You'] , 3, 12, 0, CFS2160]

List.insert(3, 12)
List.insert(0, 'CFS2160')
print("\nList after performing Insert Operation: ")
print(List)

# Creating a List & Printing It

List = ['S', 'T', 'A', 'Y', 'S', 'A', 'F', 'E']
print("Initial List: ")
print(List)

# Print elements of a range using Slice operation
## SoIndex 4 to 8 SLICED from the list

### Currently in 'List' is ['S', 'T', 'A', 'Y', 'S', 'A', 'F', 'E']
### So the value within [4:8] are printed
#### E.g. [S,A,F,E]

Sliced_List = List[4:8]
print("\nSlicing elements in a range 4-8: ")
print(Sliced_List)
