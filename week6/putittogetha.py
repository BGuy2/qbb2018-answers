#!/usr/bin/env python3

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

"""
Do really cool things with 
mus.musculus features.bed gained.bed lost.bed
"""

#first we gonna count the number lost and gained

gained= open(sys.argv[2])
lost= open(sys.argv[3])
mouse = open(sys.argv[1])

feat_dic = {}
for line in mouse:
    fields = line.rstrip("\r\n").split("\t")
    start = int(fields[1])
    end = int(fields[2])
    feature = fields[3]
    for bp in range(start, end):
        feat_dic[bp] = feature

countg=0
overall_gain = []
for i, line in enumerate(gained):
    countg += 1
    feats_gain = []
    fields = line.rstrip("\r\n").split("\t")
    startg = int(fields[1])
    endg = int(fields[2])
    for bp in range(startg, endg):
        if bp in feat_dic:
            featg = feat_dic[bp]
            if featg not in feats_gain:
                feats_gain.append(featg)
    overall_gain.append(feats_gain)
    feats_gain = []

#gdic= {i: overall_gain.count(i) for i in overall_gain}

ex_g = 0
in_g = 0
prom_g = 0
for i in overall_gain:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "intron":
            in_g += 1
        elif sublist == "exon":
            ex_g += 1
        elif sublist == "promoter":
            prom_g += 1 
        else:
            continue
#
# print( ex_g)
# print( in_g)
# print( prom_g)
# # print(overall_gain)
#
#
countl=0
overall_loss = []
for i, line in enumerate(lost):
    countl += 1
    feats_loss= []
    fields = line.rstrip("\r\n").split("\t")
    startl = int(fields[1])
    endl = int(fields[2])
    for bp in range(startl, endl):
        if bp in feat_dic:
            featl = feat_dic[bp]
            if featl not in feats_loss:
                feats_loss.append(featl)
    overall_loss.append(feats_loss)
    feats_loss = []

ex_l = 0
in_l = 0
prom_l = 0
for i in overall_loss:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "intron":
            in_l += 1
        elif sublist == "exon":
            ex_l += 1
        elif sublist == "promoter":
            prom_l += 1 
        else:
            continue
# print( ex_l)
# print( in_l)
# print( prom_l)#
# counts = [countg,countl]
# ticks = [0, 0.25]
# tick_labels = ["gained","lost"]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))
ax1.bar("exons gained", ex_g)
ax1.bar("introns gained", in_g)
ax1.bar("promoters gained", prom_g)
ax1.bar("exons lost", ex_l)
ax1.bar("introns lost", in_l)
ax1.bar("promoters lost", prom_l)
ax1.set_ylabel("Number of binding sites")
ax1.set_title ("CTCF ginding sites in these regions")
#ax1.legend()

ax2.bar("count gained", countg, width=0.1,color="r",align="center")
ax2.bar("count lost", countl, width=0.1,color="b",align="center")
ax2.set_xticks([])
#ax2.set_xticklabels(countg, countl ("gain","loss"))
ax2.set_ylabel("Number of binding sites")
ax2.set_title("CTCF binding sites, gained and lost")
#ax2.legend()
#plt.show()
fig.savefig("chip.png")
plt.close(fig)





