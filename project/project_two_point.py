import numpy as np
from project_thomas import thomas
import matplotlib.pyplot as plt

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
ratios=[]
Ns = [5,10, 20,25, 30,35, 40, 50, 60, 70, 80]
#Ns= [10,20,40,80]
temp = None
for i in Ns:
    A, rhs, y_exact = two_point2(a, b, i)
    #print(thomas(A,rhs))
    #print(y_exact)
    
    inf_norm = np.linalg.norm(thomas(A,rhs)-y_exact, ord=np.inf)
    print("inf norm", inf_norm, i)
    if temp == None:
        ratios.append(None) # append so we can plot this is does not mean anything
    else:
        error_ratio = temp/inf_norm
        ratios.append(error_ratio)
        print("ratio",error_ratio)
    temp = inf_norm


plt.plot(Ns, ratios)
plt.xlabel('N', fontsize=12)
plt.ylabel('error ratio', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()