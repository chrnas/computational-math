import numpy as np

n = 5
h = 1/n
main_diag = -1*np.ones(n)
off_diag = np.ones(n - 1)
Dx = np.diag(main_diag) + np.diag(off_diag, 1) #+ np.diag(off_diag, -1)

#x = np

Dx = np.zeros((n + 1, n + 1))

# Forward difference at x_0
Dx[0, 0] = -1 / h
Dx[0, 1] = 1 / h

# Central differences for interior points
for i in range(1, n):
    Dx[i, i - 1] = -1 / (2 * h)
    Dx[i, i + 1] = 1 / (2 * h)

# Backward difference at x_n
Dx[n, n - 1] = -1 / h
Dx[n, n] = 1 / h

f_1 = np.ones(n+1)
f_x = np.array([i for i in range(n+1)])
f_x2 = np.array([i**2 for i in range(n+1)])
print(f_1)
print(f_x)
print(f_x2)

f_prime = Dx @ f_x2
print(f_prime)
