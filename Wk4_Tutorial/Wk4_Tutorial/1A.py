#  1A | Understand Solution 1 & 2

# Solution 1
#colour = 'green'
#choice = ''

#while choice != colour:
 # choice = input ('Favourite Colour: ')
  #if choice != colour:
     #print ('Ni!')
#print ('You may pass!')

# Solution 2
print()
colour = 'green'
while 1:
  choice = input ('Favourite Colour: ')
  if choice == colour:
    break	# breaks the loop execution.
  else:
    print ('Ni!')
print ('You may pass!')
