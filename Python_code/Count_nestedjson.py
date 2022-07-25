import json
import itertools
from collections import Counter
from collections import defaultdict
import os
os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
with open('task.json','r') as employee:
   emp = json.load(employee)
 # -----------multi-list into single list-----------
u = list(itertools.chain(*emp["data"]))
print(u)
# ---------seperated only string from the list------------
d = defaultdict(list)
print(d)
for x in u:
      d[type(x)].append(x)
# ----taking only the needed elements in the  list -----
l=d[str]
r = []
n = len(l)
print(l)
freq = Counter(l)
# --------printing the count of those needed string-------
for i in range(n):
    if (freq[l[i]]>=2):
        r.append(l[i])
s=Counter(r).most_common()
print(s)