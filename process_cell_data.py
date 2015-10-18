# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:06:06 2015

@author: erik
"""

import h5py
import matplotlib.pyplot as plt
import numpy as np
#from PIL import Image
import scipy.io as sio
import os
import pickle
from read_data import FHN_res
import Struc_Noise_Dect as SND

class cellRes:
    """The result of a FHN simulation"""
    def __init__(self, imI, fileName):
        self.imI = imI        
        self.fileName = fileName


def analyseSim(cRes):
    
    v = cRes.imI
    v =(v>0)*1.0  #Binarizing the data
    #plt.imshow(v)
    delta = SND.getDelta(v)
    Omega = SND.getOmega(delta)
    redHom = SND.getHomo(v)

    OmegaM = Omega.mean()
    redHomM = redHom.mean()
    cRes.OmegaM = OmegaM
    cRes.redHomM = redHomM
    return cRes
        
def readMat(filePath):
    matFile = sio.loadmat(filePath)
    imI = np.asanyarray(matFile['imI'])
    fileName = matFile['FileName']
    cellRes_dat = cellRes(imI,fileName)
    return cellRes_dat

baseDir = "/media/erik/TOSHIBA_EXT/Latrunculin-Experiments_Results/_okay"

fileList = os.listdir(baseDir)
OmMVals = np.array([])
rHomVals = np.array([])

mat_contents = sio.loadmat('/media/erik/TOSHIBA_EXT/Latrunculin-Experiments_Results/_okay/Kymograph_3_rep_2014-12-18_WT_channel_latA_washout-0002_Position55Cell2BW_279-411data.mat')


for file in fileList:
    if file.endswith(".mat"):
        print("Working on "+file)
        res = readMat(os.path.join(baseDir,file))
        res = analyseSim(res)
        OmMVals = np.append(OmMVals,res.OmegaM)
        rHomVals = np.append(rHomVals,res.redHomM)                
        
plt.plot(OmMVals,rHomVals,'o')

pkl_file = open('cell_res_data.pkl', 'wb')
pickle.dump([OmMVals,baseDir,fileList,rHomVals], pkl_file)
pkl_file.close()