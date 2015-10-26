# -*- coding: utf-8 -*-
"""
Get an intensity profile from an image.
"""

import numpy as np
import matplotlib.pyplot as plt


def lineProf(im,x0,y0,x1,y1,length):
    sizX,sizY = im.shape
    x, y = np.linspace(x0, x1, length), np.linspace(y0, y1, length)
    x = x.astype(np.int)
    y = y.astype(np.int) 
    N = x.size    
    prof = np.ones(N)*np.NAN   
    boolAll = (x<sizX) & (y<sizY) & (x>0) & (y>0)
    xGet = x[boolAll]
    yGet = y[boolAll]    
    # Extract the values along the line
    prof[0:xGet.size] = im[xGet, yGet]
    return prof,x,y


def getStarProf(im,centX,centY,rMin,rMax,nAngles):
    
    phiRng = np.linspace(0,2*np.pi,nAngles+1)
    phiRng = phiRng[0:-1]
    dirVecX = np.cos(phiRng)
    dirVecY = np.sin(phiRng)
    length = int(rMax-rMin)    
    profAll = np.empty((phiRng.size,length))
    xAll = profAll
    yAll = profAll

    for kk in range(0,phiRng.size):
        x0 = xCent + rMin * dirVecX[kk]
        x1 = xCent + rMax * dirVecX[kk]
        y0 = yCent + rMin * dirVecY[kk]
        y1 = yCent + rMax * dirVecY[kk]
        prof,xProf,yProf = lineProf(z,x0,y0,x1,y1,length)
        profAll[kk,:] = prof
        xAll[kk,:] = xProf
        yAll[kk,:] = yProf
    return profAll, xAll, yAll
    
    
#-- Generate some data...
f = 10.;
x, y = np.mgrid[-50:50:1, -50:50:1]
z = np.sqrt(x**2/(f**2) + y**2/(f**2)) + np.sin((1/f*x)**2 + (1/f*y)**2)

#-- Extract the line...
# Make a line with "num" points...
xCent, yCent = 60, 65 
rMin = 10
rMax = 20

profs,xs,ys = getStarProf(z,xCent,yCent,rMin,rMax,10)