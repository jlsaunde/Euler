# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythagoreanTriplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def findTripletProduct():

    #Initialize a, b, c
    a = 1
    b = 2
    c = 3

    #We know that a,b,or,c could never be 32
    #since 32**2 is 1024 itself - this will serve
    #as a rough stop
    stop = 1000

    #First try
    for x in range(stop):
        for y in range(stop):
            for z in range(stop):
                a = x + 1
                b = y + a + 1
                c = z + b + 1
                #print(a, b, c)
                if isPythagoreanTriplet(a, b, c):
                    print(str(a) + " " + str(b) + " " + str(c) + " is a triplet with a sum of " + str(a + b + c))
                    if a + b + c == 1000:
                        return a * b * c

    return 0

print("Triplet product where a + b + c = 1000 is " + str(findTripletProduct()))
