import numpy as np

def RungeKutta4(f, t0, tn, y0, h):
#
#  get the size of the problem and allocate memory
   t = np.arange(t0, tn + h, h)
   y = np.zeros((len(t),))

#  save the initial values
   y[0] = y0
   t[0] = t0

#  use forward Euler with the given time step h to solve the problem and
#  save the information for later analysis
   
   for j in range(1,len(t)):
#  this is an explicit method so we always use values from the past solution history
      k1 =f(t[j-1], y[j-1])
      k2 = f(t[j-1]+h/2, y[j-1]+k1*(h/2))
      k3 = f(t[j-1]+h/2, y[j-1]+k2*(h/2))
      k4 = f(t[j-1]+h, y[j-1]+h*k3)
      
      y[j]=y[j-1] + (h/6)*(k1 + 2*k2 + 2*k3 +k4)

   return t, y