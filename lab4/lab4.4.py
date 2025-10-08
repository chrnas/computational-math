import numpy as np
from RungeKutta4 import RungeKutta4
from forwardEuler import forwardEuler
import matplotlib.pyplot as plt


f = lambda t, y: 5 / t - 1 / t**2 - 5 * t * y**2
temp = 0
for i in [0.2,0.1,0.05,0.025]:
    t, y = RungeKutta4(f=f, t0 =1, tn=25, y0=1, h=i)
    print(abs(0.04-y[25]))
    if temp == 0:
        temp = abs(0.04-y[25])
        continue
    else:
        temp = abs(0.04-y[25])/temp
        print("Error ratio ", temp)
        temp = abs(0.04-y[25])

plt.figure(figsize=(10, 6))
for i in [0.4,0.25,0.1]:
    t_rk, y_rk = RungeKutta4(f=f, t0 =1, tn=25, y0=1, h=i)
    t_fe, y_fe = forwardEuler(f=f, t0 =1, tn=25, y0=1, h=i)
    print("forward: ", y_fe[25])
    print("runge",y_rk[25])
    plt.plot(t_rk, y_rk, label=f'RK4 (h={i})')
    plt.plot(t_fe, y_fe, '--', label=f'Forward Euler (h={i})')

plt.xlabel('t', fontsize=12)
plt.ylabel('y(t)', fontsize=12)
plt.title('Comparison of Runge-Kutta 4 and Forward Euler Methods', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()

    