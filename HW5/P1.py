#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:19:33 2019

@author: ghosh128
"""

import pandas as pd
import numpy as np
from scipy.stats import entropy as sc_entropy

df=pd.read_csv('p2Tree.csv', sep=',')
attribute_names = df.columns[1:-1].values
array = df.values[:, 1:]
array = array.astype(int)

X = array[:, :-1]
Y = array[:, -1]

tree = [None]*(np.power(2,X.shape[1]+1))

def entropy(Y):
    value,counts = np.unique(Y, return_counts=True)
    ent = sc_entropy(counts, base=2)
    return ent

def makeTree(X, Y, index):
    if len(np.unique(Y))==1:
        tree[index] = str(np.unique(Y)[0])
        return
    else:
        before_ent = entropy(Y)
        gain = []
        for attribute in range(X.shape[1]):
            left = Y[X[:,attribute]==1]
            left_ent = entropy(left)

            right = Y[X[:,attribute]==0]
            right_ent = entropy(right)

            attribute_ent = len(left)/(len(left)+len(right))*left_ent + len(right)/(len(left)+len(right))*right_ent
            gain.append(before_ent-attribute_ent)
#            print("check", attribute, " gain:", gain[-1])
        attribute = np.argmax(gain)
#        print(index, ":", attribute)
        tree[index] = attribute_names[attribute]
        
        makeTree(X[X[:,attribute]==1, :], Y[X[:,attribute]==1], 2*index)
        makeTree(X[X[:,attribute]==0, :], Y[X[:,attribute]==0], 2*index + 1)

makeTree(X, Y, 1)
index = np.power(2,len(attribute_names)+1)-1
while index>=0:
    if tree[index] is not None:
        break
    index -= 1
index = np.power(2, int(np.log2(index))+1)
tree = np.array(tree[1:index])
tree[list(np.where(np.array(tree) == None)[0])] = " "
tree = list(tree)

print("_".join(tree))