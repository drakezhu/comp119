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

        #filepath = "aa/bb/cc/real.rar"
        filepath = os.environ["mapreduce_map_input_file"]
        

        filepath = filepath.split("/")[-1]
        #pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        #line = sys.stdin.readline()
        for line in sys.stdin:
               #--- remove leading and trailing whitespace---
            line = line.strip()
                               #filepath = "123"
                                   #--- split the line into words ---
            words = line.split()
                                                   #--- output tuples [word, 1] in tab-delimited format---
            line = re.sub(r'[^\w]','',line)
            for i in range(len(line)-1):
                
                word = line[i:i+7]
                #if 'tar' not in filepath:
                #    print "word: %s\t filepath: %s" %(word,filepath)
                print '%s\t%s' % (word.lower(), filepath)
        
            #print "111_111"
            #print "www_temp.rar"
            #print "qqq_tt.rar"
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
        
