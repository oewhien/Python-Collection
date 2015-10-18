# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:39:01 2015

@author: erikB
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# %pylab qt

im = np.asanyarray(Image.open('stripes35deg_ds70_scale-1.tif'),float);

f1 = plt.figure()
ax = f1.add_axes([0, 0, 1, 1])
plt.imshow(im)
f1.show()


im_f = np.fft.fft2(im)

f2 = plt.figure()
ax = f2.add_axes([0, 0, 1, 1])
plt.imshow(im_f.imag)
f2.show()