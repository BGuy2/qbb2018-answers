#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

for fname in sys.argv[1:]:
    treatment = fname.split('.')[1]
    (treatment)

    fig, ax = plt.subplots(figsize=(20,5))
    ax.set_title(treatment)

    df= pd.read_csv(open(sys.argv[1]), delim_whitespace=True)
    df['P'] = -(np.log10(df['P']))

    sig = (df['P'] > 5)
    df['P'][sig].plot(style = 'r.', ax=ax)
    df['P'][~sig].plot(style = 'b.', ax=ax)
    pvals= df['P']
    xvals = list(range(len(pvals)))
    plt.savefig("Manhattan" + str(treatment))
    plt.close()