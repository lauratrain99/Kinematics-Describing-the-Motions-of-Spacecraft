import numpy as np
from functions import eulermethod
from math import sqrt, pi

initial_q0 = 0.408248
initial_q1 = 0
initial_q2 = 0.408248
initial_q3 = 0.816497

initial_q = [initial_q0, initial_q1, initial_q2, initial_q3]


tstart = 0.0
tstop = 42.0
step = 0.01
length = int(round(tstop-tstart)/step)
time = np.linspace(tstart,tstop+step,length)

omegas  = (20*pi/180)*np.array([np.sin(0.1*time),np.full(np.shape(time), 0.01),np.cos(0.1*time)])

quaternion = np.zeros((len(initial_q), np.size(time)))

quaternion[:,0] = np.array(initial_q)

quaternion = eulermethod(quaternion, time, omegas)

result = sqrt(quaternion[1,len(time)-1]**2 + quaternion[2,len(time)-1]**2 + quaternion[3,len(time)-1]**2)
print(result)
print(sqrt(quaternion[0,len(time)-1]**2 + quaternion[1,len(time)-1]**2 + quaternion[2,len(time)-1]**2 + quaternion[3,len(time)-1]**2))

