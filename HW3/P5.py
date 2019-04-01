#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:54:36 2019

@author: ghosh128
"""

import matplotlib.pyplot as plt
import numpy as np

sigma_osq = 1
list_sigma_xsq = list(range(0,100))
sigma_zsq = 0.75
list_sigma_tsq = []
#%%
for sigma_xsq in list_sigma_xsq:
    sigma_tsq = 1
    for i in range(1,11):
        sigma_t1sq = ((sigma_tsq + sigma_xsq)/(sigma_tsq + sigma_xsq + sigma_zsq))*sigma_zsq
        sigma_tsq = sigma_t1sq
    list_sigma_tsq.append(sigma_tsq)
#%%
fig = plt.figure()
fig.set_size_inches(20, 10)
ax = plt.gca()
ax.set_xticks(np.arange(0, 100, 1))
ax.set_xticklabels(np.arange(0, 100, 1), rotation='vertical')
plt.ylabel('sigma_10')
plt.xlabel('sigma_x')
plt.plot(list_sigma_xsq, list_sigma_tsq)
plt.title("Variance after 10 throws vs Accuracy")
