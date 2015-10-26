# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:44:14 2015

@author: erikB
"""
import numpy as np

def readLogFile(filePath):
    A=[]
    B=[]
    logH = open(filePath,'r');
    logCont = logH.read().splitlines();
    logCont[0:2] = []
    for kk in range(0,len(logCont)):
        cntx, cnty, rM, rMin, rMax, frame = logCont[kk].strip().split("\t")
        A.append(cntx)
        B.append(cnty)
    
    logH.close()    
    centX = np.double(np.asarray(A))
    centY = np.double(np.asarray(B))
    return centX, centY    
        
        
    
#centX,centY = readLogFile(path)
    
    
