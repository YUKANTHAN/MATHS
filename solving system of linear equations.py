import numpy as np

A = np.array([[2, 1, 1], [1, 3, 4], [2, 1, 2]]) 
b = np.array([[180], [300], [240]])

xyz = np.linalg.solve(A, b) 
print(xyz)

