import numpy as np
from math import acos,pi

v1B = np.array([0.8273, 0.5541, -0.0920])
v2B = np.array([-0.8285, 0.5522, -0.0955])

v1N = np.array([-0.1517, -0.9669, 0.2050])
v2N = np.array([-0.8393, 0.4494, -0.3044])

t1B = v1B/np.linalg.norm(v1B)
t2B = np.cross(v1B,v2B)/np.linalg.norm(np.cross(v1B,v2B))
t3B = np.cross(t1B,t2B)

t1N = v1N/np.linalg.norm(v1N)
t2N = np.cross(v1N,v2N)/np.linalg.norm(np.cross(v1N,v2N))
t3N = np.cross(t1N,t2N)

BT  = np.array([t1B, t2B, t3B]).T

NT = np.array([t1N, t2N, t3N]).T

print(BT.dot(NT))

# check accuracy

B_barN = np.array([[0.969846, 0.17101, 0.17364],[-0.200706, 0.96461, 0.17101],[-0.138258, -0.200706, 0.969846]])
BN_true = np.array([[0.963592, 0.187303, 0.190809],[-0.223042, 0.956645, 0.187303],[-0.147454, -0.223042, 0.963592]])

DCM = B_barN.dot(BN_true.T)

# DCM to principal rotation vector

angle = acos((1/2)*(DCM[0,0] + DCM[1,1] + DCM[2,2] - 1))

print(angle*180/pi)