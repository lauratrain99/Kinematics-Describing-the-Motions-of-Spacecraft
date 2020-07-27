import numpy as np


def eulermethod(quaternion, timeVector, angularVelocities):
    for i in range(np.size(timeVector)-1):
        F = (1/2)*np.array([[0, -angularVelocities[0,i], -angularVelocities[1,i], -angularVelocities[2,i]],[angularVelocities[0,i], 0, angularVelocities[2,i], -angularVelocities[1,i]],[angularVelocities[1,i], -angularVelocities[2,i], 0, angularVelocities[0,i]], [angularVelocities[2,i], angularVelocities[1,i], -angularVelocities[0,i], 0]])
        f = F.dot(quaternion[:,i])
        quaternion[:,i+1] = quaternion[:,i] + f*0.01
    return quaternion
