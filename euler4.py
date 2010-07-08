#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=4

import sys

num = 999*999
while True:
    s = str(num)
    if(s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3]):
        #print "s: %s" % s
        n = 999
        while n > 99 and num / n < 999:
            if(num % n == 0):
                print s
                print "%d, %d" % (n, num / n)
                sys.exit()
            n -= 1
    num -= 1
