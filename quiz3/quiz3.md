# 1.Result
##question a).
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 8.06.21 PM.png)
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.13.28 PM.png)
##question b).
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 8.05.07 PM.png)
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.21.00 PM.png)
##question c).
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.04.06 PM.png)
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.04.13 PM.png)
##question d).
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.11.27 PM.png)
![](/Users/drake/Desktop/Screen Shot 2019-10-18 at 9.11.35 PM.png)

 The result is that all methods show that **Clinton** and **Obama**'s speech are most similar. And **Reagan** and **Gwbush** are least similar through 3 partition(a,c,d). And question b shows **Bush** and **Obama** are least similar.

# 2.Code
###mapper3_1.py
```
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
                
                word = line[i:i+4]
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
``` 

### mapper3_2.py
```
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
        

```

### mapper3_3.py
```
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
```
### mapper3_4.py
```
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
                word3 = re.sub(r'[^\w]','', words[i+2]).lower()
                print '%s\t%s' % (word1+word2+word3, filepath)
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
```
### reducer3_1.py
```
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
```

### reducer3_2.py
```
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
```

### reducer3_3.py
```
#!/usr/bin/env python
import sys

d = dict()
for line in sys.stdin:
    words = line.strip().split('\t')
    
    if len(words) < 2:
        continue


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
```
### reducer3_4.py
```
#!/usr/bin/env python
import sys

d = dict()
for line in sys.stdin:
    words = line.strip().split('\t')
    
    if len(words) < 2:
        continue


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
```
### run.sh
```
outputfile=$1
hadoop fs -rm -r $outputfile
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files ./mapper.py,./reducer.py -mapper ./mapper.py -reducer ./reducer.py  -input /user/five-books -output $outputfile

```
### each_statistics.sh
```
filename=$3
s1="hadoop fs -cat $3\/\* | grep 'size of file $1.tar' | awk '{s+=\$6} END {print s}'"
s2="hadoop fs -cat $3\/\* | grep 'size of file $2.tar' | awk '{s+=\$6} END {print s}'"
s3="hadoop fs -cat $3\/\* | grep 'intersect' | grep -w $1 | grep -w $2 | awk '{s+=\$11} END {print s}'"
x1=$(eval $s1)
x2=$(eval $s2)
x3=$(eval $s3)
bottom=$(($x1 + $x2 - $x3))
#echo "$(($x3) // ($x1 + $x2 - $x3))"
echo "$1 $2 $x3 $bottom"
```

### total\_pair_statistics
```
filename=$1
declare -a arr=("reagan" "bush" "clinton" "gwbush" "obama")
rm final_statistics.log
## now loop through the above array
for i in "${arr[@]}"
do
        for j in "${arr[@]}"
        do
                if [ "$i" != "$j" ]
                then
                        str="bash each_statistics.sh $i $j $filename >> final_statistics.log"
                        eval $str
                fi
              # or do whatever with individual element of the array
        done
done

cat final_statistics.log | ./cal_similarity.py
```

### cal_similarity.y
```
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
```

# 3. Conclusion
1. Mappers are taking charge of the input and transfer the input as "key = shingles; value = filename" to the reducer, where filename represents the president's name.
2. Reducers will store the  key pair into the set. Since the **same keys will go to the same reducer**, thus we can calculate the intersection between each two presidents. Meanwhile we can get the total shingles for each president.
3. After each reducer finishes their job, all the pata in part-0000's are like below:
	![](/Users/drake/Desktop/Screen Shot 2019-10-19 at 9.22.13 PM.png)
4. Then the formula of union between two presidents(A and B) is:|A| + |B| - |A & B|(intersection) So we only need to collect all the output and do the calculations.
5. I write several scripts in order to make my assembly line more effectively, where:
	
	
	**run.sh**: used for running the hadoop hdfs and restore the result to each shingles 
	**each_statistics.sh**: used for combining two presidents' intersection and union, the sample result is shown above:
	![](/var/folders/ms/gc_h6ryd2c76hxnhd7zmq00w0000gn/T/TemporaryItems/(A Document Being Saved By screencaptureui)/Screen Shot 2019-10-19 at 9.28.59 PM.png)
	**total\_pair_statistics.sh**: This is a loop script to output all the two pair of presidents' intersection and union and then record the results in **final_statistics.log** and call **cal_similarity** to calculate the maximum similarity and minimum similarity. The sample **cal_similarity** output is shown above:
	![](
	/var/folders/ms/gc_h6ryd2c76hxnhd7zmq00w0000gn/T/TemporaryItems/(A Document Being Saved By screencaptureui 2)/Screen Shot 2019-10-19 at 9.33.23 PM.png)
	
	# 4. Command
	```
	./run.sh -outputfile
	```
	```
	./total_pair_statistics.sh -outputfile
	```