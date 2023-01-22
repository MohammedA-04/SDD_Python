def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False #N9 % by any num 2-8 = 0 then its False
        return True          #Otherwise True
print(test_prime(9))
