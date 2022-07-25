import numpy as np

from pyspark.sql import SparkSession
from pyspark import SparkContext
import os
import itertools
import json
os.chdir(r"C:\Users\z032359\Desktop\iii\schema")

from operator import add
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, DoubleType, Row

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()
#data = spark.read.text("C:/Users/z032359/Desktop/iii/schema/test.json")
#print("data")
#df = spark.read.text("task.json")
#u = list(itertools.chain(*df["data"]))
#df.printSchema()
#df.show()
with open('task.json','r') as employee:
   emp = json.load(employee)
 # -----------multi-list into single list-----------
u = list(itertools.chain(*emp["data"]))
print(u)

#i=list(map(str, u))
#print(i)
pieces = 6
#new_arrays = np.array_split(u, pieces)
#print(new_arrays)
length_to_split = [3,3,3,3,3,3]

# Using islice
Inputt = iter(u)
Output = [list(itertools.islice(Inputt, elem))
          for elem in length_to_split]
print(Output)
columns = ["num", "name", "dept"]

# creating a dataframe
dataframe = spark.createDataFrame(Output, columns)

# show data frame
dataframe.show()

dataframe.groupBy("dept").count().show(truncate=False)