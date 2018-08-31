#!/usr/bin/env python3 


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv( sys.argv[1], sep="\t")



StartPos= df.loc[:, "start"].tolist()

Before=[]
After= []

for i in range(len(StartPos)):
     Before.append(StartPos[i])
     Before[i]= Before[i] - 500
     After.append(StartPos[i])
     After[i]= After[i] + 500
     if Before[i] < 0:
         Before[i] = 1
     
     
se1= pd.Series(Before)
df["Before"] = se1.values

se2 = pd.Series(After)
df["After"] = se2.values

df1=  df[["chr", "Before", "After", "t_name"] ] 


#df1= df.loc[ :, "chr"]#
# df2= df.loc[ :, "Before"]
# df3= df.loc[ :, "After"]
# #df4= df.loc[ :, "t_name"]

ThisPrints= pd.DataFrame.to_csv(df1, sep="\t", header=False, index= False)
print(ThisPrints)
