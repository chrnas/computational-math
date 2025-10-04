from Lagrange_interpolation import Lagrange_interpolation
import numpy as np
import matplotlib.pyplot as plt
datapoints = [[(-1,2), (0,0), (1,2)],[(-1,-6), (0,-3), (1,0), (1.5,3.375)]]
 

def build_Interpolation(datapoints, M):
    X = np.linspace(datapoints[0][0], datapoints[-1][0], M)
    L = np.zeros((M,))
    for k in range(M):
        L[k] = Lagrange_interpolation(X[k], datapoints)
    return X,L

L =[]
X = []
for dp in datapoints:
    X_curve, L_curve = build_Interpolation(dp, M=150)
    L.append(L_curve)
    X.append(X_curve)
    x_data = [p[0] for p in dp]
    y_data = [p[1] for p in dp]

    plt.figure(figsize=(8, 6)) # 
    plt.plot(X_curve, L_curve, label='Lagrange Polynomial', color='blue') 
    plt.scatter(x_data, y_data, color='red', zorder=5, label='Data Points') 

    plt.title('Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True) 
    plt.legend() 


    plt.show()


func1 = lambda x: 2*x**2
func2 = lambda x: x**3 + 2*x - 3

print(np.linalg.norm(func1(X[0])-L[0], ord=np.inf))
print(np.linalg.norm(func2(X[1])-L[1], ord=np.inf))