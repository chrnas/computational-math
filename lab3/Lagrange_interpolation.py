import numpy as np
import matplotlib.pyplot as plt
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


def build_Interpolation(datapoints, M):
    X = np.linspace(datapoints[0][0], datapoints[-1][0], M)
    L = np.zeros((M,))
    for k in range(M):
        L[k] = Lagrange_interpolation(X[k], datapoints)
    x_data = [p[0] for p in datapoints]
    y_data = [p[1] for p in datapoints]

    """plt.figure(figsize=(8, 6)) # 
    plt.plot(X, L, label='Lagrange Polynomial', color='blue') 
    plt.scatter(x_data, y_data, color='red', zorder=5, label='Data Points') 

    plt.title('Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True) 
    plt.legend() 


    plt.show()"""
    return X,L