# -*- coding: utf-8 -*-
"""
This calculates the power spectra of kymographs from FHN simulations to find out 
potential resonances
"""
import numpy as np
import matplotlib.pyplot as plt
import h5py 
import Struc_Noise_Dect as SND
from read_data import FHN_res
import os

def getSpec(v,t):    
    y_f_Ar = np.ones(v.shape)

    for kk in range(0,v.shape[0]):
        v_c = v[kk,:];
        y_f = np.fft.fft(v_c);
        y_f_Ar[kk,:] = y_f;

    y_f_M = y_f_Ar.mean(axis=0)
    return y_f_M



baseDir = "/home/erik/Desktop/xmds-Simulationen/Simulationen-Archiv/2015-06-01_WienerNoiseScripted/archive/mat"

fileList = os.listdir(baseDir)
noiseVals = np.empty([])
specDat = np.empty(500)

for file in fileList:
    if file.endswith(".mat"):
        print("Working on "+file)
        resDat = FHN_res(os.path.join(baseDir,file))

        v = resDat.v.T;
        v = (v>0)*1.0
        t = resDat.t.T;

        y_f_M = getSpec(v,t)        
        pow_pl = y_f_M[0:y_f_M.size/2]*y_f_M[0:y_f_M.size/2].conjugate()
        
        noiseVals = np.append(noiseVals,resDat.nsGain)
        specDat = np.vstack((specDat,pow_pl))


specDat = np.delete(specDat,0,1)

uniNoise =np.unique(noiseVals)

specMean = np.empty([uniNoise.size,specDat.shape[1]])

for kk in range(0,uniNoise.size-1):
     ind = np.where(noiseVals==uniNoise[kk])
     specMean[kk,:] = specDat[ind].mean(axis=0)

freq = np.linspace(0,t.size/t.max(),t.size)    
freq_pl = freq[0:freq.size/2]

freq_pl_grd, uniNoise_grd = np.meshgrid(freq_pl,uniNoise)


plt.figure()
h = plt.pcolormesh(freq_pl_grd,uniNoise_grd,specMean)
h.set_clim(vmin=0,vmax=40)
plt.xlabel("frequency")
plt.ylabel("noise amplitude")
plt.title("power spectrum")


plt.figure()
h = plt.pcolormesh(1.0/freq_pl_grd[:,1:],uniNoise_grd[:,1:],specMean[:,1:])
h.set_clim(vmin=0,vmax=40)
plt.xlabel("period")
plt.ylabel("noise amplitude")
plt.title("power spectrum")


