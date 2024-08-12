def secant_method(
    func, initial_guess1, initial_guess2, tolerance=1e-6, max_iterations=100
):
    previous_guess = initial_guess1
    current_guess = initial_guess2

    for iteration in range(max_iterations):
        previous_value = func(previous_guess)
        current_value = func(current_guess)

        if current_value == previous_value:
            raise ValueError("Division by zero encountered in the Secant method.")

        next_guess = current_guess - current_value * (
            current_guess - previous_guess
        ) / (current_value - previous_value)

        if abs(next_guess - current_guess) < tolerance:
            return (
                next_guess,
                iteration + 1,
            )

        previous_guess = current_guess
        current_guess = next_guess

    raise ValueError(
        "Secant method did not converge within the maximum number of iterations."
    )


# Example usage:
if __name__ == "__main__":

    def target_function(x):
        return x**3 + 6 * x**2 - 11 * x + 3

    # Initial guesses
    initial_guess1 = 1.0
    initial_guess2 = 3.0

    # Call the Secant method function
    root, iterations = secant_method(target_function, initial_guess1, initial_guess2)
    print("#########Secant method##########")

    print(f"Root found: {root}")
    print(f"Iterations: {iterations}")

    print("#########Secant method output ends##########")
