import sys
import shutil
import tempfile
from avro.datafile import DataFileReader
from avro.io import DatumReader
import json
import os
#changing the dir where the input avro file is
os.chdir(r"C:\Users\z032359\Desktop\iii")

#reading the avro file using datafile and datum reader
reader = DataFileReader(open(input("enter the name of the avro file"), "rb"), DatumReader())

#extracting the schema 
schema = reader.get_meta('avro.schema')
parsed = json.loads(schema)
#printing the schema in correct format by giving space
print(json.dumps(parsed, indent=4, sort_keys=True))
#save the schema in user prefred dir
os.chdir(input("enter the dir"))
sys.stdout = open("re.avsc", "w")
print(json.dumps(parsed, indent=4, sort_keys=True))
