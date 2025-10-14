import numpy as np
import matplotlib.pyplot as plt

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