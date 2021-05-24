import math

def isprime(p):
    if p < 2:
        return False
    n = int(math.floor (math.sqrt(p)))
    for j in range(2,n+1):
        if p % j == 0:
            return False
    return True
