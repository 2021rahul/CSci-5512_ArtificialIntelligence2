#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:54:36 2019

@author: ghosh128
"""

import matplotlib.pyplot as plt

sigma_osq = 1
list_sigma_xsq = list(range(-100,100))
sigma_zsq = 0.75
list_sigma_tsq = []
#%%
for sigma_xsq in list_sigma_xsq:
    sigma_tsq = 1
    for i in range(1,11):
        sigma_tsq = ((sigma_tsq + sigma_xsq)*sigma_zsq)/(sigma_tsq + sigma_xsq + sigma_zsq)
    list_sigma_tsq.append(sigma_tsq)
#%%
plt.plot(list_sigma_xsq, list_sigma_tsq)