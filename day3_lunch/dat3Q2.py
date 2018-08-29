#!/usr/bin/env python3

import sys

if len(sys.argv) >  1:
    f = open( sys.argv[1])
else:
    f = sys.stdin

names_counts = {}
typbio = {}
for line in f:
    fields = line.rstrip( "\r\n").split()
    if line.startswith("#!"):
        continue
    if "gene" in fields[2]:
        if "gene_biotype" in line:
            for i, column in enumerate(fields):
               if column == "gene_biotype":
                   typbio = fields[i+1]
                   #print( typbio )
                   #break
                   if typbio in names_counts:
                       names_counts[typbio] += 1
                   else:
                       names_counts[typbio] = 1
                
for name, value in names_counts.items():
    print( name, value )
                 

        
    
      