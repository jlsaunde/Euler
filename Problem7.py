#10001st prime
#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

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

def findNthPrime(n):

    primeCount = 0
    naturalNumberCounter = 1
    lastPrime = 0

    while primeCount < n:
        if isPrime(naturalNumberCounter):
            primeCount += 1
            lastPrime = naturalNumberCounter
        naturalNumberCounter += 1

    return lastPrime

print(findNthPrime(10001))