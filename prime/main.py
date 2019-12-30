#!/usr/bin/python

import isprime
import left
import right
input = 15
#print (isprime.checkprime(10001))
#print (isprime.checkprime(739397))
#print(left.leftf(10001))
#print(left.leftf(input))
#print(right.rightf(input))

def tspcheck(i):
    a = left.leftf(i)
    b = right.rightf(i)
    print ('True') if a == b == True else  print ('False')
    return
