#!/bin/bash
rm -r output_new2/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.3.jar -input input/ -output output_new2/ -mapper wordcount_mapper.py -reducer wordcount_reducer.py -numReduceTasks 1
cat output_new2/part-00000 > output_new2/topic.csv