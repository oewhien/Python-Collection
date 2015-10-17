# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import h5py 



class FHN_res(object):
    def __init__(self, fName):
        f = h5py.File(fName)
        # inspect structure with vitables or something   
        y = np.array(f['/1/y'][()])
        t = np.array(f['/1/t'][()])
        r = np.array(f['/1/rOut'][()])
        v = np.array(f['/1/vOut'][()])        
        self.v = v.T;
        self.r = r.T;
        self.t = t;
        self.x = y;





