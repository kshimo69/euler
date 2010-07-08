#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=2

s = 0

def fibonacci(x, y):
    global s
    if(y > 4*10**6):
        print s
        return
    if(y % 2 == 0):
        s += y
    fibonacci(y, x + y)

fibonacci(1 ,2)
