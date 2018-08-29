#!/usr/bin/env python3

import sys

if len(sys.argv) >  1:
    f = open( sys.argv[1])
else:
    f = sys.stdin

min_dist = 1000000000000000000000    

for line in f:
    fields = line.rstrip( "\r\n").split()
    if line.startswith("#!"):
        continue
    if fields[0] != "3R":
        continue
    if "gene" in fields[2]:
        if "protein_coding" in line:
             
            gene_start = int( fields[3])
            gene_end = int( fields[4])
            my_dist = 0
            #takes sys.argv[2] as the number tou are looking for
            if int( sys.argv[2] ) < gene_start:
                my_dist = gene_start - int( sys.argv[2] )
            elif int( sys.argv[2] )> gene_end:
                my_dist = int( sys.argv[2] ) - gene_end
        
            if my_dist < min_dist:
               min_dist = my_dist
               if "gene_name" in line:
                   for i, column in enumerate(fields):
                      if column == "gene_name":
                          cistron_name = fields[i+1]
                          
print( min_dist, cistron_name )