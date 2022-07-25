import csv 
import json 
from collections import Counter
import os
import re
from collections import Counter


os.chdir(r"C:\Users\z032359\Desktop\iii")
csvFilePath = input("enter your input csv file")
jsonFilePath = r'data.json'

def csv_to_json(csvFilePath, jsonFilePath):
    myjson= []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            myjson.append(row)
  
    #convert python mypython to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(myjson, indent=4)
        jsonf.write(jsonString)
          

csv_to_json(csvFilePath, jsonFilePath)
with open("data.json", "r") as f:
    t = f.read().split('\n')
    l=[]
for line in t:
        p=re.compile("(?<=@)[^.]+(?=\.)")#searching pattern matches
        #qualifiers to drop the strings before @ and after .
        new = p.search(line)
        if(new):
            d = new.group(0)#correct matches(complete matched patterns)
            l.append(d)
            

f=Counter(l).most_common()#count the key value pairs in line by line
file = open('result.csv', 'w+', newline ='') 
with file:  
    writer = csv.writer(file)
    writer.writerow(["col1", "col2"])
    write = csv.writer(file) 
    write.writerows(f) 
with open('result.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)