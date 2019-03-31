#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:31:16 2019

@author: 2021rahul
"""

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
#%%
P_xt1_xt = np.reshape(np.array([[0.6, 0.35, 0.05], [0.2, 0.6, 0.2], [0, 0.5, 0.5]]), (3, 3))
P_et_xt = np.reshape(np.array([[0, 0, 0], [0, 0.05, 0], [0, 0, 0.4]]), (3, 3))
P_notet_xt = np.reshape(np.array([[1, 0, 0], [0, 0.95, 0], [0, 0, 0.6]]), (3, 3))

f = np.zeros((3,4))
f[:,0] = np.array([1/3, 1/3, 1/3])
h = np.zeros((3,4))
h[:,-1] = np.array([1,1,1])
S = np.zeros((3,4))

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:, 0]), (3))
f[:,1] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_notet_xt, np.transpose(P_xt1_xt)), f[:,1]), (3))
f[:,2] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_et_xt, np.transpose(P_xt1_xt)), f[:,2]), (3))
f[:,3] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_xt1_xt, P_et_xt), h[:, 3]), (3))
h[:,2] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_xt1_xt, P_notet_xt), h[:, 2]), (3))
h[:,1] = val/np.sum(val)

val = np.reshape(np.matmul(np.matmul(P_xt1_xt, P_notet_xt), h[:, 1]), (3))
h[:,0] = val/np.sum(val)

S = np.multiply(h, f)
S = np.transpose(np.transpose(S))/np.transpose(sum(S))

#%%
fig, ax = plt.subplots()
ax.plot(f[0,:], "r", label="Filtering Estimates")
ax.plot(S[0,:], "b", label="Smoothed Estimates")
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')
legend.get_frame().set_facecolor('w')
plt.ylabel('P')
plt.xlabel('t')
plt.xticks(np.arange(0, 4, step=1))
plt.title("X=low")
plt.savefig("low.png")
plt.show()

fig, ax = plt.subplots()
ax.plot(f[1,:], "r", label="Filtering Estimates")
ax.plot(S[1,:], "b", label="Smoothed Estimates")
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')
legend.get_frame().set_facecolor('w')
plt.ylabel('P')
plt.xlabel('t')
plt.xticks(np.arange(0, 4, step=1))
plt.title("X=med")
plt.savefig("med.png")
plt.show()

fig, ax = plt.subplots()
ax.plot(f[2,:], "r", label="Filtering Estimates")
ax.plot(S[2,:], "b", label="Smoothed Estimates")
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')
legend.get_frame().set_facecolor('w')
plt.ylabel('P')
plt.xlabel('t')
plt.xticks(np.arange(0, 4, step=1))
plt.title("X=high")
plt.savefig("high.png")
plt.show()