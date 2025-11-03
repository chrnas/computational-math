import matplotlib.pyplot as plt
import numpy as np

def two_point2(a,b, N):
    h = (b-a)/N
    m = N-1
    below_diag = lambda x : 1/h**2 - 4/(2*x*h )
    above_diag = lambda x : 1/h**2 + 4/(2*x*h )
    main_diag = lambda x : 2*(1/x**2 - 1/h**2)

    s = lambda x : 2*np.log(x)/x**2
    y_exact_func = lambda x: 4 / x - 2 / x**2 + np.log(x) - 3 / 2

    y1 = 1/2
    yN = np.log(2)

    y = np.zeros(N+1)
    A = np.zeros((N-1,N-1)) # Adjusted size for interior points
    rhs = np.zeros(N-1) # Adjusted size for interior points

    y[0] = y1

    for i in range(1,N):
        xi = a + i*h
        k = i - 1
        A[k, k] = main_diag(xi) # Main diagonal (main)
        if k > 0:
            A[k, k-1] = below_diag(xi) # Sub-diagonal (below)
        if k < (m-1):
            A[k, k+1] = above_diag(xi) # Super-diagonal (above)
        rhs[k] = s(xi)
        y[i] = y_exact_func(xi)

    y[-1] = yN

    # Apply boundary conditions to RHS
    rhs[0] -= below_diag(a + h*1)*y1  # Adjusted application logic for boundary conditions
    rhs[-1] -= above_diag(a + h * m)*yN # Adjusted application logic for boundary conditions

    return A, rhs, y