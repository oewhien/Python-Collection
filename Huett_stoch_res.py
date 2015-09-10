# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import h5py
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

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

def readH5():
    f = h5py.File('fhn_1d_perBnd_noisy.h5')
    # inspect structure with vitables or something   
    #y = np.array(f['/1/y'][()])
    #t = np.array(f['/1/t'][()])
    #r = np.array(f['/1/rOut'][()])
    v = np.array(f['/1/vOut'][()])
    v = v.T
    return v



v = readH5()

#v = np.asanyarray(Image.open('testBild_Streifen_Noise.tif'),float)


# test
f1 = plt.figure()
ax = f1.add_axes([0, 0, 1, 1])
plt.imshow(v)
f1.show()

delta = getDelta(v)
Omega = getOmega(delta)

f2 = plt.figure()
plt.plot(Omega)
f2.show()
