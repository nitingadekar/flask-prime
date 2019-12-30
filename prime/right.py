#!/usr/bin/python3
import isprime
def rightf(i):
    #i=373
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
        m = int(str(m)[:-1])
       # print ("after" + str(m))
        length=len(str(m))
    #print (m)
   # print (isprime.checkprime(m))
    return isprime.checkprime(m)


#rightf(700)
#print ( rightf(373) )
