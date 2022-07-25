from datetime import datetime
import re

l=['04-04-2022 22:13','04-04-2022 22:13','04-04-2022 22:13']
k=["1.2","1.3","1.5","1"]
m=['rrr','r']
n=["04-05-2022","04-05-2022","04-05-2022","04-05-2022"]

def g(dates):
        try:
            for x in dates:
                lk = [datetime.strptime(x, '%m-%d-%Y %H:%M')]

            count = 0
            for j in lk:

                count = count + 1
                if count > 1:
                    break
                print(type(j))
        except ValueError:
            try:
                for x in dates:
                  DATE = [datetime.strptime(x, '%d-%m-%Y')]

                count = 0
                for i in DATE:

                    count = count + 1
                    if count > 1:
                        break
                    print(type(i))
            except ValueError:
                try:
                    fl = [s for s in dates if re.match(r'\d+(?:\.\d+)+$', s)]

                    int = []
                    for item in dates:
                        for subitem in item.split():
                            if (subitem.isdigit()):
                                int.append(subitem)

                    if len(fl) < len(int):
                        print("<class 'int'>")
                    else:
                        if len(fl)==0:
                            print("<class 'str'>")
                        else:
                             print("<class 'float'>")
                except:
                    count = 0
                    for i in dates:

                        count = count + 1
                        if count > 1:
                            break
                        print(type(i))
g(l)
g(k)
g(m)
g(n)
g(k)
