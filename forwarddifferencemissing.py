def solve_missing_term(y):
    # Coefficients for 5-point formula: y4 - 4y3 + 6y2 - 4y1 + y0 = 0
    coeffs = [1, -4, 6, -4, 1]

    if y.count(None) != 1:
        print("Error: Exactly one value must be 'null'.")
        return None

    m = y.index(None)
    total = 0
    for i in range(5):
        if i != m:
            total += coeffs[i] * y[i]

    y_missing = -total / coeffs[m]
    return m, y_missing


def check_equal_spacing(x):
    h = x[1] - x[0]
    for i in range(len(x) - 1):
        if abs((x[i + 1] - x[i]) - h) > 1e-6:
            return False
    return True


def main():
    print("=================================================")
    print("Enter  x values (must be equally spaced):")
    x = [float(input(f"x[{i}]: ")) for i in range(5)]

    if not check_equal_spacing(x):
        print("Error: x values are not equally spaced.")
        return

    print("Enter  y values (use 'null' for the missing one):")
    y = []
    for i in range(5):
        val = input(f"y[{i}]: ").strip().lower()
        if val == "null":
            y.append(None)
        else:
            y.append(float(val))

    result = solve_missing_term(y)
    if result:
        idx, y_miss = result
        print(f"\nEstimated missing y[{idx}] (at x = {x[idx]:.1f}) = {y_miss:.4f}")
    print("=================================================")


if __name__ == "__main__":
    main()
