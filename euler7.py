#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=7

import sys

def prime_check(num):
    n = 2
    while n < num:
        if(num % n == 0):
            #print "%d is not prime." % num
            return None
        n += 1
    return True

def prime_division(num):
    start = 3
    count = 2
    next_num = 0
    while True:
        if(prime_check(start+2)):
            count += 1
            next_num = start + 2
        if(prime_check(start+(2**2))):
            count += 1
            next_num = start+(2**2)
        if count == num:
            print next_num
            sys.exit()
        if next_num == start:
            next_num += 1
        start = next_num

#prime_division(6)
prime_division(10001)
