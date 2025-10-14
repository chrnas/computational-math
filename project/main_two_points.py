import numpy as np
import matplotlib.pyplot as plt
from thomas import thomas
from two_point import two_point2

a = 1
b = 2
N = 20

ratios=[]
Ns = [5,10, 20,25, 30,35, 40, 50, 60, 70, 80]
temp = None
for i in Ns:
    A, rhs, y_exact = two_point2(a, b, i)
    print(thomas(A,rhs))
    print(y_exact)
    
    inf_norm = np.linalg.norm(thomas(A,rhs)-y_exact, ord=np.inf)
    print("inf norm", inf_norm, i)
    if temp == None:
        ratios.append(None)
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