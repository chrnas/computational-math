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
    y[0] = 1/2
    S[0] = s(a) + y_min(a)*1/2 
    index = 0
    for i in range(1,N-1):
        xi = a + i*h
        A[i,i-1] = y_min(xi)
        A[i,i] = -2
        A[i,i+1] = y_plus(xi)
        index +=1

        S[i] = s(xi)
        y[i] = y_exact_func(xi)
    A[N-1][N-1] = -2
    A[N-1][N-2] = y_min(b)
    y[N-1] = np.log(2)
    S[N-1] = s(b) + y_plus(b)*np.log(2) 
    return A, S, y

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
a = 1
b = 2
N = 20

#print(y_exact)
#print(thomas(A,S))
temp = None
for i in [5, 10, 20, 40, 80]:
    A, rhs, y_exact = two_point2(a, b, i)
    print(thomas(A,rhs))
    print(y_exact)
    break
    inf_norm = np.linalg.norm(thomas(A,rhs)-y_exact, ord=np.inf)
    print("inf norm", inf_norm, i)
    if temp != None:
        error_ratio = temp/inf_norm
        print("ratio",error_ratio)
    temp = inf_norm