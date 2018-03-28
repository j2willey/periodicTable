#!/usr/bin/python3
#  !/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import json

filename = "periodictable.csv"

with open(filename) as f:
    lines = f.readlines()
#print(lines)
elemDic={}
for  x in lines :
    #print (" ====" + x.rstrip())
    atom = x.split(",")
    elem = {}
    X = elem["X"] = atom[1]
    Y = elem["Y"] = atom[0]
    elem["atomicNumber"] = atom[2]
    elem["name"] = atom[3]
    elem["Sym"] = atom[4]
    elem["atomicWeight"] = atom[5]
    if ( not X in elemDic ) :
        elemDic[X] = {}

    elemDic[X][Y] = elem

#print(elemDic)
print(json.dumps(elemDic) )   
