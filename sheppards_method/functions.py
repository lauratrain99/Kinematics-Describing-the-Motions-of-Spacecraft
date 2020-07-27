
from math import sqrt, pi
import numpy as np

def dec2rad(angles):
    return [angle*pi/180 for angle in angles]

def largest_quaternion_square(square_betas):
    if max(square_betas) == square_betas[0]:
        return 0
    elif max(square_betas) == square_betas[1]:
        return 1
    elif max(square_betas) == square_betas[2]:
        return 2
    else:
        return 3

def sqrt_largest(largestBetaSquare, square_betas):
    betas = np.zeros((4,1))
    if largestBetaSquare == 0:
        betas[0] = sqrt(square_betas[0])
    elif largestBetaSquare == 1:
        betas[1] = sqrt(square_betas[1])
    elif largestBetaSquare == 2:
        betas[2] = sqrt(square_betas[2])
    else:
        betas[3] = sqrt(square_betas[3])
    return betas

def compute_remaining_quat(largestBetaSquare, DCM, betas):
    if largestBetaSquare == 0:
        betas[1] = (DCM[1,2] - DCM[2,1])/(4*betas[0])
        betas[2] = (DCM[2,0] - DCM[0,2])/(4*betas[0])
        betas[3] = (DCM[0,1] - DCM[1,0])/(4*betas[0])
    elif largestBetaSquare == 1:
        betas[0] = (DCM[1,2] - DCM[2,1])/(4*betas[1])
        betas[2] = (DCM[0,1] + DCM[1,0])/(4*betas[1])
        betas[3] = (DCM[2,0] + DCM[0,2])/(4*betas[1])
    elif largestBetaSquare == 2:
        betas[0] = (DCM[2,0] - DCM[0,2])/(4*betas[2])
        betas[1] = (DCM[0,1] + DCM[1,0])/(4*betas[2])
        betas[3] = (DCM[1,2] + DCM[2,1])/(4*betas[2])
    else:
        betas[0] = (DCM[0,1] - DCM[1,0])/(4*betas[3])
        betas[1] = (DCM[2,0] + DCM[0,2])/(4*betas[3])
        betas[2] = (DCM[1,2] + DCM[2,1])/(4*betas[3])
    return betas