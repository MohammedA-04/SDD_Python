# Python random number between 0 and 100 using Random built-in module

import random as rand
# Generate random number between 0 to 100

# Pass all three arguments in randrange()
print("First Random Number: ", rand.randrange(0, 100, 1))

# Pass first two arguments in randrange()
print("Second Random Number: ", rand.randrange(0, 100))   # Default step = 1

# Or, you can only pass the start argument
print("Third Random Number: ", rand.randrange(100))       # Default start = 0 | Step = 1

# randint()
# / randint chooses a random number between specified range in ()
# // Eg., print("", rand.randint(100, 1000))
# /// Print a random number 100 and 1000, so it could be 101 or 676 or 999....
print("\nRandint Test ", rand.randint(3,9))

# random.random() function
# / randint() = Random int within range mentioned

# // randrange() = Random number within range using step function also
# // Eg., random.randrange(0,101,10) | Ans Could be: 10 or 20 or 50 or 70 or 100

# /// random.shuffle()  = Method randomly reorders the elements in a list
"""
import random
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
numbers
print(numbers)
One Possible Answer: [67, 12, 65, 23, 45, 43]
"""
