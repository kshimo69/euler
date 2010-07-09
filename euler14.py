#!/usr/bin/env python2.6
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=14

goal = 1000000
memory = [0 for i in range(goal)]
max_c = [1, 1]

for n in range(2, goal - 1):
    v = n
    c = 0
    while v >= n:
        if v % 2 == 0:
            v = v /2
        else:
            v = v * 3 + 1
        c += 1
    c = c + memory[v]
    memory[n] = c
    if c > max_c[1]:
        max_c = [n, c]
print max_c[0]
