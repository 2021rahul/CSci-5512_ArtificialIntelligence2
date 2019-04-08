#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:44:11 2019

@author: ghosh128
"""

#MDP
import copy

rows = 4
columns = 3
reward = [[None, 50, None], [None, 0, -3], [-50, -1, -10], [None, -3, -2]]
terminal_states = [(0, 1), (2, 0)]
state = [[None, 50, None], [None, 0, 0], [-50, 0, 0], [None, 0, 0]]
probability = [0.7, 0.15, 0.15]
gamma = 0.8

#rows = 4
#columns = 4
#reward = [[None, 50, None, None], [None, -1, -1, -1], [-50, -1, None, -1], [None, -1, -1, -1]]
#terminal_states = [(0, 1), (2, 0)]
#state = [[None, 50, None, None], [None, 0, 0, 0], [-50, 0, None, 0], [None, 0, 0, 0]]
#probability = [0.8, 0.1, 0.1]
#gamma = 0.9

def action_list(action):
    if not action[1]:
        return [action, [0, -1], [0, 1]]
    else:
        return [action, [-1, 0], [1, 0]]

def apply_action(action, i, j):
    actions = action_list(action)
    value = 0
    for step,action in enumerate(actions):
        if i+action[0]>=0 and i+action[0]<rows and j+action[1]>=0 and j+action[1]<columns:
            new_i = i+action[0]
            new_j = j+action[1]
            if reward[new_i][new_j] is None:
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

for i in range(1000):
    new_state = copy.deepcopy(state)
    for i in range(rows):
        for j in range(columns):
    #        print(i, j)
            if (i, j) not in terminal_states and reward[i][j] is not None:
                new_state[i][j] = reward[i][j] + gamma*max(get_values(i, j))
    #            print(i, j, new_state[i][j])
    state = new_state