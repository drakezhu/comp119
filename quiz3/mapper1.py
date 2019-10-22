#!/usr/bin/env python
import sys
import os
import json
import re
import subprocess
class Mapper:

    
    def MAP(self):
#--- get all lines from stdin ---

        pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        
        for line in sys.stdin:
            line = line.strip()
            words = line.split()

            for i in range(len(words)-1):
                word1 = re.sub(r'[^\w]','', words[i]).lower()
                word2 = re.sub(r'[^\w]','', words[i+1]).lower()
                print '%s\t%s' % (word1+"|"+word2, "1")

            

                
            



exp = Mapper()
exp.MAP()