from SimpsonsRule import SimpsonsRule
from plot_composite_quad import plot_composite_quad
from adaptiveSimpson import adaptiveSimpson
import numpy as np



f = lambda x: (x + 1)**2 * np.cos((2 * x + 1) / (x - 3.3))
I_true = -1.564959809251273

I10, x10 =  SimpsonsRule(0,3, f,10)
#print(I10)
I20, x20 =  SimpsonsRule(0,3, f,20)
#print(I20)

plot_composite_quad(f, x20)
#print("Error",abs(I_true- S5))
#print("Error ratio", abs(I3- S3) / abs(I3- S4))
I_adapt, x_adapt = adaptiveSimpson(f, 0, 3, 1e-3)
print(I_adapt)
print(len(x_adapt))
print(abs(I_true - I_adapt))

plot_composite_quad(f,x_adapt)