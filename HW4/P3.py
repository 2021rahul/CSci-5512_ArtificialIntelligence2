#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:44:11 2019

@author: ghosh128
"""

#MDP
import copy
import random
import numpy as np
import matplotlib.pyplot as plt

ACTIONS = []
ACTIONS.append([-1, 0])
ACTIONS.append([1, 0])
ACTIONS.append([0, -1])
ACTIONS.append([0, 1])

rows = 4
columns = 3
reward = [[None, 50, None],
          [None, 0, -3],
          [-50, -1, -10],
          [None, -3, -2]]
index_list = [[0,1], [1,1], [1,2], [2,0], [2,1], [2,2], [3,1], [3,2]]
terminal_states = [[0, 1], [2, 0]]

probability = [0.7, 0.15, 0.15]

gamma = 0.8

state = [[None, 50, None],
         [None, 4, 8],
         [-50, 7, 4],
         [None, 9, 5]]
#%%

def action_list(action):
    if not action[1]:
        return [action, [0, -1], [0, 1]]
    else:
        return [action, [-1, 0], [1, 0]]

def get_best_action(i,j):
    value_up = apply_action(ACTIONS[0], i, j)
    value_down = apply_action(ACTIONS[1], i, j)
    value_left = apply_action(ACTIONS[2], i, j)
    value_right = apply_action(ACTIONS[3], i, j)
    return np.argmax([value_up, value_down, value_left, value_right])

def apply_action(action, i, j):
    actions = action_list(action)
    value = 0
    for step,action in enumerate(actions):
        new_i = i+action[0]
        new_j = j+action[1]
        if new_i<0 or new_i>=rows or new_j<0 or new_j>=columns or reward[new_i][new_j] is None:
            new_i = i
            new_j = j
#            print(new_i, new_j, probability[step]*state[new_i][new_j])
        value += probability[step]*state[new_i][new_j]
    return value

def get_values(i, j):
    value_up = apply_action([-1, 0], i, j)
    value_down = apply_action([1, 0], i, j)
    value_left = apply_action([0, 1], i, j)
    value_right = apply_action([0, -1], i, j)
    return [value_up, value_down, value_left, value_right]

#%%
policy = copy.deepcopy(state)
count=0
for i, index in enumerate(index_list):
    if index not in terminal_states:
        policy[index[0]][index[1]] = ACTIONS[get_best_action(index[0], index[1])]
        
state1 = [state]
iter = 0
count = len(index_list)
while count != 0:
    new_state = copy.deepcopy(state)
    for i in range(rows):
        for j in range(columns):
    #        print(i, j)
            if [i, j] not in terminal_states and reward[i][j] is not None:
                new_state[i][j] = reward[i][j] + gamma*max(get_values(i, j))
    #            print(i, j, new_state[i][j])
    state = new_state
    state1.append(state)
    
    new_policy = copy.deepcopy(state)
    count=0
    for i, index in enumerate(index_list):
        if index not in terminal_states:
            new_policy[index[0]][index[1]] = ACTIONS[get_best_action(index[0], index[1])]
            if new_policy[index[0]][index[1]][0] is not policy[index[0]][index[1]][0] or new_policy[index[0]][index[1]][1] is not policy[index[0]][index[1]][1]:
                print(new_policy[index[0]][index[1]], policy[index[0]][index[1]])
                count += 1
    policy = copy.deepcopy(new_policy)
    iter += 1
    print(iter, count)
#%%
state = [[None, 50, None],
         [None, 0, 0],
         [-50, 0, 0],
         [None, 0, 0]]

policy = copy.deepcopy(state)
count=0
for i, index in enumerate(index_list):
    if index not in terminal_states:
        policy[index[0]][index[1]] = ACTIONS[get_best_action(index[0], index[1])]

state2 = [state]
iter = 0
count = len(index_list)
while count != 0:
    new_state = copy.deepcopy(state)
    for i in range(rows):
        for j in range(columns):
    #        print(i, j)
            if [i, j] not in terminal_states and reward[i][j] is not None:
                new_state[i][j] = reward[i][j] + gamma*max(get_values(i, j))
    #            print(i, j, new_state[i][j])
    state = new_state
    state2.append(state)
    
    new_policy = copy.deepcopy(state)
    count=0
    for i, index in enumerate(index_list):
        if index not in terminal_states:
            new_policy[index[0]][index[1]] = ACTIONS[get_best_action(index[0], index[1])]
            if new_policy[index[0]][index[1]][0] is not policy[index[0]][index[1]][0] or new_policy[index[0]][index[1]][1] is not policy[index[0]][index[1]][1]:
                print(new_policy[index[0]][index[1]], policy[index[0]][index[1]])
                count += 1
    policy = copy.deepcopy(new_policy)
    iter += 1
    print(iter, count)
#%%
difference = []
for i in range(len(state1)):
    U1 = state1[i]
    U2 = state2[i]
    diff=0
    for index in index_list:
        diff += U1[index[0]][index[1]] - U2[index[0]][index[1]]
    difference.append(diff)

plt.figure(figsize=(10,10))
plt.yticks(np.arange(0, 40, step=1))
plt.xticks(np.arange(0, 4, step=1))
plt.grid()
plt.plot(0.8*np.array(difference[1:]), "b", label="0.8*|U1-U1'|")
plt.plot(np.array(difference[:-1]), "r", label="|U0-U0'|")
legend = plt.legend(loc='upper right', shadow=True, fontsize='x-small')
plt.savefig("P3.png")