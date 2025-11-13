def fit_quadratic(x, y):
    n = len(x)

    # Required summations
    sum_x = sum(x)
    sum_x2 = sum(i**2 for i in x)
    sum_x3 = sum(i**3 for i in x)
    sum_x4 = sum(i**4 for i in x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2y = sum((x[i]**2) * y[i] for i in range(n))

    # Solving normal equations for a0, a1, a2
    # Using Cramer's rule / determinant method

    # Main determinant
    D = (n*(sum_x2*sum_x4 - sum_x3*sum_x3)
         - sum_x*(sum_x*sum_x4 - sum_x2*sum_x3)
         + sum_x2*(sum_x*sum_x3 - sum_x2*sum_x2))

    # Determinant for a0
    D0 = (sum_y*(sum_x2*sum_x4 - sum_x3*sum_x3)
          - sum_x*(sum_xy*sum_x4 - sum_x3*sum_x2y)
          + sum_x2*(sum_xy*sum_x3 - sum_x2*sum_x2y))

    # Determinant for a1
    D1 = (n*(sum_xy*sum_x4 - sum_x3*sum_x2y)
          - sum_y*(sum_x*sum_x4 - sum_x2*sum_x3)
          + sum_x2*(sum_x*sum_x2y - sum_xy*sum_x2))

    # Determinant for a2
    D2 = (n*(sum_x2*sum_x2y - sum_xy*sum_x3)
          - sum_x*(sum_x*sum_x2y - sum_xy*sum_x2)
          + sum_y*(sum_x*sum_x3 - sum_x2*sum_x2))

    a0 = D0 / D
    a1 = D1 / D
    a2 = D2 / D

    return a0, a1, a2


def main():
    n = int(input("How many data points? "))
    x, y = [], []
    for i in range(n):
        xi, yi = map(float, input(f"Enter x and y for point {i+1}: ").split())
        x.append(xi)
        y.append(yi)

    a0, a1, a2 = fit_quadratic(x, y)
    print(f"\nQuadratic Equation: y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x^2")

    xv = float(input("Enter x value to predict y: "))
    yv = a0 + a1*xv + a2*(xv**2)
    print(f"Predicted y = {yv:.4f}")


# Run program
main()
