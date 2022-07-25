import os
import csv

from sqlalchemy.util import counter

os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
import pandas as pd
df = pd.read_csv ('flexis.csv')
duplicateDFRow = df[df.duplicated(keep='last')]
print(duplicateDFRow)
P=df.value_counts(dropna=False).reset_index(name='count')
print(P)
P.to_csv(r'fl.csv')
"""dfObj = pd.DataFrame(df, columns=['no','name'])

# Find a duplicate rows
duplicateDFRow = dfObj[dfObj.duplicated(keep='last')]
print(duplicateDFRow)"""