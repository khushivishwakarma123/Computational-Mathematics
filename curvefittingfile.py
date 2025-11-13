# Straight Line Fit using Least Squares (No numpy, no pandas)

def fit_line(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(i*i for i in x)
    sum_xy = sum(x[i]*y[i] for i in range(n))

    a1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    a0 = (sum_y - a1*sum_x) / n
    return a0, a1

def main():
    n = int(input("How many data points? "))
    x, y = [], []
    for i in range(n):
        xi, yi = map(float, input(f"Enter x and y for point {i+1}: ").split())
        x.append(xi)
        y.append(yi)

    a0, a1 = fit_line(x, y)
    print(f"\nEquation of line: y = {a0:.4f} + {a1:.4f}x")

    xv = float(input("Enter x value to predict y: "))
    yv = a0 + a1 * xv
    print(f"Predicted y = {yv:.4f}")

# Example
# x = [10, 2, 5, 7]
# y = [25, 12, 20, 30]
main()
