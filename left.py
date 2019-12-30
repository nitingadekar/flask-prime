#!/usr/bin/python3
import isprime
def leftf(i):
    #i=373
    #print ('inout')
   # print (i)
    m=i
    length=len(str(m))
    #print ("length" + str(length))
    while length > 1:
        if  not isprime.checkprime(m) :
          #  print (isprime.checkprime(m))
            return False 
            break
       # print ("before" + str(m))
        m = int(str(m)[1:])
       # print ("after" + str(m))
        length=len(str(m))
    #print (m)
   # print (isprime.checkprime(m))
    return isprime.checkprime(m)


#print(leftf(700))
#new = leftf(5)
#print ( new )
