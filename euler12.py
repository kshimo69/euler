#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Triangle(object):
    """
    f(T1) = f(1) * f(2/2) => 1(1)
    f(T2) = f(2/2) * f(3) => 2(1,2)
    f(T3) = f(3) * f(4/2) => 4(1,2,3,6)
    f(T4) = f(4/2) * f(5) => 4(1,2,5,10)
    f(T5) = f(5) * f(6/2) => 4(1,3,5,15)
    f(T6) = f(6/2) * f(7) => 4(1,3,7,21)
    f(T7) = f(7) * f(7/2) => 6(1,2,4,7,14,28)
    
    non even number: f(n) * f((n+1)/2)
    even number    : f(n/2) * f(n+1)
    """
    def __init__(self):
        self.prime = {1:1, 2:2, 3:2, 4:3}

    def get_triangle(self, n):
        """ return Nth triangle number
        
        Tn = n * (n + 1) / 2
        """
        return n * (n + 1) / 2

    def search_divisors(self, n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count

    def get_count(self, n):
        if n in self.prime:
            #print "f(%d) is %d" % (n, self.prime[n])
            return self.prime[n]
        else:
            self.prime[self.get_triangle(n)] = self.search_divisors(n)
            #print "f(%d) is %d" % (n, self.prime[self.get_triangle(n)])
            return self.prime[self.get_triangle(n)]

    def count_divisors(self, n):
        if n % 2 != 0:
            return self.get_count(n) * self.get_count((n+1)/2)
        else:
            return self.get_count(n/2) * self.get_count(n+1)

tri = Triangle()
c = 0
i = 1
while c < 500:
    c = tri.count_divisors(i)
    i += 1
print "%d, its divisors: %d" % (tri.get_triangle(i),c)
