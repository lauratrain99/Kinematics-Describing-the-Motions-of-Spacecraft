import numpy as np

def quaternion_add(R1_quaternion, R2_quaternion):
    matrix = np.array([[R2_quaternion[0], -R2_quaternion[1], -R2_quaternion[2], -R2_quaternion[3]], [R2_quaternion[1], R2_quaternion[0], R2_quaternion[3], -R2_quaternion[2]], [R2_quaternion[2], -R2_quaternion[3], R2_quaternion[0], R2_quaternion[1]], [R2_quaternion[3], R2_quaternion[2], -R2_quaternion[1], R2_quaternion[0]]])
    return matrix.dot(R1_quaternion)