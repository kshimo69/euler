#!/usr/bin/env python
# coding: utf-8
# http://projecteuler.net/index.php?section=problems&id=17

letters = {
        0:'',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
        #100:'hundred',
        #1000:'thousand',
        }

def fill_letters(n):
    for i in range(1, n+1):
        letter = ""
        if i / 1000 > 0:
            letter += letters[1000 * (i / 1000) / 1000] # 'one'
            letter += 'thousand'
            if i % 1000 != 0:
                letter += 'and'
            letter += letters[i % 1000]
        elif i / 100 > 0:
            letter += letters[i / 100] # 'one'
            letter += 'hundred'
            if i % 100 != 0:
                letter += 'and'
            letter += letters[i % 100]
        elif i / 20 > 0:
            if i % 10 == 0:
                letter = letters[i]
            else:
                letter += letters[i / 10 * 10] # 'twenty'
                letter += letters[i % 10]
        else:
            letter = letters[i]
        letters[i] = letter

def count_letters(n):
    sum = 0
    for i in range(1, n+1):
        #print "letters[%d]: %s" % (i, letters[i])
        sum += len(letters[i])
    print sum

fill_letters(1000)
count_letters(1000)
