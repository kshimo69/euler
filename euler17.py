#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=17

letters = {
        0:0,
        1:len('one'),
        2:len('two'),
        3:len('three'),
        4:len('four'),
        5:len('five'),
        6:len('six'),
        7:len('seven'),
        8:len('eight'),
        9:len('nine'),
        10:len('ten'),
        11:len('eleven'),
        12:len('twelve'),
        13:len('thirteen'),
        14:len('fourteen'),
        15:len('fifteen'),
        16:len('sixteen'),
        17:len('seventeen'),
        18:len('eighteen'),
        19:len('nineteen'),
        20:len('twenty'),
        30:len('thirty'),
        40:len('forty'),
        50:len('fifty'),
        60:len('sixty'),
        70:len('seventy'),
        80:len('eighty'),
        90:len('ninety'),
        100:len('hundredand'), # one hundred 'and' twenty-one
        1000:len('onethousand'),
        }

def fill_letters(n):
    for i in range(1, n+1):
        if i not in letters:
            i
            word_count = 0
            if i / 1000 > 0:
                word_count += letters[1000 * (i / 1000)]
                word_count += letters[i % 1000]
            elif i / 100 > 0:
                word_count += letters[100]
                word_count += letters[i / 100]
                word_count += letters[i % 100]
            elif i / 10 > 0:
                word_count += letters[10 * (i / 10)]
                word_count += letters[i % 10]
            letters[i] = word_count
            #print "letters has %d: %d" % (i, letters[i])

def count_letters(n):
    sum = 0
    for i in range(1, n+1):
        #print "letters[%d]: %d" % (i, letters[i])
        sum += letters[i]
    print sum

fill_letters(1000)
count_letters(1000)
