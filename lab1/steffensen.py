import numpy as np

def steffensen(f, x0, tol):
##
#  Implementation of the steffensen method to approximate
#  the root of a nonlinear function f(x)
#
#  INPUT:
#    f      - function f(x)                         OBS! passed as a lambda function
#    fprime - first derivative of the function f(x) OBS! passed as a lambda function
#    x0     - initial guess of the root location
#    tol    - error tolerance to stop the iteration
#
#  OUTPUT:
#    xVals  - sequence of approximate values for the root of the function f(x)
#    iter   - number of iterations it took to achieve user set tolerance

#  Set the maximum iteration count `max_its` and initialize a vector `xVals` to store the sequence of guesses
   max_its = 15
   xVals = np.zeros(max_its + 1)

#  save the initial guess
   xVals[0] = x0

#  perform steffensen method for a fixed number of iterations
   for k in range(max_its):

#  update to the next value
      xVals[k+1] = xVals[k] - (f(xVals[k])**2 / (f(xVals[k]+f(xVals[k])) - f(xVals[k])))

# check the stopping condition
      stopCond = abs(f(xVals[k+1]))
      if stopCond < tol:
         xVals = xVals[0:k+2]
         iter  = k+2
         break

   return xVals, iter