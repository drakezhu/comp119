#!/usr/bin/env python
import sys
import os
import json
import re
import subprocess
class Mapper:

    
    def MAP(self):
#--- get all lines from stdin ---
        
        
        #n = 3


        filepath = os.environ["mapreduce_map_input_file"]
        #filepath = "aa/bb/cc/ss/real.rar"
        filepath = filepath.split("/")[-1]
        #pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        #line = sys.stdin.readline()
        #print "%s" % filepath

        #print "%s\t%s" % ("beor","ss.rar")

        for line in sys.stdin:
               #--- remove leading and trailing whitespace---
            line = line.strip()
                               #filepath = "123"
                                   #--- split the line into words ---
            words = line.split()

            #--- output tuples [word, 1] in tab-delimited format---
            for i in range(len(words)-2):
                word1 = re.sub(r'[^\w]','', words[i]).lower()
                word2 = re.sub(r'[^\w]','', words[i+1]).lower()

                print '%s\t%s' % (word1+word2, filepath)
'''
        for lines in fl:
            words = lines.split()
            

            for i in range(len(words)-1):
                
                #words[i] = pattern.findall(words[i])
                #words[i+1] = pattern.findall(words[i+1])
                words[i] = re.sub(r'[^\w]','', words[i])
                words[i+1] = re.sub(r'[^\w]','', words[i+1])
                
                print (words[i].lower() + "|" + words[i+1].lower() + " " + "1")
'''
        


exp = Mapper()
exp.MAP()