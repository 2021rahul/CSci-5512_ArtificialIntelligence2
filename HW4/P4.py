#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:54:39 2019

@author: ghosh128
"""

#MDP
import copy

rows = 4
columns = 3
reward = [[None, 50, None], [None, 0, -3], [-50, -1, -10], [None, -3, -2]]
terminal_states = [(1, 0), (3, 1)]
state = [[None, 50, None], [None, 0, 0], [-50, 0, 0], [None, 0, 0]]
probability = [0.7, 0.15, 0.15]
gamma = 0.8
index_list = [[0,1], [1,1], [1,2], [1,3], [2,0], [2,1], [2,3], [3,1], [3,2], [3,3]]

def action_list(action):
    if not action[1]:
        return [action, [0, -1], [0, 1]]
    else:
        return [action, [-1, 0], [1, 0]]

def get_equation(i, j):
    if 