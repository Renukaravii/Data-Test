import os
import shutil
FILENAMES=[]
for root,dirs,files in os.walk(r"C:\\Users\\z032359\\Desktop\\op\\pan-ingestion-trm",topdown=False):
  for filename in files:
     if(filename.endswith(".java")):
         FILENAMES.append(filename)
         print(filename)
print('\n')
os.chdir(r"C:\\Users\\z032359\\Desktop\\op\\pan-ingestion-trm\\pan-common-trm")
outputs = os.getcwd()
print(outputs)
for FILENAME in FILENAMES:
    f1=open(FILENAME,'r')
    for line in f1:
        if("import") in line:
            print(line)
        else:
            pass
        print('\n')
f1.close