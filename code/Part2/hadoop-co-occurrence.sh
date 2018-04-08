#!/bin/bash
rm -r output_co/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.3.jar -input input/ -output output_co/ -mapper co_occurence_mapper2.py -reducer co_occurence_reducer.py -numReduceTasks 1
cat output_co/part-00000 > output_co/topic.csv