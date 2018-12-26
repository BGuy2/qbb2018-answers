#!/usr/bin/env python3

"""
./bettermanhattan.py plink.*.qassoc
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



for f in sys.argv[1:]:
    
    treatment = f.split(".")[1]
    df = pd.read_table(f, delim_whitespace=True)
    bp = df.loc[:,"BP"].tolist()
    positions = []
    count = 0

    for i, pos in enumerate(bp):
        if i == 0:
            positions.append(0)
        elif bp[i] < bp[i-1]:
            positions.append(count + 1)
            count += 1
        else:
            difference = bp[i] - bp[i-1]
            positions.append(count + difference)
            count += difference
   
    pvalue = -np.log10(df.loc[:,"P"])
    df = df.assign(pvalue=pvalue, position=positions)
    df.loc[df['pvalue'] > 5, 'sigs'] = df['pvalue']
    groups = df.groupby('CHR', sort=False)


    fig, ax = plt.subplots(figsize=(20,10))
    
    x_labels = []
    x_labels_pos = []
    
    for i, (name, group) in enumerate(groups):
        ax.scatter(group.position, group.pvalue, s=1)
        ax.scatter(group.position, group.sigs, s=1)
        x_labels.append(name)
        x_labels_pos.append(np.median(group.position))
    
    ax.set_xticklabels(x_labels, rotation=50, fontsize=8)
    ax.set_xticks(x_labels_pos)
    ax.set_xlabel("Chr")
    ax.set_ylabel("-log(p-value)")
    ax.set_title(treatment)
    fig.savefig(treatment + " Manhattan.png")
    plt.close()