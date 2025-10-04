from Lagrange_interpolation import Lagrange_interpolation, build_Interpolation
import numpy as np
import matplotlib.pyplot as plt

datapoints = [[(-1,2), (0,0), (1,2)],[(-1,-6), (0,-3), (1,0), (1.5,3.375)]]
X_list = []
L_list = []
for i in datapoints:
    X, L = build_Interpolation(i,M=150)
    X_list.append(X)
    L_list.append(L)
func1 = lambda x: 2*x**2
func2 = lambda x: x**3 + 2*x - 3

print(np.linalg.norm(func1(X_list[0])-L_list[0], ord=np.inf))
print(np.linalg.norm(func2(X_list[1])-L_list[1], ord=np.inf))