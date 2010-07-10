#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=16

n = 2**1000
l = [str(n)[i] for i in range(len(str(n)))]
sum = 0
for i in l:
    sum += int(i)
print sum
