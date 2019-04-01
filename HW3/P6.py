#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:03:50 2019

@author: ghosh128
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 3/8
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
#%%
list_sigma_tsq = [1/2,1/2]
sigma_xsq = 1
sigma_zsq = 0.5

for t in range(2,100):
    sigma_tsq = ((list_sigma_tsq[t-1] + sigma_xsq)/(list_sigma_tsq[t-1] + sigma_xsq + sigma_zsq))*sigma_zsq
    list_sigma_tsq.append(sigma_tsq)

plt.plot(list_sigma_tsq[1:])
plt.show()