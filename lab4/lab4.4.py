import numpy as np
from RungeKutta4 import RungeKutta4
from forwardEuler import forwardEuler
import matplotlib.pyplot as plt
from LorenzAttractor import LorenzAttractor


f = lambda t, y: 5 / t - 1 / t**2 - 5 * t * y**2
errors = []
error_ratios = []
eoc_values = []
error = 0
previous_error = None
for i in [0.2,0.1,0.05,0.025, 0.0125, 0.00625]:
    t, y = RungeKutta4(f=f, t0 =1, tn=25, y0=1, h=i)
    error = float(abs(0.04-y[-1]))
    errors.append(error)
    if previous_error is not None:
        error_ratio = previous_error / error
        error_ratios.append(error_ratio)
        eoc_value = np.log(previous_error / error) / np.log(2)
        eoc_values.append(float(eoc_value))
    else:
        error_ratios.append(None)
    previous_error = error
print("Errors: ", errors)
print("Error Ratios: ", error_ratios)
print("EOC Values: ", eoc_values)

plt.figure(figsize=(10, 6))
for i in [0.4,0.25,0.1]:
    t_rk, y_rk = RungeKutta4(f=f, t0 =1, tn=25, y0=1, h=i)
    t_fe, y_fe = forwardEuler(f=f, t0 =1, tn=25, y0=1, h=i)

    print(f"forward: {y_fe[-1]:e}")
    print(f"runge: {y_rk[-1]:e}")

    plt.plot(t_rk, y_rk, label=f'RK4 (h={i})')
    plt.plot(t_fe, y_fe, '--', label=f'Forward Euler (h={i})')

    plt.xlabel('t', fontsize=12)
    plt.ylabel('y(t)', fontsize=12)
    plt.title('Comparison of Runge-Kutta 4 and Forward Euler Methods', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()



LorenzAttractor(50)

    