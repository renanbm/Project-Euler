import math

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f += 6
        return True

def LargestPrimeFactor(numero):
    largestfactor = 0
    CurrentDivider = 3
    while True:
        if isPrime(CurrentDivider) and numero % CurrentDivider == 0:
            numero = numero / CurrentDivider
            largestfactor = CurrentDivider
            if numero == 1:
                break
        CurrentDivider += 2
    return largestfactor

print(LargestPrimeFactor(600851475143))
