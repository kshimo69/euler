#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=1

s = 0
for n in range(1000):
    if(n % 3 == 0 or n % 5 == 0):
        s += n
print s
