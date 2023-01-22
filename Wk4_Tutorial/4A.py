# 4A  Python function to check whether a number is perfect or not

def PerfectNum(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(PerfectNum(6))




