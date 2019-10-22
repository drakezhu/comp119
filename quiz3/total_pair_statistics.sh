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