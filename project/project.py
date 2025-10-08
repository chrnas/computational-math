import numpy as np

import numpy as np

def thomas_algorithm(A, d):
    """
    Solves A x = d for tridiagonal A using the Thomas algorithm.

    Parameters
    ----------
    A : 2D array-like (X x X)
        Tridiagonal coefficient matrix.
    d : array-like
        Right-hand side vector.

    Returns
    -------
    x : np.ndarray
        Solution vector.
    """

    A = np.array(A, dtype=float)
    d = np.array(d, dtype=float)
    X = len(d)

    # Extract sub-, main-, and super-diagonals
    a = np.zeros(X)
    b = np.zeros(X)
    c = np.zeros(X)

    for i in range(X):
        b[i] = A[i, i]
        if i > 0:
            a[i] = A[i, i - 1]
        if i < X - 1:
            c[i] = A[i, i + 1]

    # Allocate scratch space
    scratch = np.zeros(X)

    # Forward sweep
    scratch[0] = c[0] / b[0]
    d[0] = d[0] / b[0]

    for ix in range(1, X):
        denom = b[ix] - a[ix] * scratch[ix - 1]
        if ix < X - 1:
            scratch[ix] = c[ix] / denom
        d[ix] = (d[ix] - a[ix] * d[ix - 1]) / denom

    # Back substitution
    for ix in range(X - 2, -1, -1):
        d[ix] -= scratch[ix] * d[ix + 1]

    return d



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

    d = thomas_algorithm(A, manuf_b)