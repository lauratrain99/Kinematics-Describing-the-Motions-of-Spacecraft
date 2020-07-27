import numpy as np


def eulermethod(q, timeVector, angularVelocities):
    for i in range(np.size(timeVector)-1):
        F = (1/2)*np.array([[1 + q[0,i]**2, q[0,i]*q[1,i] - q[2,i], q[0,i]*q[2,i] + q[1,i]],[q[1,i]*q[0,i] + q[2,i], 1 + q[1,i]**2, q[1,i]*q[2,i] - q[0,i]],[q[2,i]*q[0,i] - q[1,i], q[2,i]*q[1,i] + q[0,i], 1 + q[2,i]**2]])
        f = F.dot(angularVelocities[:,i])
        q[:,i+1] = q[:,i] + f*0.01
    return q

