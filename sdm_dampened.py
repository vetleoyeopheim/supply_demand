# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:31:19 2022

@author: Vetle
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

def dx_dt(x,t):
    S,p = x
    a0 = 10
    a1 = 1
    b0 = 2
    b1 = 1.5
    b2 = 0.5
    r = 0.1
    q_d = a0 - a1 * p
    q_s = b0 + b1 * p - b2 * S
    dS_dt = q_s - q_d
    dp_dt = -r * S
    
    return dS_dt, dp_dt

t = np.linspace(0,50,200)
x0 = (5,1)

solution = odeint(dx_dt, x0, t)
plt.plot(solution[:,0],solution[:,1])
