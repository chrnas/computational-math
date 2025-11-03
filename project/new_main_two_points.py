import numpy as np
import matplotlib.pyplot as plt
from new_thomas import thomas
from new_two_point import two_point2

a = 1
b = 2
y0 = 0.5
yn = np.log(2)

ratios=[]
errors = []
Ns = [10, 20, 40, 80]
temp = None
for i in Ns:
    A, rhs, y_exact = two_point2(a, b, i)
    y_int = thomas(A.copy(), rhs.copy())
    y_full = np.zeros(i+1)
    y_full[0] = y0
    y_full[-1] = yn
    y_full[1:-1] = y_int
    inf_norm = np.linalg.norm(y_full-y_exact, ord=np.inf)
    errors.append(float(inf_norm))
    if temp == None:
        ratios.append(None)
    else:
        error_ratio = temp/inf_norm
        ratios.append(float(error_ratio))
    temp = inf_norm

# Print results
print("Ns:", np.array(Ns))
print("Errors:", np.array(errors))
print("Ratios:", np.array(ratios))

# Plot error ratios
plt.plot(Ns, ratios)
plt.xlabel('N', fontsize=12)
plt.ylabel('error ratio', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()