import numpy as np
import time 
def thomas(A, d):
    a = np.diag(A,-1)
    b = np.diag(A, 0)
    c = np.diag(A, 1)
    N = len(d) 
    c_prime = np.zeros(N)
    c_prime[0] = c[0]/b[0]

    d_prime = np.zeros(N)
    d_prime[0] = d[0]/b[0]
    
    for i in range(1,N):

        if i < N - 1: c_prime[i] = c[i] / (b[i] - a[i]*c_prime[i-1])
        d_prime[i] = (d[i] - a[i-1]*d_prime[i-1]) / (b[i] - a[i-1]*c_prime[i-1])
    
    x = np.zeros(N)
    x[N-1] = d_prime[N-1]
    for i in range(N-2,-1, -1):
        x[i] = d_prime[i] - c_prime[i]*x[i+1]
    return x

def test(N):
    main = N * np.ones(N) + np.random.rand(N)
    sub = np.random.rand(N - 1)
    super = np.random.rand(N - 1)
    # use the ’np.diag’ command to create tridiagonal matrix
    A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)
    known_x = np.pi * np.ones(N) # create known solution vector filled with pi
    manuf_b = A @ known_x # manufacture the right-hand-side
    return A,manuf_b


A_test = np.array([[1,2,0],[1,2,3],[0,2,3]])
d_test = np.array([1,1,1])

A, d = test(7)
#print(d)
#print( A @ thomas(A,d))
             


#TO-DO plot and time thomas for different sizes of matrices. This way we can see if time grows O(n) or exponetially or whatever