#!/usr/bin/env python3

import sys

if len(sys.argv) >  1:
    f = open( sys.argv[1])
else:
    f = sys.stdin
    
# alright brian: you need to have your second argument (index 1) be the output from question #1. capiche? but your third ones gotta be t_ctab. I think 

flydic = {}
for line in f:
    fields = line.rstrip("\r\n").split()
    flyac = fields[0]
    uniac = fields[1]
    flydic[flyac] = uniac
    
if len(sys.argv) > 1:
    g = open( sys.argv[2])

for line in g:
    fields2 = line.rstrip("\r\n").split("\t") 
    ctabAC = fields2[8]
    if ctabAC in flydic:
        uniac = flydic[ctabAC]
        print( line.rstrip('\r\n') + "\t" + uniac)
    else:
        if len(sys.argv) < 4:
            continue
        else:
            print(line.rstrip('\r\n') + "\t" + "No Match")

        
        

        
        