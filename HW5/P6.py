#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:08:31 2019

@author: ghosh128
"""

import math

alpha = 0.01
a = 0
b = 0
c = 0
d = 0
d_viz = []
d_viz.append(d)
for i in range(1,100000):
    anew = a + alpha*((4*a*pow(c,4)) - b)
    bnew = b + alpha*((4*b*pow(d,2)) - a)
    cnew = c + alpha*((8*pow(a,2)*pow(c,3)) - (9*pow(c,2)*d))
    dnew = d + alpha*((math.exp(math.sin(d)+d)*(math.cos(d)+1)) + (4*d*pow(b,2)) - (3*pow(c,3)))

    a = anew
    b = bnew
    c = cnew
    d = dnew
    
    d_viz.append(d)
#%%
import matplotlib.pyplot as plt
plt.plot(d_viz)
    