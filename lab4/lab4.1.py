from SimpsonsRule import SimpsonsRule

f = lambda x: 8*x**3 - 4*x**2 + 6*x - 3

# Interval [0,1]
S1, x1 = SimpsonsRule(0, 1, f, 2)
I1 = 2/3
error1 = abs(I1 - S1)

# Interval [-4,2]
S2, x2 = SimpsonsRule(-4, 2, f, 4)
I2 = -630
error2 = abs(I2 - S2)

print("Error [0,1]:", error1)
print("Error [-4,2]:", error2)