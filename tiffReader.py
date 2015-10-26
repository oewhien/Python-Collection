# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:05:10 2015

@author: erikB
"""
from PIL import Image
import numpy as np

def readTiffStack(stackPath):
    im = Image.open(stackPath)
    imW = im.size[0]
    imH = im.size[1]
    
    n = 1
    while True:
        try:
            im.seek(n)
            n = n+1
        except EOFError:
            break;    
    
    imAr = np.empty((imW,imH)+(n+1,),dtype="uint16")
    imAr[:,:,0] = np.array(im.getdata()).reshape(imH, imW).T
    n = 1
    print "Loading \n", stackPath
    while True:
        try:
            tmpAr = np.array(im.getdata()).reshape(imH, imW)
            imAr[:,:,n] = tmpAr.T
            im.seek(n)
            n = n+1
        except EOFError:
            print "...done"
            break;
    
    imAr = imAr[:,:,0:n]
    return imAr
    
#stackPath = '/Volumes/TOSHIBA_EXT/Latrunculin-Experiments/2014-12-18_WT_chamber_latA_washout/2014-12-18_WT_channel_latA_washout-0002/2014-12-18_WT_channel_latA_washout-0002_Position55Cell11/2014-12-18_WT_channel_latA_washout-0002_Position55Cell11.tif'
#imAr = readTiffStack(stackPath)