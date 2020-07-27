import numpy as np
def quaternionToDCM(q):
    C11 = q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2
    C12 = 2*(q[1]*q[2] + q[0]*q[3])
    C13 = 2*(q[1]*q[3] - q[0]*q[2])
    C21 = 2*(q[1]*q[2] - q[0]*q[3])
    C22 = q[0]**2 - q[1]**2 + q[2]**2 - q[3]**2
    C23 = 2*(q[2]*q[3] + q[0]*q[1])
    C31 = 2*(q[1]*q[3] + q[0]*q[2])
    C32 = 2*(q[2]*q[3] - q[0]*q[1])
    C33 = q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2
    DCM = np.array([[C11, C12, C13],[C21, C22, C23],[C31,C32,C33]])
    return DCM

def CRPtoDCM(q):
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
    return DCM