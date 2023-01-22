# 3C Copy element 44 and 55 from the following tuple into a new tuple
# Index: 3 and 4
print('Slicing Index 3 & 4')
Tuple1 = (11,22,33,44,55,66)
Tuple2 = Tuple1[3:5]
print(Tuple2)

# Other Method - Slicing
print("\nTeacher's Solution")
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

# 3D Modify Item 1 (22) of a list inside a following tuple to [222]
# Expected output: tuple1: (11, [222, 33], 44, 55)
Tuple3 = (11,[22,33],44, 55)
Tuple3[1][0] = 222
print('\nReplace [22] wiv [222]')
print(Tuple3)


