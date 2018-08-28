#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )    
else:
    f = sys.stdin

count = 0    
sumQ = 0     

for line in f :
    if line.startswith( "@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[4] != "*":
        count += 1
        sumQ += float(fields[4])
average = float(sumQ / count)

       
print(average)       
       