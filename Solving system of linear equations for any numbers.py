#program to solve 3x3 matrix
import numpy as np

A = np.array([[int(input("Enter a1")), int(input("Enter b1")), int(input("Enter c1"))], [int(input("Enter a2")),
                                                int(input("Enter b2")), int(input("Enter c2"))], [int(input("Enter a3")), int(input("Enter b3")), int(input("Enter c3"))]]) 
b = np.array([[int(input("Enter d1"))], [int(input("Enter d2"))], [int(input("Enter d3"))]])

xyz = np.linalg.solve(A, b) 
print(xyz)
xyz=list(xyz)
print("x=",xyz[0][0])
print("y=",xyz[1][0])
print("z=",xyz[2][0])

