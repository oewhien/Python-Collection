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


def analyseSim(cRes):
    v = cRes.v.T 
    v = (v>0)*1.0    
    T_all = np.empty([])

    for kk in range(0,v.shape[0]-1):    
        T_all = np.hstack((T_all,getT(v[kk,:])))
    
    R =  T_all.std()/T_all.mean()
    cRes.R = R
    return cRes





baseDir = "/home/erik/Desktop/xmds-Simulationen/Simulationen-Archiv/2015-06-01_WienerNoiseScripted/archive/mat"
fileList = os.listdir(baseDir)
noiseVals = np.array([])
rVals = np.array([])

for file in fileList:
    if file.endswith(".mat"):
        print("Working on "+file)
        #resDat = FHN_res('fhn_1d_perBnd_noisy.h5')
        #v = resDat.v;
        res = FHN_res(os.path.join(baseDir,file))
        res = analyseSim(res)
        noiseVals = np.append(noiseVals,res.nsGain)
        rVals = np.append(rVals,res.R)      
        

plt.figure() 
plt.plot(noiseVals,rVals,'o')
plt.xlabel("noise amplitude")
plt.ylabel("std(T)/mean(T)")
