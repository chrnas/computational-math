import numpy as np
import time 
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

def test(N):
    main = N * np.ones(N) + np.random.rand(N)
    sub = np.random.rand(N - 1)
    super = np.random.rand(N - 1)
    # use the ’np.diag’ command to create tridiagonal matrix
    A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)
    known_x = np.pi * np.ones(N) # create known solution vector filled with pi
    manuf_b = A @ known_x # manufacture the right-hand-side
    return A,manuf_b, known_x


A_test = np.array([[1,2,0],[1,2,3],[0,2,3]])
d_test = np.array([1,1,1])

A, d, known_x = test(7)

# Old check for correctness
#print(d)
#print( A @ thomas(A,d))

x_thomas = thomas(A, d)

print("Correct solution:", known_x)
print("Solution thomas:", x_thomas)
print("Error:", np.abs(known_x-x_thomas))
print("Relative error:", np.abs(known_x-x_thomas)/np.abs(known_x))

# "warm up" run, otherwise we get a tail on the plot not representative on the time it takes to execute thomas            
# A, d, known_x = test(4)
# x = thomas(A,d)

times = []
Ns =[5,10,15, 20,25,30, 35, 40]
for i in Ns:
    A, d, known_x = test(i)
    t1 = time.time_ns()
    x = thomas(A,d)
    delta_t = (time.time_ns() - t1)/10**9 #convert to seconds
    times.append(delta_t)
#print(times)
plt.plot(Ns, times)
plt.xlabel('N', fontsize=12)
plt.ylabel('times', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
