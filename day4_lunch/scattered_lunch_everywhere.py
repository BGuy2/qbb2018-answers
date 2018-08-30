#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" )


name1 = sys.argv[1].split( os.sep)[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name").loc[:,"FPKM"]
log_fpkm1 = np.log(fpkm1 + 1)

name2 = sys.argv[2].split( os.sep)[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col= "t_name").loc[:,"FPKM"]
log_fpkm2 = np.log(fpkm2 + 1)

coeff_p = np.polyfit( log_fpkm1, log_fpkm2, 1)
lineobf= np.poly1d(coeff_p)

xplot= np.linspace(0, 10, 100)
yplot= lineobf(xplot)


print(coeff_p)
print(lineobf)

fig, ax = plt.subplots()
fig.suptitle( "Descriptive Title Here (yes I know this actually isn't that descriptive)" )
ax.set_xlabel("log(fpkm) " + str(name1))
ax.scatter(log_fpkm1, log_fpkm2, alpha= 0.2)
#I'm thinking theres something wrong with line 34, for some reason my graph is orange
ax.set_ylabel("log(fpkm) " + str(name2))
ax.plot(xplot, yplot)
# ax.scatter( log_fpkm1, log_fpkm2)
fig.savefig("day4lunch.png")
plt.close(fig)