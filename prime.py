import math

def is_prime(num):
     if n < 0:
        return 'Negative numbers are not allowed'
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True
