outputfile=$1
hadoop fs -rm -r $outputfile
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files ./mapper.py,./reducer.py -mapper ./mapper.py -reducer ./reducer.py  -input /user/five-books -output $outputfile