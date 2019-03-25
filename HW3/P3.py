#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:45:50 2019

@author: 2021rahul
"""

import numpy as np

P_0 = np.array([1/3, 1/3, 1/3])
P_xt1_xt = np.reshape(np.array([[0.6, 0.35, 0.05], [0.2, 0.6, 0.2], [0, 0.5, 0.5]]), (3, 3))
P_et_xt = np.transpose(np.array([[0, 0.05, 0.4], [1, 0.95, 0.6]]))

#%%
#Evidence till day 5
T=5
E = np.ones(T+1, dtype=int)
E[[1,4]] = 0
MLE = np.zeros((len(P_0), T+1), dtype=float)
MLE[:,0] = P_0

for t in range(1, T+1):
    MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
val = np.argmax(MLE, axis=0)
print(val)
#%%
#Evidence till day 5
T=6
E = np.ones(T+1, dtype=int)
E[[1,4,6]] = 0
MLE = np.zeros((len(P_0), T+1), dtype=float)
MLE[:,0] = P_0

for t in range(1, T+1):
    MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
val = np.argmax(MLE, axis=0)
print(val)