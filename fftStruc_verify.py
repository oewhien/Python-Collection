# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:23:47 2015

@author: erikB
"""
import numpy as np
import matplotlib.pyplot as plt

f = 2.3 

x = np.linspace(0,10,1001);
y = np.sin(f*2*np.pi*x)

y_f = np.fft.fft(y);

per = np.linspace(0,x.size/x.max(),x.size)
plt.figure()
plt.plot(x,y)


per_pl = per[0:per.size/2]
pow_pl = y_f[0:y_f.size/2]*y_f[0:y_f.size/2].conjugate()

plt.figure()
plt.plot(per_pl,pow_pl)
plt.xlabel("frequency")

plt.figure()
plt.plot(1.0/per_pl[1:],pow_pl[1:])
plt.xlabel("period")