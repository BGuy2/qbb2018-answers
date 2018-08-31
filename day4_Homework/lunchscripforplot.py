#!/usr/bin/env python3
"""
script ctabfile1 ctabfile2
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" )


name1 = sys.argv[1].split( os.sep)[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name").loc[:,"FPKM"]


name2 = sys.argv[2].split( os.sep)[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col= "t_name").loc[:,"FPKM"]

m = (fpkm1/fpkm2)
log_m = np.log( m + 1)
a = (1/2) * (fpkm1 + fpkm2)
log_a = np.log( a +1)


#
# coeff_p = np.polyfit( log_fpkm1, log_fpkm2, 1)
# lineobf= np.poly1d(coeff_p)

# xplot= np.linspace(0, 10, 100)
# y# plot= lineobf(xplot)
#
#
# print(coeff_p)
# print(lineobf)

fig, ax = plt.subplots()
fig.suptitle( "MA plot" )
ax.set_xlabel("log(fpkm) " + str(name1))
ax.scatter(log_a,log_m, alpha= 0.2)
#I'm thinking theres something wrong with line 34, for some reason my graph is orange
ax.set_ylabel("log(fpkm) " + str(name2))
# ax.plot(xplot, yplot)
# ax.scatter( log_fpkm1, log_fpkm2)
fig.savefig("day4MA.png")
plt.close(fig)