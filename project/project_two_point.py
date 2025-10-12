import numpy as np
from project_thomas import thomas


def two_point(a,b, N):
    h = (b-a)/N
    y_min = lambda x : 1 - 2*h/x 
    y_plus = lambda x : 1 + 2*h/x
    s = lambda x : -h**2*( 8/(x**3) - 4/(x**4) + 2*np.log(x)/(x**2) - 6/(2*x**2))

    y_exact_func = lambda x: 4 / x - 2 / x**2 + np.log(x) - 3 / 2
    y = np.zeros(N)
    A = np.zeros((N,N))
    A[0][0] = -2
    A[0][1] = y_plus(a)
    
    S = np.zeros(N)
    y[0] = y_exact_func(a)
    S[0] = s(a)*1/2 # change expression here
    index = 0
    for i in range(1,N-1):
        xi = a + i*h
        A[i][index] = y_min(xi)
        A[i][index+1] = -2
        A[i][index+2] = y_plus(xi)
        index +=1

        S[i] = s(xi)
        y[i] = y_exact_func(xi)
    A[N-1][N-1] = -2
    A[N-1][N-2] = y_min(b)
    y[N-1] = y_exact_func(b)
    S[N-1] = s(b) + np.log(2) # change expression here
    return A, S, y

a = 1
b = 2
N = 10

A, S, y_exact = two_point(a, b, N)
print(y_exact)
print(thomas(A,S))