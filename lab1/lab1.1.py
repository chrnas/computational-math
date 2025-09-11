import numpy as np

# First attempt: x = 0 (will cause error and result nan)
try:
    x = 0
    expression_calculated = (np.cos(x) - 1) / (x ** 2)
    print(f"Result for x = 0: {expression_calculated:.4e}")
except Exception as e:
    print(f"An error occurred for x = 0: {e}")

# Second attempt: x = 1 (normal case)
try:
    x = 1
    expression_calculated = (np.cos(x) - 1) / (x ** 2)
    print(f"Result for x = 1: {expression_calculated:.4e}")
except Exception as e:
    print(f"An error occurred for x = 1: {e}")
