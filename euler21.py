#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=21

divisers = []
for i in range(10000+1):
    n = 0
    for j in range(1,i/2+1):
        if j == 1:
            n += 1
            continue
        if i % j == 0:
            n += j
    divisers.append(n)

sums = 0

for i,v in enumerate(divisers):
    if v == []:
        continue
    if v >= 10000:
        continue
    if i == v:
        continue
    if i == divisers[v]:
        #print "divisers[%d] = %d divisers[%d] = %d" % (i, v, v, i)
        sums += v
    else:
        continue

print sums
