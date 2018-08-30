#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#
# name1 = sys.argv[1].split( os.sep)[-2]
# fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name").loc[:,"FPKM"]
#
# name2 = sys.argv[2].split( os.sep)[-2]
# fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col= "t_name").loc[:,"FPKM"]
#
# compound_fpkms = fpkm1 + fpkm2
#
# df = pd.DataFrame( compound_fpkms )
# df.columns = ['FPKM']

#past_threshold = compound_fpkms.loc[:,"FPKM"] > float( sys.argv[3] )
#print(compound_fpkms.columns)

# past_threshold = compound_fpkms[compound_fpkms["FPKM"] > float(sys.argv[3])]
# print(past_threshold)
#print(past_threshold)
#past_threshold.to_csv( sys.stdout, sep="\t")


name1 = sys.argv[1].split( os.sep)[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name")

name2 = sys.argv[2].split( os.sep)[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col= "t_name")
compound_fpkms = fpkm1 + fpkm2
past_threshold = compound_fpkms[compound_fpkms["FPKM"] > float(sys.argv[3])][['FPKM']]
print(past_threshold)