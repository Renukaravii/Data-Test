import os

os.chdir(r"C:\Users\z032359\Desktop\iii\schema")
with open('1.csv', 'r') as file1:
    with open('2.csv', 'r') as file2:
        difference = set(file1).difference(file2)

difference.discard('\n')

with open('diff.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)