# -*- coding: utf-8 -*-
"""
Structure and noise detection based on the article 
"Method for detecting the signature of noise-induced strcutures in spatiotemporal data sets"
by M.Th. Hütt, R. Neff, H. Busch & F. Kaiser
Phys. Rev. E 66: 026117 (2002)

Implemented for 1-d data
"""

import numpy as np

class deltaClass:
    """Has the forward and backward difference"""
    def __init__(self, delta_t,delta_d):
        self.delta_t = delta_t
        self.delta_d = delta_d

    
def getDelta(A):
    """The forward and backward differences for detection of undirected changes"""
    A_t = np.append([A[-1,:]],A,axis=0)
    A_d = np.append(A,[A[0,:]],axis=0)
    delta = deltaClass(A - A_t[0:-1,:],A - A_d[1:,:])    
    return delta

def getOmega(dels):    
    """Cellular automata fluctuation number Omega, (Eq. 17 in Huett et al) """
    N = dels.delta_d.shape[1]
    delta_t = dels.delta_t
    delta_d = dels.delta_d
    
    a_t = np.diff(delta_t)
    a_t = a_t[:,0:-1]
    
    a_d = np.diff(delta_t[:,::-1])
    a_d = a_d[:,::-1]
    a_d = a_d[:,1::]
    
    b_t = np.diff(delta_d)
    b_t = b_t[:,0:-1]
    
    b_d = np.diff(delta_d[:,::-1])
    b_d = b_d[:,::-1]
    b_d = b_d[:,1::]    
    
    c_t = 0.25*(np.abs(a_t)+np.abs(b_t))*np.sign(a_t)*np.sign(b_t)*(np.sign(a_t)*np.sign(b_t)-1)
    c_d = 0.25*(np.abs(a_d)+np.abs(b_d))*np.sign(a_d)*np.sign(b_d)*(np.sign(a_d)*np.sign(b_d)-1)
    Omega = 1.0/(2*N)*(c_t.mean(axis=0) + c_d.mean(axis=0))

    return Omega

def getHomo(A):
    """Reduced homogeneity (Eq. 14 in Huett et al) """
    Sigm = np.abs(A.max() - A.min())
    A_t = np.append([A[-1,:]],A[:-1,:],axis=0)
    A_d = np.append(A[1:,:],[A[0,:]],axis=0)
    AM = A.mean(axis=0)
    A2M = np.mean(A*A,axis=0)    
    
    V = AM*AM - A2M

    Xi = 0.5*(A*A_t + A*A_d - 2*A2M).mean(axis=0)
    
    h = 2.0*Xi/(V*Sigm*Sigm)
    h[np.isnan(h)] = 0; 
    return h