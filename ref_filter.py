import csv
import json
import sys


commit_list = 'commit_list.csv'
target_type = 'the refactoring operation type you want'


print(target_type)
with open( target_type + '.csv', 'w', newline='', errors='ignore', encoding='utf-8') as out:
    csv_writer = csv.writer(out)
    with open(commit_list, errors='ignore', encoding='utf-8') as raw:
        csv_reader = csv.reader(raw)
        for line in csv_reader:
            if len(line) < 6:
                continue
            for type in line[5:len(line)-1]:
                if type == target_type:
                    csv_writer.writerow(line)

