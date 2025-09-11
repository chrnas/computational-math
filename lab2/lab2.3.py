import numpy as np
from lufact import lufact

A = np.array([[4, -2, 1],[3, 2, -6],[1, -1, 1]])

L, U, P = lufact(A)

B = np.array([[2.0, 0.0, 6.0, 3.0], [-4.0, 0.0, 1.0, -9.0],
[1.0, 11.0, 2.0, -4.75], [-2.0, 6.0, -7.0, -11.0]])

L, U, P = lufact(B)

print(L)
print(U)
print(P)