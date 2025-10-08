import numpy as np

def thomas_algorithm(A, b):
    pass

if __name__ == "__main__":
    N = 5
    # create three random vectors
    main = N * np.ones((N,)) + np.random.rand((N,))
    sub = np.random.rand((N - 1,))
    super = np.random.rand((N - 1,))
    # use the ’np.diag’ command to create tridiagonal matrix
    A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)

    known_x = np.pi * np.ones((N,)) # create known solution vector filled with pi
    manuf_b = A @ known_x # manufacture the right-hand-side

    solution = thomas_algorithm(A, manuf_b)