#!/usr/bin/env python3
"""
(heat.py) (originaltext file of DE genes)
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage 
from scipy import stats
import seaborn as sns
import pandas as pd

filejamesgaveus = pd.read_csv(sys.argv[1], sep="\t", index_col= "gene")
df = pd.DataFrame(data=filejamesgaveus)

cmap = sns.diverging_palette(145,280, s=85, l=25, n=7, as_cmap=True)
ax = sns.clustermap(df, cmap = cmap)

ax.savefig("heat")
plt.close()

from sklearn.cluster import KMeans


kmeans= KMeans(n_clusters= 4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

#(df)

plt.figure()
plt.title("k-means")
plt.scatter(df["CFU"], df['poly'], c=y_kmeans, s=5, cmap='viridis')
# plt.scatter(df["CFU"], df['poly'], c = kmeans[1])
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("test_kmeans.png")
plt.close()



df2 = df.filter(['CFU','mys','poly', 'unk'], axis=1)

df2['avg_latte'] = df[['poly', 'unk']].mean(axis=1)

df2['avg_early'] = df2[['CFU', 'mys']].mean(axis=1)

"""
YO BOY ABOVE IS HOW YAS ADDS A COLUMN
"""

df2["fold_change"] = df2["avg_latte"] / df2["avg_early"]

df2.loc[df2['fold_change'] < .5, 'Downregulated'] = df2['fold_change']
df2.loc[df2['fold_change'] > 2, 'Upregulated'] = df2['fold_change']

p_value = []
for index, row in df2.iterrows():
   CFU = row['CFU']
   mys = row['mys']
   early = [CFU, mys]
   poly = row['poly']
   unk = row['unk']
   late = [poly, unk]
   t_test, p_val = stats.ttest_ind( early, late)
   if p_val < .05:
       p_value.append(p_val)
   else:
       p_value.append(int(-1))
df2['p_value'] = p_value
 
 
 
 
 
Down_sig = []
for index, row in df2.iterrows():
    Downregulated = row['Downregulated']
    p_value = row['p_value']
    if Downregulated and p_value > 0:
            Down_sig.append(Downregulated)
    else:
        Down_sig.append(int(-1))
df2['Down_sig'] = Down_sig

Up_sig = []
for index, row in df2.iterrows():
    Upregulated = row['Upregulated']
    p_value = row['p_value']
    if Upregulated and p_value > 0:
            Up_sig.append(Upregulated)
    else:
        Up_sig.append(int(-1))
df2['Up_sig'] = Up_sig



df3 = df2.filter(['Down_sig','Up_sig','p_value'], axis=1)


df3_sorted = (df3.sort_values(['Down_sig', 'Up_sig'], ascending=True))
df3_sorted1 = (df3.sort_values(['Up_sig'], ascending=False))

""" for significant 2 fold upregulated genes, I made a text file"""

file = open('Up_sig_list.txt','w') 
for index, row in df3_sorted1.iterrows():
    Up_sig = row['Up_sig']
    p_value = row['p_value']
    if Up_sig > int(0):
        print(index, "\t", Up_sig, "\t", p_value)
        file.write(index)
        file.write("\t")
        file.write(str(Up_sig))
        file.write("\t")
        file.write(str(p_value))
        file.write("\n")
    else:
        continue
file.close()
""" for significant 2 fold downregulated genes, I made a text file """

file = open('Down_sig_list.txt','w') 
for index, row in df3_sorted.iterrows():
    Down_sig = row['Down_sig']
    p_value = row['p_value']
    if Down_sig > int(0):
        print(index, "\t", Down_sig, "\t", p_value)
        file.write(index)
        file.write("\t")
        file.write(str(Down_sig))
        file.write("\t")
        file.write(str(p_value))
        file.write("\n")
    else:
        continue
        
print(len(y_kmeans))

""" 2310046K01Rik is 9th gene, so cluster 2 """
print(kmeans.fit(df))
ribo_cluster = y_kmeans[2]
similar_genes = df.index[y_kmeans == ribo_cluster]
print(similar_genes)
print(similar_genes.tolist())

file = open('similargenes_incluster.txt','w')
for line in similar_genes.tolist():
    print(line)
    file.write(line)
    file.write('\n')
file.close()
file.close()










