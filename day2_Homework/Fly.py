#!/usr/bin/env python3

import sys

if len(sys.argv) >  1:
    f = open( sys.argv[1])
else:
    f = sys.stdin
#requires input "./Fly.py filename.txt" due to sys.argv.


for line in f:
    fields = line.rstrip("\r\n").split()
    if "DROME" in line: 
        if fields[-1].startswith("FBgn"):
            print( fields[-1], fields[-2] )


