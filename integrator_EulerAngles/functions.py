from math import pi,cos,sin
import numpy as np

def deg2rad(listDeg):
    listRad = [angle*pi/180 for angle in listDeg]
    return listRad
        


def eulermethod(angles, timeVector, angularVelocities):
    for i in range(np.size(timeVector)-1):
        F = (1/cos(angles[1,i]))*np.array([[0, sin(angles[2,i]), cos(angles[2,i])],[0, cos(angles[2,i])*cos(angles[1,i]), -sin(angles[2,i])*cos(angles[1,i])],[cos(angles[1,i]), sin(angles[2,i])*sin(angles[1,i]), cos(angles[2,i])*sin(angles[1,i])]])
        f = F.dot(angularVelocities[:,i])
        angles[:,i+1] = angles[:,i] + f*0.01
    return angles
