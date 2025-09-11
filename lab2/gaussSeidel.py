import numpy as np

def gaussSeidel(A, b, x0, tol, max_its=250):
#
#  Gauss-Seidel iterative method to approximate the solution of a
#  linear system Ax=b up to a user defined tolerance
#
#  INPUT:
#    A   - n by n square, non-singular matrix
#    b   - n by 1 right hand side vector
#    x0  - n by 1 vector containing that initial guess for the iteration
#    tol - user set tolerance for the stopping condition in the iteration
#
#  OUTPUT:
#    x - n by 1 vector containing the iterative solution
#    k - number of iterations

#  get the system size
   n, _ = A.shape

#  Gauss-Seidel iteration which overwrites the current approximate solution
#  with the new approximate solution (pseudocode available in the lecture
#  notes on page 46)
   x = x0.copy()
   x_old = x0.copy()

   # max_its = 250 # maximum allowed iterations
   for k in range(max_its):
      for i in range(n):
         sum = 0
         for j in range(n):
            if j != i:
               sum += A[i, j] * x[j]
         x[i] = (b[i] - sum) / A[i, i]
      r = b - A @ x
      #if np.linalg.norm(r, 2) < tol * np.linalg.norm(b, 2):
      #   break
      if np.linalg.norm(x - x_old) < tol * np.linalg.norm(x):
         break
      x_old = x.copy()
   return x, k