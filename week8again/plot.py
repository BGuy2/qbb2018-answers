#!/usr/bin/env python3
"""
./plot.py ER4_peaks_Narrowpeaks.bed
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab

stuff= open(sys.argv[1])

percentage = []

for line in stuff:
    fields = line.rstrip("\r\n").split("\t")
    Sm = fields[3]
    Em = fields[4]
    Sp = fields[10]
    Ep = fields[11]
    percentage.append(100*(abs(float(Sm)-float(Sp))/abs(float(Ep)-float(Sp))))
    # print(percentage)

""" line of best fit"""





fig, ax = plt.subplots()

plt.hist(percentage, bins=200)




ax.set_xlabel("Position")
ax.set_ylabel("Frequency")
fig.suptitle("Motif Position with respect to Peak Sequence")
fig.savefig("Week8.png")
plt.tight_layout()
plt.close(fig)