import numpy as np

def Lagrange_interpolation(z, data_points):
#
#  Implementation to evaluate an interpolating polynomial p_n(x)
#  at the point x = z. The polynomial uses the standard Lagrange
#  basis functions.
#
#  INPUT:
#
#     z    - 1x1 value to evaluate
#     data_points - list of (x, y) points
#
#  OUTPUT:
#
#     pnx - value of the polynomial interpolant at x = z
#

#  Compute the polynomial interpolation sum evaluated at x = z
   pnx = 0 
   n = len(data_points)
   for i in range(n):
      temp = 1
      for j in range(n):
         if i == j:
            continue
         temp = temp * (z - data_points[j][0]) / (data_points[i][0]-data_points[j][0])
         #print(temp)




      pnx += data_points[i][1]*temp

   return pnx