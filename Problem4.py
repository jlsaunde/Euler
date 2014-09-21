#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindrome():
    product = 0
    k = j = 999

    while(k > 99):
        while(j > 99):
            val = k*j
            if isPalindrome(val):
                if val > product:
                    product = val
            j -= 1
        j = 999
        k -= 1

    return product

def isPalindrome(num):
    return str(num) == str(num)[::-1]

print('The largest palindrome is ' + str(largestPalindrome()))
