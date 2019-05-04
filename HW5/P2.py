#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:27:18 2019

@author: ghosh128
"""

import numpy as np

raw_data = [
0,1,0,1,1,1,
1,0,1,1,1,1,
0,0,0,0,1,0,
1,1,0,0,1,1,
0,1,0,0,0,0,
0,0,1,1,0,0,
1,1,1,1,1,1,
1,1,1,0,0,0,
1,0,0,0,1,1,
1,1,0,0,1,1,
0,0,0,1,0,1,
0,1,0,1,0,1,
0,1,1,1,1,0,
0,0,1,1,0,0,
0,1,0,0,0,0,
0,0,0,0,0,0,
0,1,0,1,1,1,
1,1,1,1,0,1,
1,0,1,0,0,0,
1,1,0,1,1,1]

data = np.zeros((20, 6))
X = data[:, :-1]
Y = data[:, -1]
#%%
i = 0
while i < 20:
    data[i, :] = raw_data[i*6:(i*6)+6]
    i = i+1
#%%
attribute = 4
mat = np.zeros((2, 2))
mat[0, 0] = len(data[np.logical_and(data[:, attribute] == 0, data[:, 5] == 0), :])
mat[0, 1] = len(data[np.logical_and(data[:, attribute] == 0, data[:, 5] == 1), :])
mat[1, 0] = len(data[np.logical_and(data[:, attribute] == 1, data[:, 5] == 0), :])
mat[1, 1] = len(data[np.logical_and(data[:, attribute] == 1, data[:, 5] == 1), :])
#%%
decisions = np.zeros(5)
decisions[0] = 1
decisions[1] = 1
decisions[2] = 0
decisions[3] = 1
decisions[4] = 1
#%%
from itertools import combinations 
combination = list(combinations([0, 1, 2, 3, 4], 3))
#%%
accuracy = []
for comb in combination:
    pred0 = np.zeros(len(Y))
    pred0[X[:,comb[0]]==decisions[comb[0]]]=1
    pred1 = np.zeros(len(Y))
    pred1[X[:,comb[1]]==decisions[comb[1]]]=1
    pred2 = np.zeros(len(Y))
    pred2[X[:,comb[2]]==decisions[comb[2]]]=1
    actualpred = np.transpose(np.vstack((pred0, pred1, pred2)))
    actualpred = np.sum(actualpred, axis=1)
    pred = np.zeros(len(actualpred))
    pred[actualpred>1] = 1
    accuracy.append(np.sum(pred == Y))
#%%
combination = combination[np.argmax(accuracy)]
