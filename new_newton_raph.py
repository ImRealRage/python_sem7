def newton_raphson(f, df, x0, tol=1e-1000, max_itr=10000000000):
    """
    f: function
    df: derivative
    x0: initial guess
    tol: tolerance
    max_iter: maximum number of iterations
    Returns the root of the function within the given tolerance and maximum number of iterations.
    Raises a ValueError if the root is not found within the given tolerance and maximum number of iterations.
    """
    x_n = x0
    itr = 0

    for _ in range(max_itr):
        itr += 1
        f_xn = f(x_n)
        df_xn = df(x_n)

        if df_xn == 0:
            raise ValueError("No roots found")

        x_next = x_n - (f_xn / df_xn)
        if abs(x_next - x_n) < tol:
            return x_next, itr
        x_n = x_next

    raise ValueError("All iternations completed, root not yet found")


def function(x):
    return x**3 - 4 * x - 9


def derivative(x):
    return 3 * x**2 - 4


root, itr = newton_raphson(function, derivative, 3)

print(f"Approximate root: {root}")
print(f"Number of iterations: {itr}")
