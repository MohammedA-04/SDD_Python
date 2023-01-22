# 3B Write program to display all prime number within given range

#for i in range(25, 51):
    #if i > 1:  # All Prime Numbers are > 1
        #for j in range(2, i):
            #if (i % 1) == 0:
                #print(i)
  #  else:
      #  print(i)

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

for n in range(1,51):
    if is_prime(n):
        if n == 47:
            print(n)
        else:
            print(n, "",)
