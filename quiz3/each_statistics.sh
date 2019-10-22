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