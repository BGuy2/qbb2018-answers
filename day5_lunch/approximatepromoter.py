#!/usr/bin/env python3 


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name")



StartPos= df.loc[:, "start"].tolist()

Before=[]
After= []

for i in range(len(StartPos)):
     Before.append(StartPos[i])
     Before[i]= Before[i] + 500
     After.append(StartPos[i])
     After[i]= After[i] - 500

se1= pd.Series(Before)
df["Before"] = se1.values

se2 = pd.Series(After)
df["After"] = se2.values

df1=  df[["chr", "Before", "After"] ] 


#df1= df.loc[ :, "chr"]#
# df2= df.loc[ :, "Before"]
# df3= df.loc[ :, "After"]
# #df4= df.loc[ :, "t_name"]

ThisPrints= pd.DataFrame.to_csv(df1, sep="\t")
print(ThisPrints)
