# Creating a Dictionary w Integer Keys
Dict = {1: 'Welcome', 2: 'to', 3: 'CFS2160'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict) # Prints Out The Dictionary in L3

# Creating a Dictionary w Mixed keys
##  E.g. {'Name': 'John', 1: [1, 2, 3, 4]}
Dict = {'Name': 'John', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict) # Prints Out Dict in L9

# Accessing a element using key
# ## Accesses Key called 'Name' then print VALUE = 'John'
print("\nAccessing a element using key:")
print(Dict['Name'])

# Accessing a element using key
# ## Prints Key '1' which is [1, 2, 3, 4]
print("\nAccessing a element using key:")
print(Dict[1])
