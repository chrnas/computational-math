import numpy as np

A = np.array([[0.913, 0.659], [0.457, 0.33]])
b = np.array([0.254, 0.127])

# Verify solution
x_exact = np.array([1, -1])

# print exact solution
print("Exact solution: ", x_exact)

# Verify exact solution
print("Solution should be [0,0]:\n")
print(A @ x_exact - b)

# Solve 
x_num = np.linalg.solve(A, b)

# Print result
np.set_printoptions(precision=16, suppress=False)
print("\nNumerical solution: ", x_num)

# calculate perturbations
b_hat = np.array([0.2539949, 0.1272061])
b_tilde = np.array([0.252428, 0.126213])

print("perturbations:")
print("b_hat:", b_hat)
print("b_tilde:", b_tilde)

# solve perturbations
x_hat = np.linalg.solve(A, b_hat)
x_tilde = np.linalg.solve(A, b_tilde)

# Print results
print("\nx_hat: ", x_hat)
print("\nx_tilde: ", x_tilde)

# Calculate residual
r_hat = b_hat - A @ x_hat
r_tilde = b_tilde - A @ x_tilde

# Print residuals
print("\nResiduals:")
print("r_hat:", r_hat)
print("r_tilde:", r_tilde)

# normalize residuals
r_hat = np.linalg.norm(r_hat, ord=1)
r_tilde = np.linalg.norm(r_tilde, ord=1)

print("\nNormalized residuals:")
print("r_hat:", r_hat)
print("r_tilde:", r_tilde)

# calculate condition number
cond_A = np.linalg.cond(A, p=1)

# Print condition number
print("\nCondition number:", cond_A)