#!/usr/bin/env python
import sys
import os
import json
import re
import subprocess
class Mapper:

    
    def MAP(self):
#--- get all lines from stdin ---
        
        maxVal = 0.0
        minVal = 1.0
        for line in sys.stdin:
            line = line.strip()
            words = line.split()
            
            val = float(words[2]) / float(words[3]) 

            if val < minVal:
                minVal = val
                outMin = words[0] + " and " + words[1]
            if val > maxVal:
                maxVal = val
                outMax = words[0] + " and " + words[1]


        print "Most similarity is %s, which their similarity is: %8.4f" %(outMax, maxVal)
        print "Least similarity is %s, which their similarity is: %8.4f" %(outMin,minVal)






exp = Mapper()
exp.MAP()