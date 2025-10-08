import numpy as np

def SimpsonsRule(a, b, f, n):
#
#   Implementation of the (possibly) composite Simpsons's quadrature
#   rule to approximate the definite integral
#
#            b
#           /\
#           |
#           | f(x) dx
#           |
#          \/
#          a
#
#   INPUT:
#
#      a    - lower integration bound
#      b    - upper integration bound
#      f    - integrand (input as a lambda function)
#      n    - number of intervals for the composite quadrature rule (must
#             be an even integer)
#
#   OUTPUT:
#
#      In - approximation to the definite integral of the function f(x)
#           on the given interval [a,b] using Simpson's rule
#      x  - set of nodes that define the sub-intervals

#  check is the number of intervals is even
   if n % 2 != 0:
      raise ValueError("The number of intervals n must be even!")

#  Find the interval spacing
   h = (b - a) / n

#  Build the set of uniformly spaced quadrature nodes
   x = np.linspace(a, b, n + 1)

#  Initialize In value to zero
   In = 0.0

#  Approximate the integral with composite Simpson's rule
   S = (h/3)*(f(a)+4*f((a+b)/2)+f(b))
   In = (h/3)*f(x[0])
   for i in range(1, n-1,2):
      In = In + (h / 3) * (4*f(x[i]) + 2 * f(x[i + 1]))
   In = In + (h/3)*(4*f(x[n-1])+f(x[n]))

   return In, x