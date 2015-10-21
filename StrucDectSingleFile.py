# -*- coding: utf-8 -*-
"""


"""


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from read_data import FHN_res
import h5py 
import Struc_Noise_Dect as SND



#resDat = FHN_res('fhn_1d_perBnd_noisy_scriptable_nsGain_0.15_seed1_247seed2_321seed3_423.mat')
#v = resDat.v;
v = np.asanyarray(Image.open('testBild_Streifen_Noise.tif'),float)
v = (v>1)*1.0

# test
f1 = plt.figure()
ax = f1.add_axes([0, 0, 1, 1])
plt.imshow(v)
plt.title('Spatiotemporal') 
plt.xlabel('t')
plt.ylabel('s')
f1.show()


delta = SND.getDelta(v)
Omega = SND.getOmega(delta)
redHom = SND.getHomo(v)


f2 = plt.figure()
plt.plot(Omega)
plt.title('Omega') 
plt.xlabel('t')
plt.ylabel('Omega')
f2.show()

f3 = plt.figure()
plt.title('Reduced homogeneity') 
plt.xlabel('t')
plt.ylabel('h')
plt.plot(redHom)
f3.show()