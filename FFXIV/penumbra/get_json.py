# Requirements:
# JSON5 for python

# For each line in nameList, descriptionList, authorList, write the line to respective meta.json
# i.e. Name = Kartoffel's super cool mod, Author = Kartoffel


import glob
import sys
import json5


n = 0
nameList = []
authorList = []
descriptionList = []
for f in glob.glob(sys.argv[1] + "/**/meta.json", recursive=True):
    print(f)
    with open(f, "r", encoding="utf-8") as j:
        data = json5.load(j)
        print(data)
        nameList.append(data['Name']+'\n')
        authorList.append(data['Author'] + '\n')
    n = n + 1
with open(sys.argv[1]+"_nameList.txt", "w", encoding="utf-8") as t:
    t.writelines(nameList)
with open(sys.argv[1]+"_authorList.txt", "w", encoding="utf-8") as t:
    t.writelines(authorList)
