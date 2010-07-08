#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-
# url: http://projecteuler.net/index.php?section=problems&id=5

import sys

hoge = 2520
i = 2
while True:
    num = hoge * i
    list = [ n for n in range(1,21) if num % n == 0 ]
    if(len(list) == 20):
        print num
        print list
        sys.exit()
    i += 1
