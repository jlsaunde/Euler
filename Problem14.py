# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def problem14():
    most_terms = 0
    winning_num = 0
    for num in range(1000000, 1, -1):
        terms = calc_terms(num)
        if terms > most_terms:
            most_terms = terms
            winning_num = num

    print(str(winning_num) + ' wins with ' + str(most_terms) + ' terms.')

def calc_terms(start_num):
    seq = []
    seq.append(start_num)
    workingNum = start_num
    while(True):
        if workingNum % 2 == 0:
            workingNum = workingNum / 2
        else:
            workingNum = (workingNum * 3) + 1
        seq.append(workingNum)
        if workingNum == 1:
            break
    return len(seq)

problem14()
