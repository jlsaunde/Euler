# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from math import sqrt

def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    if n <= 2:
        return True
    if n % 2 == 0:
        return False

    counter = 3 # The first odd divisor is 2.
    stopPoint = sqrt(n)
    while counter <= stopPoint:
        if n % counter == 0: return False
        counter += 2


    return True

def sumPrimesBelow(n):
    sum = 0
    counter = 1

    while counter < n:
        if isPrime(counter):
            sum += counter
        counter += 1

    return sum

print(sumPrimesBelow(2000000))