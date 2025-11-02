import numpy as np
from math import sin, cos, log
from newtonRaphson import newtonRaphson
from steffensen import steffensen

# Define functions
f = lambda x: 3 * x - cos(2 * np.pi * x)
fprime = lambda x: 3 + 2 * np.pi * sin(2 * np.pi * x)

# Define constants
x0 = 0.4
tol = 1e-9
x_star = 1/6

# Calculate newton raphson values
xVals, iter = newtonRaphson(f, fprime, x0, tol)

# Print number of iterations for newton raphson
print(f"Number of iterations for Newton-Raphson: {iter}")

# Print newton raphson values
print("\nNewton Raphson X values")
for k, x in enumerate(xVals):
    print(f'x{k+1}: {x:.4e}')

# Calculate function values
function_values = np.vectorize(f)(xVals)

# Print function values
print("\nFunction values:")
for k, x in enumerate(function_values):
    print(f'f(x{k+1}): {x:.4e}')

# Calculate absolute differences
absolute_differences = np.abs(xVals - x_star)

# Print absolute differences
print("\nAbsolute differences:")
for k, x in enumerate(absolute_differences):
    print(f'|x{k+1} - x*|: {x:.4e}')

# Calculate eoc values
eoc = [(log(abs(x_star-xVals[i]))/(log(abs(x_star-xVals[i-1])))) for i in range(1, len(xVals))]

# Print EOC values
print("\nEOC values:")
for i, eoc in enumerate(eoc, start=1):
    print(f"k:{i+1} = {eoc:.4e}")

# Calculate average EOC(Experimental order of Convergence)
average_eoc = np.mean(eoc)

# Print average EOC
print(f"\nAverage EOC = {average_eoc:.4e}")

# Define guesses for steffenson method
x1 = 0.4
tol = 1e-9

# Calculate steffenson values
xVals, iter = steffensen(f, x1, tol)

# print iterations
print(f"\nNumber of iterations for Steffensen: {iter}")

# Print steffensen values
print("\nSteffensen X values")
for k, x in enumerate(xVals):
    print(f'x{k+1}: {x:.4e}')

# Calculate function values for steffensen
function_values = np.vectorize(f)(xVals)

# Print function values
print("\nFunction values:")
for k, x in enumerate(function_values):
    print(f'f(x{k+1}): {x:.4e}')

# Calculate absolute differences
absolute_differences = np.abs(xVals - x_star)

# Print absolute differences
print("\nAbsolute differences:")
for k, x in enumerate(absolute_differences):
    print(f'|x{k+1} - x*|: {x:.4e}')

# Calculate eoc values
eoc = [(log(abs(x_star-xVals[i]))/(log(abs(x_star-xVals[i-1])))) for i in range(1, len(xVals))]

# Print EOC values
print("\nEOC values:")
for i, eoc in enumerate(eoc, start=1):
    print(f"k:{i+1} = {eoc:.4e}")

# Print average EOC
print(f"\nAverage EOC = {average_eoc:.4e}")
