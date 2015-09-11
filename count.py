import sys
import csv

def count(file, key):
    count_key = 0
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        try:
            for num, row in enumerate(reader):
                for item in row:
                    item = item.lower()
                    if item.count(key):
                        count_key = count_key + 1
            return count_key
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

print count('iowa-liquor-sample.csv','single malt scotch')

    
