import numpy as np
import math

# Define range of n
n = np.arange(1, 13)

# Calculate Stirling approximations
stirling_approx = np.sqrt(2 * np.pi * n) * (n / np.e) ** n

# Print Stirling approximations
print("Stirling approximations:")
for i, val in enumerate(stirling_approx, start=1):
    print(f'S{i}: {val:.4e}')

# Calculate exact values
exact_values = np.array([math.factorial(x) for x in n])

# Print exact values
print("\nExact values:")
for i, val in enumerate(exact_values, start=1):
    print(f'E{i}: {val:.4e}')

# Calculate absolute errors
absolute_errors = np.abs(exact_values - stirling_approx)

# Print absolute errors
print("\nAbsolute errors:")
for i, val in enumerate(absolute_errors, start=1):
    print(f'AbsErr{i}: {val:.4e}')

# Calculate relative errors
relative_errors = absolute_errors / exact_values

# Print relative errors
print("\nRelative errors:")
for i, val in enumerate(relative_errors, start=1):
    print(f'RelErr{i}: {val:.4e}')

