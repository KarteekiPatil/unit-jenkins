import math

def is_prime(num):
     if n < 0:
        return 'Negative numbers are not allowed'
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    for i in range(2,int(math.sqrt(num))+1):
         if num%i==0:
              return False
    return True
