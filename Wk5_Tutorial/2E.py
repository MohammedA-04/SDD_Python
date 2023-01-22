# Act 2E - Write TWO Functions in your program One to MAX Num Other to get MIN Num in List
def min_max_list(numbers, min_max):

    if min_max == "min":
        min = numbers[0]
        for num in numbers:
            if min > num:
                min = num
        return min

    elif min_max == "max":
        max = numbers[0]
        for num in numbers:
            if max < num:
                max = num
        return max


print(min_max_list([2,9,3,8,7,5], "min"))
print(min_max_list([2,9,3,8,7,5], "max"))


"""
- if printed 'min' then
    min = numbers from numbers[0]
    for each num in numbers
        if min[0] is > than num in numbers[0]
        then min = num 
        return min
"""

# Another Method
print('\n Method 2 | Def Function')
def Max_num(list):
    Max = list[0]
    for A in list:
        if A > Max:
            Max = A
    return Max

def Min_num(list):
    Min = list[0]
    for A in list:
        if A < Min:
            Min = A
    return Min
print(Max_num([1, 3, -4, 7, 12]))
print(Min_num([1, 3, -4, 7, 12]))
