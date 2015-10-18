# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import h5py 
import scipy.io as sio


class FHN_res(object):
    def __init__(self, fName):
        """Class representing the result of a FHN simulation"""     
        if fName.endswith("h5"):
            f = h5py.File(fName)
            # inspect structure with vitables or something   
            x = np.array(f['/1/y'][()])
            t = np.array(f['/1/t'][()])
            r = np.array(f['/1/rOut'][()])
            v = np.array(f['/1/vOut'][()])
            nsGain = np.NaN#np.array(f['/1/etaOut'][()])
        elif fName.endswith("mat"):
            matFile = sio.loadmat(fName)
            v = np.asanyarray(matFile['V'])
            r = np.asanyarray(matFile['R'])
            t = np.asanyarray(matFile['t'])
            x = np.asanyarray(matFile['x'])
            nsGain = matFile['nsGain']
        else:
            raise NameError('Not a valid file extension')
        self.v = v.T;
        self.r = r.T;
        self.t = t;
        self.x = x;
        self.nsGain = nsGain
        self.fName = fName





