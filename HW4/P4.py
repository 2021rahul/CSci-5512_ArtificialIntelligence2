#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:54:39 2019

@author: ghosh128
"""

#MDP
import copy
import numpy as np

ACTIONS = []
ACTIONS.append([-1, 0])
ACTIONS.append([1, 0])
ACTIONS.append([0, -1])
ACTIONS.append([0, 1])

rows = 4
columns = 3
reward = [[None, 50, None], [None, 0, -3], [-50, -1, -10], [None, -3, -2]]
terminal_states = [(0, 1), (2, 0)]
state = [[None, 50, None], [None, 0, 0], [-50, 0, 0], [None, 0, 0]]
policy = [[None, 50, None], [None, ACTIONS[0], ACTIONS[0]], [-50, ACTIONS[0], ACTIONS[0]], [None, ACTIONS[0], ACTIONS[0]]]
probability = [0.7, 0.15, 0.15]
gamma = 0.8
index_list = [[0,1], [1,1], [1,2], [2,0], [2,1], [3,1], [3,2]]

rows = 4
columns = 4
reward = [[None, 50, None, None], [None, -1, -1, -1], [-50, -1, None, -1], [None, -1, -1, -1]]
terminal_states = [(0, 1), (2, 0)]
state = [[None, 50, None, None], [None, 0, 0, 0], [-50, 0, None, 0], [None, 0, 0, 0]]
policy = [[None, 50, None, None], [None, ACTIONS[0], ACTIONS[2], ACTIONS[2]], [-50, ACTIONS[3], None, ACTIONS[0]], [None, ACTIONS[0], ACTIONS[2], ACTIONS[0]]]
probability = [0.8, 0.1, 0.1]
gamma = 1
index_list = [[0,1], [1,1], [1,2], [1,3], [2,0], [2,1], [2,3], [3,1], [3,2], [3,3]]

def action_list(action):
    if not action[1]:
        return [action, [0, -1], [0, 1]]
    else:
        return [action, [-1, 0], [1, 0]]

def apply_action(action, i, j):
    actions = action_list(action)
    value = 0
    for step,action in enumerate(actions):
        new_i = i+action[0]
        new_j = j+action[1]
        print(new_i, new_j)
        if new_i<0 or new_i>=rows or new_j<0 or new_j>=columns or reward[new_i][new_j] is None:
            new_i = i
            new_j = j
#            print(new_i, new_j, probability[step]*state[new_i][new_j])
        value += probability[step]*state[new_i][new_j]
    return value

def get_equation(i, j):
    a = np.zeros(len(index_list))
    b = reward[i][j]
    a[index_list.index([i, j])] = 1
    if (i, j) in terminal_states:
        return a, b
    else:
#        print(i, j)
        actions = action_list(policy[i][j])
#        print(actions)
        for step, action in enumerate(actions):
            new_i = i+action[0]
            new_j = j+action[1]
            if new_i<0 or new_i>=rows or new_j<0 or new_j>=columns or reward[new_i][new_j] is None:
                new_i = i
                new_j = j
            a[index_list.index([new_i, new_j])] += (-1*gamma*probability[step])
        return a, b
    
def get_best_action(i,j):
    value_up = apply_action(ACTIONS[0], i, j)
    value_down = apply_action(ACTIONS[1], i, j)
    value_left = apply_action(ACTIONS[2], i, j)
    value_right = apply_action(ACTIONS[3], i, j)
    return np.argmax([value_up, value_down, value_left, value_right])
    
#%%
A = np.zeros(10)
B = []
for index in index_list:
    a, b = get_equation(index[0], index[1])
    A = np.vstack((A, np.reshape(a, (1,-1))))
    B.append(b)
A = A[1:,:]
x = np.linalg.solve(A, B)

for i, index in enumerate(index_list):
    if index not in terminal_states:
        state[index[0]][index[1]] = x[i]

for i, index in enumerate(index_list):
    if index not in terminal_states:
        policy[index[0]][index[1]] = ACTIONS[get_best_action(index[0], index[1])]
#%%
a, b = get_equation(3,3)

