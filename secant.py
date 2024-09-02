def secant_method(function, x0, x1, tol=1e-7, max=100):
    """
    function: function
    x0: initial guess
    x1: next guess
    tol: tolerance
    max: maximum number of iterations
    Returns the root of the function within the given tolerance and maximum number of iterations.
    If the function does not converge within the maximum number of iterations, raises a ValueError.
    """
    iter = 0
    for _ in range(max):
        iter += 1
        f_x0 = function(x0)
        f_x1 = function(x1)

        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero encountered in the Secant method.")

        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2, iter

        x0 = x1
        x1 = x2

    raise ValueError(
        "Secant method did not converge within the maximum number of iterations."
    )


def function(x):
    return x**3 - x - 4


x0 = 1
x1 = 2

root, iter = secant_method(function, x0, x1)

print("Root found: ", root)
print("iter: ", iter)
