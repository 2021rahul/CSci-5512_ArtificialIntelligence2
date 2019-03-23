#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:42:07 2019

@author: 2021rahul
"""

import numpy as np
import random

def sample(N, prob):
    x = np.zeros(3)
    for i in range(N):
        rand_num = random.uniform(0, 1)
        if rand_num<=prob[0]:
            x[0] += 1
        elif rand_num <= prob[1]+prob[0]:
            x[1] += 1
        else:
            x[2] += 1
    return x

P_0 = np.array([1/3, 1/3, 1/3])
P_xt1_xt = np.reshape(np.array([[0.6, 0.35, 0.05], [0.2, 0.6, 0.2], [0, 0.5, 0.5]]), (3, 3))
P_et_xt = np.array([[0, 0.05, 0.4], [1, 0.95, 0.6]])
#%%
N = 100
E = np.ones(11, dtype=int)
E[[3,4,9]] = 0
X = np.zeros((3,len(E)))
#%%
X[:,0] = sample(N, P_0)
for i in range(1, len(E)):
    X[:, i] = np.add(X[:, i], sample(int(X[0, i-1]), P_xt1_xt[0, :]))
    X[:, i] = np.add(X[:, i], sample(int(X[1, i-1]), P_xt1_xt[1, :]))
    X[:, i] = np.add(X[:, i], sample(int(X[2, i-1]), P_xt1_xt[2, :]))
    prob = np.multiply(X[:,i], P_et_xt[E[i],:])/np.sum(np.multiply(X[:,i], P_et_xt[E[i],:]))
    X[:,i] = sample(N,prob)