#!/usr/bin/env python
import sys

d = dict()
for line in sys.stdin:
    words = line.strip().split('\t')
    pair = words[0]
    filename = words[1]
    

    if filename in d.keys():
        d[filename].add(pair)
        #d[filename]="replaced"
    else:
        s = set()
        d[filename] = s
        d[filename].add(pair)
        
        #d[filename] = "new" 
    #print '%s\t%s' %(pair,filename)
if 'speeches' in d:
    del d['speeches']





cp = d.copy()

for x in d:
    del cp[x]
    for y in cp:
        if y == x:
            continue
        else:
            intersect = len((d[x]) & d[y])
            print 'file1 : %s and file2 : %s\t intersect number is %d' % (x,y , intersect)
    print "size of file %s is %d " % (x,len(d[x]))