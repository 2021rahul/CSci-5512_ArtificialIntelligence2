#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:59:27 2019

@author: ghosh128
"""

import numpy as np
#%%
Parent = np.asarray([8, 11]) 
children = np.asarray([[1, 8], [2, 0], [5, 3]])
#%%
Parent = np.asarray([1, 8]) 
children = np.asarray([[1, 1], [0, 7]])
#%%
Parent = np.asarray([5, 3]) 
children = np.asarray([[3, 0], [2, 1], [0, 2]])
#%%
Parent = np.asarray([1, 1]) 
children = np.asarray([[1, 0], [0, 1]])
#%%
Parent = np.asarray([2, 1]) 
children = np.asarray([[2, 0], [0, 1]])
#%%
x = 0
for child in children:
    total = np.sum(child)
    print(total)
    for val in range(2):
        print(pow(child[val]-(np.sum(child)*Parent[val]/np.sum(Parent)),2)/(np.sum(child)*Parent[val]/np.sum(Parent)))
        x += pow(child[val]-(np.sum(child)*Parent[val]/np.sum(Parent)),2)/(np.sum(child)*Parent[val]/np.sum(Parent))
