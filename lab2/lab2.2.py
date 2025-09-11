import numpy as np
from gaussSeidel import gaussSeidel

# Test gausseidel implementation
n = 10
main_diag = 2.1 * np.ones(n)
off_diag = -1 * np.ones(n - 1)
C = np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)

b = np.ones(n)
x0 = np.zeros(n)
tol = 1e-5

x, k = gaussSeidel(C, b, x0, tol)

print(f"Solution: {x}")
print(f"Number of iterations: {k}")

# Test gausseidel implementation

x0 = np.ones(n)*3.5

b = C @ x0 # Compute the right-hand side
print("b:", b)

x0 = np.ones(n)
tol = 1e-8
max_its = 500
xVals, iter_count = gaussSeidel(C, b, x0, tol, max_its)

print(f"Solution: {xVals}")
print(f"Number of iterations: {iter_count}")