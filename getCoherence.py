# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:14:05 2015

@author: erikB
"""
import numpy as np

def getT(slc):
    slc_neg = 1-slc
    rests = np.hstack(([0],np.cumsum(1.0*(np.diff(slc_neg)>0))))*slc_neg
    N_rests = np.int(rests.max())
    T_rest = np.empty(N_rests)

    for kk in range(0,N_rests):
        T_rest[kk] = np.sum(rests == (kk+1))
    
    return T_rest
    
    
def getR(v):
    v =(v>0)*1.0  #Binarizing the data  
    T_all = np.empty([])

    for kk in range(0,v.shape[0]-1):    
        T_all = np.hstack((T_all,getT(v[kk,:])))
    
    R = T_all.std()/T_all.mean()
    return R