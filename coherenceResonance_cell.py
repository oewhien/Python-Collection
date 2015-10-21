# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:08:08 2015

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
from PIL import Image


def getT(slc):
    slc_neg = 1-slc
    rests = np.hstack(([0],np.cumsum(1.0*(np.diff(slc_neg)>0))))*slc_neg
    N_rests = np.int(rests.max())
    T_rest = np.empty(N_rests)

    for kk in range(0,N_rests):
        T_rest[kk] = np.sum(rests == (kk+1))
    
    #plt.figure()
    #plt.plot(slc)
    #plt.plot(rests,'r')
    return T_rest



class cellRes:
    """The result of a FHN simulation"""
    def __init__(self, imI, fileName):
        self.imI = imI        
        self.fileName = fileName

def readMat(filePath):
    matFile = sio.loadmat(filePath)
    imI = np.asanyarray(matFile['imI'])
    fileName = matFile['FileName']
    cellRes_dat = cellRes(imI,fileName)
    return cellRes_dat
    
def analyseSim(cRes):
    v = cRes.imI
    v =(v>0)*1.0  #Binarizing the data  
    T_all = np.empty([])

    for kk in range(0,v.shape[0]-1):    
        T_all = np.hstack((T_all,getT(v[kk,:])))
    
    R =  T_all.std()/T_all.mean()
    cRes.R = R
    return cRes





baseDir = "/media/erik/TOSHIBA_EXT/Latrunculin-Experiments_Results/_okay"
fileList = os.listdir(baseDir)
noiseVals = np.array([])
rVals = np.array([])

for file in fileList:
    if file.endswith(".mat"):
        print("Working on "+file)
        #resDat = FHN_res('fhn_1d_perBnd_noisy.h5')
        #v = resDat.v;
        res = readMat(os.path.join(baseDir,file))
        res = analyseSim(res)

        rVals = np.append(rVals,res.R)      
        

plt.figure() 
plt.plot(rVals,'o')
plt.xlabel("")
plt.ylabel("std(T)/mean(T)")
