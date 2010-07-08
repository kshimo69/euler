#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=9

import sys

c = 1000
while c > 1:
    for b in reversed(range(1,c)):
        if c + b > 1000:
            continue
        for a in reversed(range(1,1000-1-c)):
            if (a + b + c == 1000) and (c**2 - b**2 == a**2):
                print "a:%d b:%d c:%d" % (a, b, c)
                print "%d + %d + %d = 1000" % (a, b, c)
                print "%d + %d = %d" % (a**2, b**2, c**2)
                print a * b * c
                sys.exit()
    c -= 1
