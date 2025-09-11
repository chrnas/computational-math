import numpy as np

A = np.array([[4, -2, 1],
              [3, 2, -6],
              [1, -1, 1]], dtype=float)

# Calculate multipliers
m21 = A[1, 0] / A[0, 0]  # 3/4 = 0.75
m31 = A[2, 0] / A[0, 0]  # 1/4 = 0.25

# Construct elimination matrix E1
E1 = np.array([[1, 0, 0],
               [-m21, 1, 0],
               [-m31, 0, 1]])

print("E1:\n", E1)

U1 = E1 @ A

print("After first elimination (E1 @ A):\n", U1)