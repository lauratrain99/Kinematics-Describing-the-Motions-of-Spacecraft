import numpy as np
from math import sqrt
q = np.array([0.1, 0.2, 0.3])

C11 = 1 + q[0]**2 - q[1]**2 - q[2]**2
C12 = 2*(q[0]*q[1] + q[2])
C13 = 2*(q[0]*q[2] - q[1])
C21 = 2*(q[1]*q[0] - q[2])
C22 = 1 - q[0]**2 + q[1]**2 - q[2]**2
C23 = 2*(q[1]*q[2] + q[0])
C31 = 2*(q[2]*q[0] + q[1])
C32 = 2*(q[2]*q[1] - q[0])
C33 = 1 - q[0]**2 - q[1]**2 + q[2]**2

DCM = (1/(1 + q.dot(q)))*np.array([[C11, C12, C13], [C21, C22, C23], [C31, C32, C33]])

print(DCM)


DCM = np.array([[0.333333, -0.666667, 0.666667],[0.871795, 0.487179, 0.0512821],[-0.358974, 0.564103, 0.74359]])
psi = sqrt(np.trace(DCM) + 1)

q = np.zeros(3)

q[0] = 1/psi**2 *(DCM[1,2] - DCM[2,1])
q[1] = 1/psi**2 *(DCM[2,0] - DCM[0,2])
q[2] = 1/psi**2 *(DCM[0,1] - DCM[1,0])

print(q)


qFN = np.array([0.1, 0.2, 0.3])
qNF = -qFN
qBN = np.array([-0.3, 0.3, 0.1])

qBF = (qBN + qNF - np.cross(qBN,qNF))/(1 - qBN.dot(qNF))

print(qBF)
