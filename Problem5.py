#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_number():
    count = 20
    attemptCount = count
    x = 1

    while(attemptCount < 1000000000):
        successCount = 0
        x=1
        while(x <= count):
            val = attemptCount % x
            if val == 0:
                successCount += 1
            x += 1
        if successCount == count:
            return attemptCount
        attemptCount += 1

print("The smallest number is " + str(smallest_number()))