#!/usr/bin/env python3

import sys 

inpoot= open(sys.argv[1])
outpoot= open(sys.argv[2], "w")

for line in inpoot:
    fields = line.rstrip("\r\n").split()
    outpoot.write( '>' + fields[0] + "\n")
    outpoot.write(fields[1] + "\n")
    
outpoot.close()