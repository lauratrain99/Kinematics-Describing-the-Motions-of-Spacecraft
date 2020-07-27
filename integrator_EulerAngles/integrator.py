import numpy as np
from functions import deg2rad, eulermethod
from math import sqrt, pi

initial_yaw = 40
initial_pitch = 30
initial_roll = 80

initial_angles = [initial_yaw, initial_pitch, initial_roll]
initial_angles = deg2rad(initial_angles)

tstart = 0.0
tstop = 42.0
step = 0.01
length = int(round(tstop-tstart)/step)
time = np.linspace(tstart,tstop+step,length)

omegas  = (20*pi/180)*np.array([np.sin(0.1*time),np.full(np.shape(time), 0.01),np.cos(0.1*time)])

angles = np.zeros((len(initial_angles), np.size(time)))

angles[:,0] = np.array(initial_angles)

angles = eulermethod(angles, time, omegas)

result = sqrt(angles[0,len(time)-1]**2 + angles[1,len(time)-1]**2 + angles[2,len(time)-1]**2)
print(result)