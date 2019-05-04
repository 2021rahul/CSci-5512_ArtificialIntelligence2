#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:04:40 2019

@author: ghosh128
"""

a=0.2
b=0.3
c=0
d=0.5

Reward_S = - a - 4*b + c - 2*d

#move LEFT
A = 0.3*(0.85*a + 0.7*b + 0.15*c + 0*d)
B = 0*(0*a + 0.15*b + 0*c + 0.15*d)
C = 0.9*(0.15*a + 0*b + 0.85*c + 0.7*d)
D = 0.2*(0*a + 0.15*b + 0*c + 0.15*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S1 = - a - 4*b + c - 2*d

#move DOWN
A = 0.3*(0.15*a + 0.15*b + 0*c + 0*d)
B = 0*(0.15*a + 0.15*b + 0*c + 0*d)
C = 0.9*(0.7*a + 0*b + 0.85*c + 0.15*d)
D = 0.2*(0*a + 0.7*b + 0.15*c + 0.85*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S2 = c - a - 4*b - 2*d
#%%
a=0.2
b=0.3
c=0
d=0.5

Reward_S = - a - 4*b + c - 2*d

#move LEFT
A = 0.3*(0.85*a + 0.7*b + 0.15*c + 0*d)
B = 0*(0*a + 0.15*b + 0*c + 0.15*d)
C = 0.9*(0.15*a + 0*b + 0.85*c + 0.7*d)
D = 0.2*(0*a + 0.15*b + 0*c + 0.15*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S1 = - a - 4*b + c - 2*d

#move LEFT
A = 0.3*(0.85*a + 0.7*b + 0.15*c + 0*d)
B = 0*(0*a + 0.15*b + 0*c + 0.15*d)
C = 0.9*(0.15*a + 0*b + 0.85*c + 0.7*d)
D = 0.2*(0*a + 0.15*b + 0*c + 0.15*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S2 = - a - 4*b + c - 2*d
#%%
a=0.2
b=0.3
c=0
d=0.5

Reward_S = - a - 4*b + c - 2*d

#move DOWN
A = 0.3*(0.15*a + 0.15*b + 0*c + 0*d)
B = 0*(0.15*a + 0.15*b + 0*c + 0*d)
C = 0.9*(0.7*a + 0*b + 0.85*c + 0.15*d)
D = 0.2*(0*a + 0.7*b + 0.15*c + 0.85*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)
#%%
Reward_S1 = - a - 4*b + c - 2*d

#move LEFT
A = 0.3*(0.85*a + 0.7*b + 0.15*c + 0*d)
B = 0*(0*a + 0.15*b + 0*c + 0.15*d)
C = 0.9*(0.15*a + 0*b + 0.85*c + 0.7*d)
D = 0.2*(0*a + 0.15*b + 0*c + 0.15*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S2 = - a - 4*b + c - 2*d
#%%
a=0.2
b=0.3
c=0
d=0.5

Reward_S = - a - 4*b + c - 2*d

#move DOWN
A = 0.3*(0.15*a + 0.15*b + 0*c + 0*d)
B = 0*(0.15*a + 0.15*b + 0*c + 0*d)
C = 0.9*(0.7*a + 0*b + 0.85*c + 0.15*d)
D = 0.2*(0*a + 0.7*b + 0.15*c + 0.85*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)
#%%
Reward_S1 = - a - 4*b + c - 2*d

#move DOWN
A = 0.3*(0.15*a + 0.15*b + 0*c + 0*d)
B = 0*(0.15*a + 0.15*b + 0*c + 0*d)
C = 0.9*(0.7*a + 0*b + 0.85*c + 0.15*d)
D = 0.2*(0*a + 0.7*b + 0.15*c + 0.85*d)
a=A/(A+B+C+D)
b=B/(A+B+C+D)
c=C/(A+B+C+D)
d=D/(A+B+C+D)

Reward_S2 = - a - 4*b + c - 2*d