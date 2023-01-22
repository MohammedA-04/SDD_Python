def list_sum(num_List):  # Sum = 24
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

print(list_sum([2, 4, 5, 6, 7]))
# Cuz it's recurisve its repeatin
# 2+4 = 6 | 6+5 = 11 | 11+6 =17 | 17+7 = 24



