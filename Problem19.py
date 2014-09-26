# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def count_sundays(start, end):
    count = 0
    for a_day in daterange(start, end):
        if a_day.weekday() == 6 and a_day.day == 1: #First Sunday of month
            count += 1
    return count

print(count_sundays(date(1901, 1, 1), date(2000, 12, 31)))