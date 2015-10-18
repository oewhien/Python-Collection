# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:21:58 2015

@author: erik
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

pkl_file = open('cell_res_data.pkl', 'rb')
cell_OmMVals,cell_baseDir,cell_fileList,cell_rHomVals = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('FHN_res_data.pkl', 'rb')
FHN_noiseVals,FHN_OmMVals,FHN_baseDir,FHN_fileList,FHN_rHomVals = pickle.load(pkl_file)
pkl_file.close()

plt.plot(FHN_OmMVals,FHN_rHomVals,'o')
plt.plot(cell_OmMVals,cell_rHomVals,'ro')
plt.show()
