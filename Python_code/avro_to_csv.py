from fastavro import reader
import csv
import os
os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
head = True
count = 0
f = csv.writer(open("088.csv", "w+"))
with open('088.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for emp in avro_reader:
        #print(emp)
        if head == True:
            header = emp.keys()
            f.writerow(header)
            head = False
        count += 1
        f.writerow(emp.values())
print(count)