#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=20

factorial_nums = {}

def factorial(n):
    if n == 1:
        factorial_nums[1] = 1
        return 1
    elif n in factorial_nums:
        print "has data"
        return factorial_nums[n]
    else:
        factorial_nums[n] = n * factorial(n - 1)
        return factorial_nums[n]

sum = 0
for i in str(factorial(100)):
    sum += int(i)
print sum
