#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=15

def pascal(n, l=[1]):
    if len(l) == n:
        return l
    else:
        new_list = [1]
        for i in range(len(l) - 1):
            new_list.append(l[i] + l[i + 1])
        new_list.append(1)
        return pascal(n, new_list)

l = pascal(1 + 2 * 20)
print l[len(l)/2]
