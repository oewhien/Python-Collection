# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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


def analyseSim(cRes):
    v = cRes.v 
    v = (v>0)*1.0
    delta = SND.getDelta(v)
    Omega = SND.getOmega(delta)
    redHom = SND.getHomo(v)

    OmegaM = Omega.mean()
    redHomM = redHom.mean()
    cRes.OmegaM = OmegaM
    cRes.redHomM = redHomM
    return cRes



#v = readH5()
#v = np.asanyarray(Image.open('testBild_Streifen_Noise.tif'),float)


baseDir = "/home/erik/Desktop/xmds-Simulationen/Simulationen-Archiv/2015-06-01_WienerNoiseScripted/archive/mat"

fileList = os.listdir(baseDir)
noiseVals = np.array([])
OmMVals = np.array([])
rHomVals = np.array([])

for file in fileList:
    if file.endswith(".mat"):
        print("Working on "+file)
        #resDat = FHN_res('fhn_1d_perBnd_noisy.h5')
        #v = resDat.v;
        res = FHN_res(os.path.join(baseDir,file))
        res = analyseSim(res)
        noiseVals = np.append(noiseVals,res.nsGain)
        OmMVals = np.append(OmMVals,res.OmegaM)
        rHomVals = np.append(rHomVals,res.redHomM)                
        

plt.plot(OmMVals,rHomVals,'o')
plt.ylabel("H")
plt.xlabel("Omega")


pkl_file = open('FHN_res_data.pkl', 'wb')
pickle.dump([noiseVals,OmMVals,baseDir,fileList,rHomVals], pkl_file)
pkl_file.close()

