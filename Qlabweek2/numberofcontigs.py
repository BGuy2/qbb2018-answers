#!/usr/bin/env python3

import sys
import fasta
import numpy as np

velvet= fasta.FASTAReader(open(sys.argv[1]))
#spades= FASTAReader(open(sys.argv[2]))

contig_list=[]
len_list=[]

for ident, seq in velvet:
    contig_list.append(seq)
    
for i in range(len(contig_list)):
    length= len(contig_list[i])
    len_list.append(length)
    
len_list.sort()
sumlen=sum(len_list)
meanlen= sumlen / len(len_list)
tots = 0 
startnp50= sumlen // 2

print("number of contigs " + str(len(contig_list)))
print("min " + str(len_list[0]))
print("maximo " + str(len_list[-1]))
print("Avg is" + str(meanlen))

for i in range(len(len_list)):
    tots += len_list[i]
    if tots > startnp50:
        print("N50 is " + str(len_list[i]))
        break


