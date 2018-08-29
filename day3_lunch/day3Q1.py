#!/usr/bin/env python3

import sys

if len(sys.argv) >  1:
    f = open( sys.argv[1])
else:
    f = sys.stdin

count = 0
for line in f:
    fields = line.rstrip( "\r\n").split()
    if line.startswith("#!"):
        continue
    if "gene" in fields[2]:
        if "protein_coding" in line:
            count += 1
print( count )
            