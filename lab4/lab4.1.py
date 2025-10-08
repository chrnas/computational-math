from SimpsonsRule import SimpsonsRule
import numpy as np

f = lambda x: 8*x**3 - 4*x**2 + 6*x - 3
f2 = lambda x: np.sqrt(x)

# Interval [0,1]
S1, x1 = SimpsonsRule(0, 1, f, 2)
I1 = 2/3
error1 = abs(I1 - S1)

# Interval [-4,2]
S2, x2 = SimpsonsRule(-4, 2, f, 2)
I2 = -630

error2 = abs(I2 - S2)
S3, x3 = SimpsonsRule(0, 1, f2, 8)
I3 = (2/3)#*(2*np.sqrt(2)-1)
S4, x4 = SimpsonsRule(0, 1, f2, 16)

print("Error",abs(I3- S3))
print("Error",abs(I3- S4))
print("Error ratio", abs(I3- S3) / abs(I3- S4))
print("Error [0,1]:", error1)
print("Error [-4,2]:", error2)




