import json
import itertools
import os
import numpy as np
import pandas as pd
os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
j=open('task.json')
k = json.load(j)
u = list(itertools.chain(*k["data"]))
np_array=np.asarray(u)
d=np_array.reshape(6,3)
df=pd.DataFrame(d)
df.to_csv('h.csv')
df.columns = ['id', 'name','dept']
print(df.groupby(['dept']).size().reset_index(name='counts'))