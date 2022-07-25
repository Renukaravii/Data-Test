import shutil
shutil.unpack_archive(input("enter source zip file"),'C:\\Users\\z032359\\Desktop\\New folder')
file = open("C:\\Users\\z032359\\Desktop\\New folder\\sample.txt","r")
data = file.read()
pattern = input("enter word to count")
occurrences = data.count(pattern)
print('occurence of the word',occurrences)
