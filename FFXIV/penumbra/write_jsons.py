# Requirements:
# JSON5 for python

# For each %mod%/meta.json in your root directory, write its Name to nameList.txt, and Author to authorList.txt
# i.e. nameList = (Kartoffel's Awesome Mod, Kartoffel's second Awesome Mod)'; authorList = (Kartoffel, Kartoffel)

import glob
import sys
import json5

with open(sys.argv[1]+"_nameList.txt", encoding="utf-8") as f:
    nameLines = f.read().split('\n')

with open(sys.argv[1]+"_authorList.txt", encoding="utf-8") as f:
    authorLines = f.read().split('\n')
n = 0
for f in glob.glob(sys.argv[1] + "/**/meta.json", recursive=True):
    print(f)
    with open(f, "r", encoding="utf-8") as j:
        data = json5.load(j)
        print(data)
        data['Name'] = nameLines[n]
        data['Author'] = authorLines[n]
        print(data)
    with open(f, "w", encoding="utf-8") as j:
        j.write(json5.dumps(data))
    n = n + 1
