#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt


Depths=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip("\r\n").split("\t")
        columns = fields[7].split(";")
        deptp = columns[7].split("=")
        #print(deptp)
        values = deptp[1].strip("\r\n").split(",")
        bettervalues = values[0]
        Depths.append(bettervalues)
count = len(Depths)#



alleles=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip("\r\n").split("\t")
        columns = fields[7].split(";")
        alleletp = columns[3].split("=")
        #print(deptp)
        values = alleletp[1].strip("\r\n").split(",")
        betteralleles = values[0]
        alleles.append(betteralleles)
count2 = len(alleles)


Quals=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip("\r\n").split("\t")
        Qual = float(fields[5])
        Quals.append(Qual)
count3 = len(Quals)


Variants = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip("\r\n").split("\t")
        columns = fields[7].split(";")
        #yucky = columns[-1].split("=")
        for item in columns:
            anewlist = item.split("=")
            if anewlist[0] == "ANN":
                anewerlist= anewlist[1].split("|")
                #print( anewerlist[1] )
                if anewerlist[1] == " ": #or "ERROR_CHROMOSOME_NOT_FOUND":
                    continue
                else:
                    Variants.append(anewerlist[1])
vardic = {}
for item in Variants:
    if item in vardic:
        vardic[item] += 1
    elif item == "":
        continue
    else:
        vardic[item] = 1
        
        
varkeys = list(vardic.keys())

Varval= []
for i in varkeys:
    if i in vardic:
        Varval.append(vardic[i])

fig, axes = plt.subplots(nrows=2,ncols=2)
axes = axes.flatten()

fig.set_size_inches(20,12)

axes[0].hist(alleles, bins = 200, color = "black")
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Position')
axes[0].set_title('Allele')

axes[1].hist(Depths, bins = 200, color = "black")
axes[1].set_xlabel('position')
axes[1].set_ylabel('read depth')
axes[1].set_title('Depth')

axes[2].hist(Quals, bins = 200, color = "black")
axes[2].set_xlabel('Quality')
axes[2].set_ylabel('Position')
axes[2].set_title('Quality')


axes[3].bar (varkeys, Varval)
axes[3].set_xlabel( 'types' )
axes[3].set_ylabel( 'frequency' )
axes[3].set_title ("effects of variant")
#axes[3].set_xticklabels(rotation='vertical')
plt.title( "allele effects " )

plt.savefig('hereis4graphs.png')
plt.close(fig)
