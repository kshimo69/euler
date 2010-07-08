#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=10

def make_prime_list(num):
    plist = [] # list of prime numbers
    slist = [] # list of search numbers
    [slist.append(i) for i in range(3,num+1) if i % 2 != 0]
    plist.append(2)
    while plist[-1]**2 < slist[-1]:
        plist.append(slist.pop(0))
        i = 0
        while i < len(slist):
            if slist[i] % plist[-1] == 0:
                slist.pop(i)
                continue
            i += 1
    return plist + slist

s = 0
for i in make_prime_list(10):
    s += i
print s

s = 0
for i in make_prime_list(2*10**6):
    s += i
print s
