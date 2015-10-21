# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:08:08 2015

@author: erik
"""
import numpy as np
import matplotlib.pyplot as plt

slc = np.array([0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1])


def getT(slc):
    slc_neg = 1-slc
    rests = np.hstack(([0],np.cumsum(1.0*(np.diff(slc_neg)>0))))*slc_neg
    N_rests = np.int(rests.max())
    T_rest = np.empty(N_rests)

    for kk in range(0,N_rests):
        T_rest[kk] = np.sum(rests == (kk+1))
    
    plt.figure()
    plt.plot(slc)
    plt.plot(rests,'r')
    return T_rest

getT(slc)