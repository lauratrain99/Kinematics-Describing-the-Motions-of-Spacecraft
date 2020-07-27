import numpy as np
from functions import CRPtoDCM

v1B = np.array([0.8273, 0.5541, -0.0920])
v2B = np.array([-0.8285, 0.5522, -0.0955])

v1N = np.array([-0.1517, -0.9669, 0.2050])
v2N = np.array([-0.8393, 0.4494, -0.3044])

# q-method parameters
w1 = 1
w2 = 1
B = w1*np.outer(v1B,v1N) + w2*np.outer(v2B,v2N)

S = B + B.T

sigma = np.trace(B)

Z = np.array([B[1,2]-B[2,1], B[2,0]-B[0,2], B[0,1]-B[1,0]])

lamda = w1 + w1

q  = np.linalg.inv((lamda + sigma)*np.eye(3) - S).dot(Z)

BbarN = CRPtoDCM(q)

print(BbarN)

