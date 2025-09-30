import numpy as np

n = 5
h = 1 / n
x = np.linspace(0, 1, n + 1)
m = n + 1

# Build Dx using diags only:
# central stencil on off-diagonals, with boundary fixes in the first/last entries
diag0 = np.zeros(m)
diag0[0]  = -1/h       # forward diff at x0
diag0[-1] =  1/h       # backward diff at xN

super1 = np.ones(m - 1) / (2*h)
super1[0] = 1/h        # forward diff coefficient

sub1 = -np.ones(m - 1) / (2*h)
sub1[-1] = -1/h        # backward diff coefficient

Dx = np.diag(diag0) + np.diag(super1, 1) + np.diag(sub1, -1)

# Tests
test_cases = [
    ("f(x) = 1",  lambda x: np.ones_like(x), lambda x: np.zeros_like(x)),
    ("f(x) = x",  lambda x: x,               lambda x: np.ones_like(x)),
    ("f(x) = x^2",lambda x: x**2,            lambda x: 2*x),
]

for name, f, df in test_cases:
    f_vec  = f(x)
    approx = Dx @ f_vec
    exact  = df(x)
    error  = np.abs(approx - exact)

    print(f"\n{name}")
    print("Approx: ", np.round(approx, 4))
    print("Exact:  ", np.round(exact, 4))
    print("Error:  ", np.round(error, 4))
