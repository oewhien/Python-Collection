# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:23:47 2015

@author: erikB
"""
import numpy as np
import matplotlib.pyplot as plt
import h5py 
import Struc_Noise_Dect as SND
from read_data import FHN_res

resDat = FHN_res('fhn_1d_perBnd_noisy_scriptable_nsGain_0.15_seed1_247seed2_321seed3_423.mat')
v = resDat.v;
v = (v>0)*1.0
t = resDat.t.T;

dt = t[1]-t[0];

v_c = v[0,:];

y_f = np.fft.fft(v_c);

per = np.linspace(0,t.size/t.max(),t.size)

plt.figure()
plt.plot(t,v_c)



per_pl = per[0:per.size/2]
pow_pl = y_f[0:y_f.size/2]*y_f[0:y_f.size/2].conjugate()

plt.figure()
plt.plot(per_pl,pow_pl)
plt.xlabel("frequency")

plt.figure()
plt.plot(1.0/per_pl[1:],pow_pl[1:])
plt.xlabel("period")

