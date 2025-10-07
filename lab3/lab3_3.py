from Lagrange_interpolation import Lagrange_interpolation, build_Interpolation
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial

datapoints = [(1,1), (2,1), (3,2), (4,6), (5,24)]

X, L = build_Interpolation(datapoints, M =150)

x_values = np.linspace(0.1, 6, 400) 
y_gamma = gamma(x_values)


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_gamma, label='Gamma Function (Γ(x))', color='blue', linewidth=2)

plt.title('True Gamma Function')
plt.xlabel('x')
plt.ylabel('Γ(x)')
plt.grid(True)
plt.legend()

plt.show()

print("absolute error:", abs(np.sqrt(np.pi)/2-Lagrange_interpolation(1.5, datapoints)))
print("relative error:", abs(np.sqrt(np.pi)/2-Lagrange_interpolation(1.5, datapoints))/np.sqrt(np.pi)/2)

print("absolute error:", abs(120-Lagrange_interpolation(6, datapoints)))
print("relative error:", abs(120-Lagrange_interpolation(6, datapoints))/120)