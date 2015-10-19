# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:02:13 2015

@author: erikB
"""
import numpy as np
import h5py 
from read_FHN_res import FHN_res
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

resDat = FHN_res('/Users/erikB/Documents/Data_Diary/2015-05-24_FHN_WienerNoiseSeries/nsGain0_15/fhn_1d_perBnd_noisy.h5')
v = resDat.v;
r = resDat.r;

rMin = r.min()
rMax = r.max()
vMin = v.min()
vMax = v.max()

rGrd,vGrd = np.meshgrid(np.linspace(rMin,rMax,100),np.linspace(vMin,vMax,120));

pArray = np.zeros(rGrd.shape) 

siz1,siz2=v.shape

for ii in range(0,siz1-1):  #space
    for jj in range(0,siz2-1):  #time
        v0 = v[ii,jj]
        r0 = r[ii,jj]
        dv = np.abs(v0-vGrd)
        ind1,dummy = np.where(dv == dv.min())
        dr = np.abs(r0-rGrd)
        dummy,ind2 = np.where(dr == dr.min())
        #plt.plot(ind1[0],ind2[0],'o')
        pArray[ind1[0],ind2[0]] += 1 
        
f1 = plt.figure()
ax = f1.add_axes([0, 0, 1, 1])
imgPlot = plt.imshow(np.log(pArray+0.1),origin='lower')
plt.colorbar()
#imgPlot.set_clim(pArray.min(),pArray.max())