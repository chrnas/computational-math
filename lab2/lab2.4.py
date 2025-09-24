import numpy as np
from thinQR import thinQR
from DrawCurveFit import DrawCurveFit


t = np.linspace(0, 0.384, 49)
y = np.array([60.5620, 60.8120, 61.8750, 64.1250, 67.7500, 72.3120, 77.0000, 81.1880, 84.5620, 87.3750, 89.7500, 91.8120, 93.5620, 94.9380, 95.8750, 96.4380, 96.6250, 96.5000, 96.0620, 95.4380, 94.4380, 92.9380, 90.6250, 87.8120, 85.3750, 83.4380, 81.9380, 80.5000, 79.1880, 78.0000, 76.8120, 75.7500, 74.6880, 73.6880, 72.6250, 71.6250, 70.6250, 69.6880, 68.7500, 67.8750, 67.0000, 66.1250, 65.2500, 64.3120, 63.3750, 62.5620, 61.8120, 61.1880, 60.7500])
# Given data
t = np.linspace(0, 0.384, 49)
T = t[-1] - t[0]  # total duration

# Construct matrix A
A = np.column_stack([
    np.ones_like(t),
    np.cos(2 * np.pi * t / T),
    np.sin(2 * np.pi * t / T),
    np.cos(4 * np.pi * t / T),
    np.sin(4 * np.pi * t / T)
])
np.set_printoptions(precision=4, suppress=True)
#print(A)
Q, R = thinQR(A)
c = np.linalg.solve(R, Q.T @ y) 
DrawCurveFit(c, t, y)
print("Q:", Q)
print("R:", R)
print("c",c)