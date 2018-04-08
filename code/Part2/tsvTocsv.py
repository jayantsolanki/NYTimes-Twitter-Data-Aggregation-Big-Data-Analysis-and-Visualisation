from itertools import repeat
import csv

with open('output_new2/part-00000','rb') as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)

    for row in tsvin:
        count = int(row[4])
        if count > 0:
            csvout.writerows(repeat(row[2:4], count))