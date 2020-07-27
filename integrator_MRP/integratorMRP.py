import numpy as np
from functions import eulermethod
from math import sqrt, pi

initial_sigma1 = 0.4
initial_sigma2 = 0.2
initial_sigma3 = -0.1

initial_sigma = [initial_sigma1, initial_sigma2, initial_sigma3]


tstart = 0.0
tstop = 42.0
step = 0.01
length = int(round(tstop-tstart)/step)
time = np.linspace(tstart,tstop+step,length)

omegas  = (20*pi/180)*np.array([np.sin(0.1*time),np.full(np.shape(time), 0.01),np.cos(0.1*time)])

sigma = np.zeros((len(initial_sigma), np.size(time)))

sigma[:,0] = np.array(initial_sigma)

sigma = eulermethod(sigma, time, omegas)

result = sqrt(sigma[0,len(time)-1]**2 + sigma[1,len(time)-1]**2 + sigma[2,len(time)-1]**2)
print(result)

