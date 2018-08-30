#!/usr/bin/env python3

""""
This script is designed to assemble all fpkms for each transcript sample in each fly in samples

SO whoever wants to use this shoud have it like so:

./bigmerge.py samples.csv ctab_dir

"""



import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(sys.argv[1])

fpkms = {}
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join( sys.argv[2], sample, "t_data.ctab")
    #make the filename "stringtie/SRRXXXX/t_data.ctab"
    ctab_df = pd.read_table( filename, index_col="t_name")
    #we are now organizing ctab-df as a dataframe containing filename, organized by T-name. 
    fpkm = ctab_df.loc[:,"FPKM"]
    #we orfanized FPKM's by transcript name, stored into variable fpkm
    name = "{0}_{1}".format(sex, stage)
    fpkms[name]= fpkm
    #now we have a dictionary containing {Sex_stage:DF} where DF is a dataframe containing all of the FPKM's organized by transcript

fpkms_df = pd.DataFrame(fpkms)
#we converted our dictionary to a dataframe; now this is all the FPKM's organized by transcript, which is organized by samplename.
fpkms_df.to_csv(sys.stdout)
#SEND IT AWAY