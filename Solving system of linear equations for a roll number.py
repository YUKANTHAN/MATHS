#program to solve 3x3 matrix
import numpy as np
N=int(input("Enter a roll number"))
A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]]) 
b = np.array([[N], [15], [14]])
xyz = np.linalg.solve(A, b)
print("For the roll number:",N)
print(xyz)
xyz=list(xyz)
print("x=",xyz[0])
print("y=",xyz[1])
print("z=",xyz[2])

