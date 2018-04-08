#!/bin/bash
rm -r output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.3.jar -input input/ -output output/ -mapper wordcount_mapper.py -reducer wordcount_reducer.py -numReduceTasks 1
cat output/part-00000 > output/topic.csv