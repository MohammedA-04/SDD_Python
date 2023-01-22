String = "I am 19 years and 10 months old"

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
# NB the NwStr is made up all String Items which are digits
NewStr = ''.join([item for item in String if item.isdigit()])
print(NewStr)