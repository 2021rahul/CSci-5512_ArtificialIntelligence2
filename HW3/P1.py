#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:35:32 2019

@author: 2021rahul
"""

#%%
import numpy as np

P_xt1_xt = np.reshape(np.array([[0.6, 0.35, 0.05], [0.2, 0.6, 0.2], [0, 0.5, 0.5]]), (3, 3))
P_et_xt = np.reshape(np.array([[0, 0, 0], [0, 0.05, 0], [0, 0, 0.4]]), (3, 3))
P_notet_xt = np.reshape(np.array([[1, 0, 0], [0, 0.95, 0], [0, 0, 0.6]]), (3, 3))

f = np.zeros((3,4))
f[:,0] = np.array([1/3, 1/3, 1/3])

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:, 0]), (3))
f[:,1] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:,1]), (3))
f[:,2] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_et_xt, np.transpose(P_xt1_xt)), f[:,2]), (3))
f[:,3] = val/np.sum(val)
#%% Lecutre Validation
P_xt1_xt = np.reshape(np.array([[0.6, 0.4], [0.9, 0.1]]), (2, 2))
P_et_xt = np.reshape(np.array([[0.3, 0], [0, 0.8]]), (2, 2))
P_notet_xt = np.reshape(np.array([[0.7, 0], [0, 0.2]]), (2, 2))

f = np.zeros((2,3))
f[:,0] = np.array([1/2, 1/2])

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:, 0]), (2))
f[:,1] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:,1]), (2))
f[:,2] = val/np.sum(val)