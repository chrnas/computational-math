import numpy as np
import matplotlib.pyplot as plt
import time
from new_thomas import thomas

def test(N):
    main = N * np.ones(N) + np.random.rand(N)
    sub = np.random.rand(N - 1)
    super = np.random.rand(N - 1)
    # use the ’np.diag’ command to create tridiagonal matrix
    A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)
    known_x = np.pi * np.ones(N) # create known solution vector filled with pi
    manuf_b = A @ known_x # manufacture the right-hand-side
    return A,manuf_b, known_x

# Verify thomas algorithm
A_test = np.array([[1,2,0],[1,2,3],[0,2,3]])
d_test = np.array([1,1,1])

A, d, known_x = test(7)

x_thomas = thomas(A, d)

# Print results
print("Correct solution:", known_x)
print("Solution thomas:", x_thomas)
print("Error:", np.abs(known_x-x_thomas))
print("Relative error:", np.abs(known_x-x_thomas)/np.abs(known_x))

# Plot execution times
times = []
Ns = np.arange(5, 300, 5)
for i in Ns:
    A, d, known_x = test(i)
    t1 = time.perf_counter()
    x = thomas(A,d)
    delta_t = (time.perf_counter() - t1)
    times.append(delta_t)

plt.plot(Ns, times)
plt.xlabel('N', fontsize=12)
plt.ylabel('times', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
