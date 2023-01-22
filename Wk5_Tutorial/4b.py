# 4B - Task 4
# Example 3**4 is 81 | Ex2 2**8 is 256

def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
        print(power(3,4))
"""
lets say a = 2 | b = 4 | Q 2**4
    - #1 2**4 = 16
    - #2 2**3 = 8
    - #3 2**2 = 4
    - #4 2**1 = 2
    - #5 2**0 = 0
"""
