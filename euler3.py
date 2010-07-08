#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=3

def prime_check(num):
    for i in range(2, num):
        if(num % i == 0):
            return None
    return True

def prime_division(num):
    sum = 1
    i = 2
    while True:
        if(num % i == 0 and prime_check(i)):
            sum *= i
        if(sum == num):
            print i
            return
        i += 1

prime_division(13195)
prime_division(600851475143)
