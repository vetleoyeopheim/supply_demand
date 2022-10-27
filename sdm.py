# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:30:29 2021

@author: Vetle
"""


import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import math


def dx_dt(x,t):
    
    R,p = x
    
    K = 10
    r = 0.1
    h = 1
    a0 = 5
    a1 = 1
    a2 = 0.2
    a3 = 0.1
    
    f_i = -r * R + K
    f_o = h * (a0 + a1 * math.sin(a2 + t) - a3 * p) 
    
    dR_dt = f_i - f_o
    dp_dt = (1 - 0.05 * R) * p
    
    return dR_dt, dp_dt

t = np.linspace(0,50,500)
x0 = (5,1)

solution = odeint(dx_dt, x0, t)
#plt.plot(solution[:,0],solution[:,1])
plt.plot(solution)
