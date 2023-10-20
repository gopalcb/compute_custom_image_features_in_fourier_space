# Libraries import
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
import os
from os import listdir
from os.path import isfile, join

%matplotlib inline
# Get current/root directory
root = os.getcwd()

data = []
sig_arr = []
pid = 1
N = 256
# compute--
# magnitude   phase   signature   distance   sector


# Compute spectral rotation angle given r,c
def spectral_rotation_angle(r, c):
    x = r - (N / 2)
    y = (N / 2) - c
    q = 0 if x == 0 or y == 0 else (y / x)
    phase = math.atan(q)
    return phase


# Compute distance given r,c
def compute_distance(r, c):
    x = r - (N / 2)
    y = (N / 2) - c
    d = math.sqrt(x*x+y*y)
    return d


# Compute sector index
def compute_sector(phase):
    phase_d = abs(np.degrees(phase))
    #print(phase_d)
    v = (phase_d/22.5)//1 #get only integer
    if v == 16:
        return 0
    return v


# Computing spectral deviation angle
def compute_theta(p1, p2, p3):
    # p1(x1,y1)
    # p2(x2,y2)
    # p3(x3,y3)
    HX1 = []
    HX2 = []
    
    HX1.append(p1[0]-5) # x1 0
    HX1.append(p1[1]) # y1 1
    HX1.append(p1[0]+5) # x2 2
    HX1.append(p1[1]) # y2 3
    
    HX2.append(p2[0]-5)
    HX2.append(p2[1])
    HX2.append(p2[0]+5)
    HX2.append(p2[1])
    
    M1 = (HX1[3]-HX1[1])/(HX1[2]-HX1[0]) # Slope of HX1
    M2 = (p2[1]-p1[1])/(p2[0]-p1[0]) # Slope of p1p2
    M3 = (HX2[3]-HX2[1])/(HX2[2]-HX2[0]) # Slope of HX2
    M4 = (p3[1]-p2[1])/(p3[0]-p2[0]) # Slope of p2p3
    
    TAN1 = abs((M2-M1)/(1+M1*M2))
    THETA1 = math.atan(TAN1)
    
    TAN2 = abs((M4-M3)/(1+M3*M4))
    THETA2 = math.atan(TAN2)
    
    # For negative slope, THETA1 is negative
    if M2 < 0:
        THETA1 = -THETA1
        
    if p3[1] < p2[1]:
        THETA2 = -THETA2
    
    THETA3 = THETA2-THETA1
    
    #OBJ.append(THETA3)
    
    return THETA3