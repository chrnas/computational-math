import matplotlib.pyplot as plt
import numpy as np

def two_point2(a,b, N):
    h = (b-a)/N
    below_diag = lambda x : 1/h**2 - 4/(2*x*h )
    above_diag = lambda x : 1/h**2 + 4/(2*x*h )
    main_diag = lambda x : 2*(1/x**2 - 1/h**2)

    s = lambda x : 2*np.log(x)/x**2

    y1 = 1/2
    yN = np.log(2)
    y_exact_func = lambda x: 4 / x - 2 / x**2 + np.log(x) - 3 / 2

    y = np.zeros(N)

    A = np.zeros((N,N))

    A[0,0] = main_diag(a)
    A[0,1] = below_diag(a)
    
    rhs = np.zeros(N)
    y[0] = y1
    
    for i in range(1,N-1):
        xi = a + i*h
        A[i,i-1] = below_diag(xi)
        A[i,i] = main_diag(xi)
        A[i,i+1] = above_diag(xi)

        rhs[i] = s(xi)
        y[i] = y_exact_func(xi)
        
    A[N-1][N-1] = main_diag(b)
    A[N-1][N-2] = above_diag(b)
    y[N-1] = yN

    rhs[0] = s(a) + above_diag(a)*y1
    rhs[N-1] = s(b) + below_diag(b)*yN
    return A, rhs, y