#!/usr/bin/env python
import sys

D = dict()
Counter = dict()
for line in sys.stdin:
    line = line.strip()
    words = line.strip().split('\t')
     
    key = words[0]
    value = words[1].split('|')[0]
    count = words[1].split('|')[1]
    count = int(count)
    #print "key: %s\tvalue: %s\tcount: %s" % (key,value,count)
    
    if key in Counter:
        Counter[key] += 1
    else:
        Counter[key] = 1


    
    if key in D:
        #print key
        if value in D[key]:
            (D[key])[value] += 1
        else:
            
            D[key][value] = count
    else :
        d = {value:count}
        D[key] = d 

        #print d
    
for x in D:
    for y in D[x]:
        t = float(Counter[x])
        c = float(D[x][y])
        print "%s|%s: %8.2f" %(x,y,c/t)
    
    
    
    
