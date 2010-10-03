#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=19

def is_leap_year(year):
    if year % 4 == 0:
        if not year % 400 == 0 and year % 100 == 0:
            return None
        else:
            return True
    else:
        return None

dates = 1
sunday = 0

for year in range(1900, 2001):
    for mon in range(1, 13):
        if dates % 7 == 0 and not year == 1900:
            sunday += 1

        if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
            dates += 31
        elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
            dates += 30
        elif is_leap_year(year):
            dates += 29
        else:
            dates += 28

print sunday
