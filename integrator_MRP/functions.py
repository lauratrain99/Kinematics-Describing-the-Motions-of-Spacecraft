import numpy as np

def eulermethod(sigma, timeVector, angularVelocities):
    for i in range(np.size(timeVector)-1):
        F = (1/4)*np.array([[1 - np.linalg.norm(sigma[:,i])**2 + 2*sigma[0,i]**2, 2*(sigma[0,i]*sigma[1,i] -sigma[2,i]), 2*(sigma[0,i]*sigma[2,i] + sigma[1,i]) ],[2*(sigma[1,i]*sigma[0,i] + sigma[2,i]), 1 - np.linalg.norm(sigma[:,i])**2 + 2*sigma[1,i]**2, 2*(sigma[1,i]*sigma[2,i] -sigma[0,i])],[2*(sigma[2,i]*sigma[0,i] -sigma[1,i]), 2*(sigma[2,i]*sigma[1,i] + sigma[0,i]), 1 - np.linalg.norm(sigma[:,i])**2 + 2*sigma[2,i]**2]])
        #sigma_tilde = np.array([[0, -sigma[2], sigma[1]],[sigma[2], 0, -sigma[0]],[-sigma[1], sigma[0], 0]])
        #F = (1 - np.linalg.norm(sigma[:,i]**2))*np.eye(3) + 2*sigma_tilde + 2*sigma[:,i].dot(sigma[:,i])
        f = F.dot(angularVelocities[:,i])
        sigma[:,i+1] = sigma[:,i] + f*0.01
        
        if abs(np.linalg.norm(sigma[:,i]) >= 1):
            sigma[:,i] = -sigma[:,i]/np.linalg.norm(sigma[:,i])
    return sigma

