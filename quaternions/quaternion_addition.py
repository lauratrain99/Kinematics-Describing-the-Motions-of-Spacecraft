from functions import quaternion_add
import numpy as np

### From B to N
quaternionBN = [0.774597, 0.258199, 0.516398, 0.258199]

### From F to B
quaternionFB = [0.359211, 0.898027, 0.179605, 0.179605]


quaternionFN = quaternion_add(quaternionBN, quaternionFB)

print("Final quaternions:\nbeta_0: ", quaternionFN[0])
print("beta_1: ", quaternionFN[1])
print("beta_2: ", quaternionFN[2])
print("beta_3: ", quaternionFN[3])
print("Satisfying constraint: ", np.linalg.norm(quaternionFN) )



### From F to N
quaternionFN = [0.359211, 0.898027, 0.179605, 0.179605]

### From B to N
quaternionBN = [-0.377964, 0.755929, 0.377964, 0.377964]

quaternionNB = [quaternionBN[0], -quaternionBN[1], -quaternionBN[2], -quaternionBN[3]]

quaternionFB = quaternion_add(quaternionFN, quaternionNB)

print("Final quaternions:\nbeta_0: ", quaternionFB[0])
print("beta_1: ", quaternionFB[1])
print("beta_2: ", quaternionFB[2])
print("beta_3: ", quaternionFB[3])
print("Satisfying constraint: ", np.linalg.norm(quaternionFB) )