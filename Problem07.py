import math

def isPrime(n):
    if n == 0 or n == 1:
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

def WantedPrime(wantedPrime):
    count = 0
    current = 0

    while count < wantedPrime:
        if isPrime(current):
            count += 1
        current += 1

    return (current - 1)

print(WantedPrime(10001))
