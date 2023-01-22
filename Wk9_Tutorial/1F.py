# 1F Generate a random password which meets the following conditions
# / Password len must be 10 Char Long
# // Must contain 2 Upper case at least, 1 digit and 1 Special Symbol

import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation) # Here len is 10

    passwordList = list(password)  # Password into list
    random.SystemRandom().shuffle(passwordList)  # Shuffle the list in Password
    password = ''.join(passwordList) # Join password variable to password list via ''.join
    return password # Return Call

print ("Password is ", randomPassword())
# printing the random paasowrd funciton created as indicated by the YELLOW
