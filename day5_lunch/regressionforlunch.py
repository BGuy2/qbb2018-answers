#!/usr/bin/env python3 
"""
 
 script h1 h2 h3 h4 h5 all.csv bed

"""



import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import statsmodels.formula.api as sm

df_SRRfiles = pd.read_csv( sys.argv[6], sep="\t")
xpsn= df_SRRfiles.loc[:,"FPKM"]



df1= pd.read_csv(sys.argv[1], sep="\t")
df1_1=df1.iloc[:,-1] 
df2= pd.read_csv(sys.argv[2], sep="\t")
df2_1=df2.iloc[:,-1] 
df3= pd.read_csv(sys.argv[3], sep="\t")
df3_1= df3.iloc[:,-1] 
df4= pd.read_csv(sys.argv[4], sep="\t")
df4_1=df4.iloc[:,-1] 
df5= pd.read_csv(sys.argv[5], sep="\t")
df5_1= df5.iloc[:,-1]

mod= pd.concat([df1_1, df2_1, df3_1, df4_1, df5_1, xpsn], axis= 1 )   

mod.columns= ["FPKMS", "H3K4me3", "H3K4me1", "H3K27me3", "H3K27ac","H3K9ac"]
print(mod)
#
regression= sm.ols( formula= 'FPKMS ~ H3K4me3 + H3K4me1 + H3K27me3 + H3K27ac + H3K9ac', data= mod)
#
results= regression.fit()
print( results.summary())


fig, ax = plt.subplots()
ax.set_title("residual from ChIP and FPKMs")
fig.suptitle( "residual from Chip and FPKMs" )
plt.hist(results.resid_pearson())
fig.savefig("day4MA.png")
plt.close(fig)










#
# #comput pearson correlation
# pearson_corr = df.corr( method="spearman")
# #doesnt make assumptions about normality of values, instead sorts FPKMS for analysis. this allows for a better regression
# mid heat in plot has a second diagonal, telling us a similarity between gene expresson in M/F (until dosage compensation at around stage 13)
# print( pearson_corr)
#
# fig, ax = plt.subplots()
# ax.set_title("Pairwise Spearman Corr. of FPKMs")
# im = ax.pcolor( pearson_corr )
# fig.colorbar( im, ax=ax)
# ax.set_xlabel( "Samples")
# ax.set_ylabel( "Samples")
# fig.savefig( "pearson_corr.png")
# plt.close()
#
#
# print( pearson_corr )