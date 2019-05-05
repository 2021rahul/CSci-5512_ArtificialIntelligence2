#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:29:14 2019

@author: ghosh128
"""

import numpy as np

in1 = 0.6
in2 = 0.5
in3 = 0.3

w1 = 0.5
w2 = 0.3
w3 = 0.4
w4 = 0.6
w5 = 1
w6 = 0.7
w7 = -0.3
w8 = -0.5
w9 = 0.9

N1in = w1*in1 + w2*in2
N1 = 1/(1 + np.exp(-N1in))

N2in = w3*in2 + w4*in3
N2 = 1/(1 + np.exp(-N2in))

N3in = N1*w5
N3 = 1/(1 + np.exp(-N3in))

N4in = w6*N1 + w7*N2
N4 = 1/(1 + np.exp(-N4in))

N5in = w8*N3 + w9*N4
N5 = 1/(1 + np.exp(-N5in))