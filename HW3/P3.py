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
#Evidence till day 6
T=6
E = np.ones(T+1, dtype=int)
E[[1,4,6]] = 0
MLE = np.zeros((len(P_0), T+1), dtype=float)
MLE[:,0] = P_0

for t in range(1, T+1):
    MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
val = np.argmax(MLE, axis=0)
print(val)
#%%
T=5
E = np.ones(T+1, dtype=int)
E[[1,4]] = 0
MLE = np.zeros((len(P_0), T+1), dtype=float)
MLE[:,0] = P_0
#%%
t=1
MLE1 = P_et_xt[:,E[t]]*(P_xt1_xt.T*MLE[:,t-1]).T
MLE[:,t] = np.amax(MLE1, axis=0)
t=2
MLE2 = P_et_xt[:,E[t]]*(P_xt1_xt.T*MLE[:,t-1]).T
MLE[:,t] = np.amax(MLE2, axis=0)
t=3
MLE3 = P_et_xt[:,E[t]]*(P_xt1_xt.T*MLE[:,t-1]).T
MLE[:,t] = np.amax(MLE3, axis=0)
t=4
MLE4 = P_et_xt[:,E[t]]*(P_xt1_xt.T*MLE[:,t-1]).T
MLE[:,t] = np.amax(MLE4, axis=0)
t=5
MLE5 = P_et_xt[:,E[t]]*(P_xt1_xt.T*MLE[:,t-1]).T
MLE[:,t] = np.amax(MLE5, axis=0)

#%% Lecutre Validation
#P_0 = np.array([1/2, 1/2])
#P_xt1_xt = np.reshape(np.array([[0.9, 0.1], [1, 0]]), (2, 2))
#P_et_xt = np.transpose(np.array([[0.01, 1], [0.99, 0]]))
#
#T=4
#E = np.ones(T+1, dtype=int)
#E[[2,3]] = 0
#MLE = np.zeros((len(P_0), T+1), dtype=float)
#MLE[:,0] = P_0
#
#t=1
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)/np.sum(P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0))
#t=2
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#t=3
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#t=4
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#
#
#for t in range(1, T+1):
#    MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#val = np.argmax(MLE, axis=0)
#print(val)
##%%
#P_0 = np.array([0.5, 0.5])
#P_xt1_xt = np.reshape(np.array([[0.7, 0.3], [0.3, 0.7]]), (2, 2))
#P_et_xt = np.transpose(np.array([[0.9, 0.2], [0.1, 0.8]]))
#
#T=5
#E = np.zeros(T+1, dtype=int)
#E[[3]] = 1
#MLE = np.zeros((len(P_0), T+1), dtype=float)
#MLE[:,0] = P_0
#
#t=1
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)/np.sum(P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0))
#t=2
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#t=3
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#t=4
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#t=5
#MLE[:,t] = P_et_xt[:,E[t]] * np.amax((P_xt1_xt.T*MLE[:,t-1]).T, axis=0)
#
#val = np.argmax(MLE, axis=0)
#print(val)