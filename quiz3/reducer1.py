#!/usr/bin/env python
import sys
word2count = {}
word2count = {}
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()
    repeated = 0

    #--- split the line into words ---
    words = line.strip().split('\t')
    count = words[1]
    word = words[0]
#    name = words[1]

    try:
        count = int(count)

    except ValueError:
        continue    


    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count


for word in word2count.keys():
        print '%s\t%s'% ( word, word2count[word] )

