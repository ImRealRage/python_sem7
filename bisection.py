def bisection_method(f, a, b, tol=1e-7, max_iter=1000):
    """
    f: function
    a: lower bound
    b: upper bound
    tol: tolerance
    max_iter: maximum number of iterations
    Returns the root of the function within the given tolerance and maximum number of iterations.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("Root must exist within the given interval.")

    c = (a + b) / 2.0

    iter = 0

    while abs(f(c)) > tol and iter < max_iter:
        iter += 1
        c = (a + b) / 2.0

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iter


def function(x):
    return x**3 - x - 1


root, iter = bisection_method(function, 1, 2)
print(f"The root is: {root} and the number of iterations is: {iter}")
