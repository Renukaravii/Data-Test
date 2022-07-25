from Datatype_foreach_column import *
import csv
import os
from csv import DictReader
from itertools import repeat
os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
with open(input("enter csv"),encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    num = len(next(reader))#count the number of coloumns to autogenerate the list
    bl = [[] for x in repeat(None, num)]
    for row in reader:
     for col in range(num):
            bl[col].append(row[col])

for i in bl:
    g(i)