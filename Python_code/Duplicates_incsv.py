from collections import Counter
import os

os.chdir(r"C:\Users\z032359\Desktop\iii\schema")

with open('flexis.csv') as f:
   c=Counter(c.strip().lower() for c in f if c.strip()) #for case-insensitive search

for line in c:
         if c[line]>1:
            print (line)
