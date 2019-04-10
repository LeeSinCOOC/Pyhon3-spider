import csv
import pandas

with open('data.csv','r') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)
        
data = pandas.read_csv('data.csv')
print(data)