#Sheppard's method
from functions import dec2rad, largest_quaternion_square, sqrt_largest, compute_remaining_quat
import numpy as np
from math import cos, sin

# =============================================================================
# INSERTING DCM DIRECTLY
# C11 = -0.529403
# C12 = -0.467056
# C13 = 0.708231
# C21 = -0.474115
# C22 = -0.529403
# C23 = -0.703525
# C31 = 0.703525
# C32 = -0.708231 
# C33 = 0.0588291
# =============================================================================

# INSERTING EULER SEQUENCE 3-2-1
theta_1 = 20
theta_2 = 10
theta_3 = -10

angles = [theta_1, theta_2, theta_3]

angles = dec2rad(angles)
C11 = cos(angles[0])*cos(angles[1])
C12 = sin(angles[0])*cos(angles[1])
C13 = -sin(angles[1])
C21 = cos(angles[0])*sin(angles[1])*sin(angles[2]) - cos(angles[2])*sin(angles[0]) 
C22 = sin(angles[0])*sin(angles[1])*sin(angles[2]) + cos(angles[2])*cos(angles[0])
C23 = cos(angles[1])*sin(angles[2])
C31 = cos(angles[0])*sin(angles[1])*cos(angles[2]) + sin(angles[2])*sin(angles[0])
C32 = sin(angles[0])*sin(angles[1])*cos(angles[2]) - sin(angles[2])*cos(angles[0])
C33 = cos(angles[1])*cos(angles[2])





DCM = np.array([[C11, C12, C13], [C21, C22, C23], [C31, C32, C33]])

betas_2 = np.zeros((4,1))

betas_2[0] = (1/4)*(1 + C11 + C22 + C33)
betas_2[1] = (1/4)*(1 + 2*C11 - (C11 + C22 + C33))
betas_2[2] = (1/4)*(1 + 2*C22 - (C11 + C22 + C33))
betas_2[3] = (1/4)*(1 + 3*C33 - (C11 + C22 + C33))

selected = largest_quaternion_square(betas_2)

print("The largest quaternion is beta_", selected, sep="", end= "\n")

quaternions = sqrt_largest(selected, betas_2)

quaternions = compute_remaining_quat(selected, DCM, quaternions)

print("Final quaternions:\nbeta_0: ", quaternions[0])
print("beta_1: ", quaternions[1])
print("beta_2: ", quaternions[2])
print("beta_3: ", quaternions[3])
print("Satisfying constraint: ", np.linalg.norm(quaternions) )