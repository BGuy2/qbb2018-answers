#!/usr/bin/env python3

"""
Usage: timecourse gene samples.csv ctab_dir

create a timecourse of a given transcript for females

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def timecourse( csv, gender, gene ):
    df = pd.read_csv( csv )
    soi = df.loc[:,"sex"] == gender 
    frames = df.loc[soi,:]

    fpkms_avg = []
    
    for index, sample, sex, stage in frames.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table( filename, index_col="t_name")
        roi = ctab_df.loc[:,"gene_name"] == gene
        fpkms= ctab_df.loc[roi,"FPKM"]
        fpkms_avg.append(np.mean(fpkms) )

    return fpkms_avg
  #instead of storing these fpkms like in the last script, we are redturning them into females_ or males_fpkms  
    
var = timecourse(sys.argv[2], "female", sys.argv[1])
print( var ) 

#
# females_fpkms = timecourse( sys.argv[2], "female")
# males_fpkms = timecourse( sys.argv[2], "male")
#
# females_fpkmsREP =timecourse( sys.argv[3], "female")
# males_fpkmsREP = timecourse( sys.argv[3], "male")
##
#
# print(females_fpkms)
#
# print("THIS IS THE REP BELOW: ")
# print(females_fpkmsREP)
#
# print(" YO FEMALE FPKMS STOP HERE")
#
# print(males_fpkms)
#
# print("THIS IS THE REP BELOW: ")
# print(males_fpkmsREP)

#
# stages = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
#
# fig, ax = plt.subplots()
# ax.plot( stages, males_fpkms, color= "blue", label= "male" )
# ax.plot( stages, females_fpkms, color= "red", label= "female" )
# ax.plot( stages, males_fpkmsREP, color= "orange", label= "male Replicates")
# ax.plot( stages, females_fpkmsREP, color= "green", label= "female Replicates")
# ax.set_title=( sys.argv[1] )
# plt.tight_layout()
# ax.set_ylabel("FPKMs")
# ax.set_xlabel("stage")
# plt.tight_layout()
# box=ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.8, box.height] )
# ax.legend(loc='center left', bbox_to_anchor=(1,0.5), frameon = False)
# plt.xticks(stages, rotation= "vertical")
# fig.savefig( "timecourseMF.png")
# plt.close( fig )
