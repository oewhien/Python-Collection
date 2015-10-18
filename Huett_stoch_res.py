# -*- coding: utf-8 -*-
"""
Structure and noise detection based on the article 
"Method for detecting the signature of noise-induced strcutures in spatiotemporal data sets"
by M.Th. Hütt, R. Neff, H. Busch & F. Kaiser
Phys. Rev. E 66: 026117 (2002)

"""


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from read_FHN_res import FHN_res
import h5py 

class deltaClass:
    """Has the forward and backward difference"""
    def __init__(self, delta_t,delta_d):
        self.delta_t = delta_t
        self.delta_d = delta_d

def getDelta(A):
    A_t = np.append([A[-1,:]],A,axis=0)
    A_d = np.append(A,[A[0,:]],axis=0)
    delta = deltaClass(A - A_t[0:-1,:],A - A_d[1:,:])    
    return delta

def getOmega(dels):    
#    for k in range(1,dels.delta_d.shape[0])
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
    A_t = np.append([A[-1,:]],A[:-1,:],axis=0)
    A_d = np.append(A[1:,:],[A[0,:]],axis=0)
    AM = A.mean()
    A2M = np.mean(A*A)
    
    V = AM*AM - A2M
    
    Xi = 0.5*(A*A_t + A*A_d - 2*A2M).mean(axis=0)
    
    h = 2.0*Xi/(V*Sigm*Sigm)
    return h



resDat = FHN_res('/Users/erikB/Documents/Data_Diary/2015-05-24_FHN_WienerNoiseSeries/nsGain0_15/fhn_1d_perBnd_noisy.h5')
v = resDat.v;
#v = np.asanyarray(Image.open('stripToNoisy.tif'),float)


# test
f1 = plt.figure()
ax = f1.add_axes([0, 0, 1, 1])
plt.imshow(v)
plt.title('Spatiotemporal') 
plt.xlabel('t')
plt.ylabel('s')
f1.show()

Sigm = np.abs(v.max() - v.min())
delta = getDelta(v)
Omega = getOmega(delta)
redHom = getHomo(v)


f2 = plt.figure()
plt.plot(Omega)
plt.title('Omega') 
plt.xlabel('t')
plt.ylabel('Omega')
f2.show()

f3 = plt.figure()
plt.title('Reduced homogeneity') 
plt.xlabel('t')
plt.ylabel('H_s')
plt.plot(redHom)
f3.show()