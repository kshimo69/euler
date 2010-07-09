#!/usr/bin/env python2.6
# coding: utf-8

import time
from math import sqrt

def profile(__f, *a, **k):
    t = time.time()
    r = __f(*a, **k)
    print '%s: %g sec elapsed.' % (__f.__name__, time.time() - t)
    return r

def prime1(n=10000): #prime1: 9.11336 sec elapsed.
    l = []
    for i in range(2, n):
        if 0 not in [i%j for j in range(2, i/2+1)]:
            l.append(i)
    #print l
    return l

def prime2(n=10000): #prime2: 0.269485 sec elapsed.
    l = []
    for i in range(2, n):
        if 0 not in [i%j for j in range(2, int(sqrt(i))+1)]:
            l.append(i)
    #print l
    return l
    
def prime3(n=10000): #prime3: 0.0911481 sec elapsed.
    l = range(2, n+1)
    for i in range(2, int(n ** 0.5)):
        l = [x for x in l if (x == i or x % i != 0)]
    #print l
    return l

def get_primes_list(n=10000): #get_primes_list: 0.0331881 sec elapsed.
    l = range(n+1)
    l[0] = l[1] = None
    for i in l:
        if not i:
            continue
        elif i**2 > max(l):
            break
        else:
            for multiple_i in range(i+i, n+1, i):
                l[multiple_i] = None
    r = [prime for prime in l if prime]
    #print r
    return r
        
from itertools import ifilter, count
def gen_primes():
    g = count(2)
    while True:
        p = g.next()
        yield p
        g = ifilter(lambda n, p=p: n % p, g)

def _gen_test(n=10000): #_gen_test: 0.516967 sec elapsed.
    #l = []
    for i in gen_primes():
        if i > n:
            break
        #l.append(i)
        print i
    #print l

if __name__ == '__main__':
    profile(prime1,100)
    profile(prime2,10000)
    profile(prime3,10000)
    profile(get_primes_list,10000)
    profile(_gen_test,10000)
