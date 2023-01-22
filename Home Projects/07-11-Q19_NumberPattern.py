# Q19 Number Pattern
print('\n Q19')
patternrows = 6
for i in range(patternrows, 1, -1):
    for j in range(1, i):
        print(j, end=' ')
    print("\r")