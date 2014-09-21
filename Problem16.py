#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

def problem16():
    sum = 2**1000
    sum_str = str(sum)
    print(sum_str)

    total = 0
    for c in sum_str:
        total += int(c)

    print(total)

problem16()