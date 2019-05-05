#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:08:31 2019

@author: ghosh128
"""

import math

def f(a, b, c, d):
    return 2*a*pow(c,4) - a*b + math.exp(math.sin(d)+d) + 2*pow(b,2)*pow(d,2) - 3*pow(c,3)*d
#%%

alpha = 0.001
a = 0
b = 0
c = 0
d = 0

a_viz = []
b_viz = []
c_viz = []
d_viz = []
f_viz = []
a_viz.append(a)
b_viz.append(b)
c_viz.append(c)
d_viz.append(d)
for i in range(1,100000):
    anew = a - alpha*((4*a*pow(c,4)) - b)
    bnew = b - alpha*((4*b*pow(d,2)) - a)
    cnew = c - alpha*((8*pow(a,2)*pow(c,3)) - (9*pow(c,2)*d))
    dnew = d - alpha*((math.exp(math.sin(d)+d)*(math.cos(d)+1)) + (4*d*pow(b,2)) - (3*pow(c,3)))

    a = anew
    b = bnew
    c = cnew
    d = dnew
    
    a_viz.append(a)
    b_viz.append(b)
    c_viz.append(c)
    d_viz.append(d)
    f_viz.append(f(a, b, c, d))
#%%
import matplotlib.pyplot as plt
plt.plot(a_viz)
plt.savefig("a.png")
plt.show()
plt.plot(b_viz)
plt.savefig("b.png")
plt.show()
plt.plot(c_viz)
plt.savefig("c.png")
plt.show()
plt.plot(d_viz)
plt.savefig("d.png")
plt.show()
plt.plot(f_viz)
plt.savefig("f.png")
plt.show()