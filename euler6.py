#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=6

def sum_all(n):
    if(n == 1):
        return 1
    else:
        return n + sum_all(n -1)

def square_all(n):
    if(n == 1):
        return 1
    else:
        return n**2 + square_all(n - 1)

print (sum_all(100) ** 2) - (square_all(100))
