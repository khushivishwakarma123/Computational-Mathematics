# Modified Euler's Method (Heun's Method)

def f(x, y):
    return x + y   # Example: dy/dx = x + y

# main program
if __name__ == "__main__":
    x0 = 0.0     # initial x
    y0 = 1.0     # initial y
    h = 0.1      # step size
    n = 5        # number of steps

    print("="*70)
    print(f"{'Modified Euler’s Method Approximation':^70}")
    print("="*70)
    print(f"{'x':>8} {'y':>15}")

    for i in range(n):
        k1 = f(x0, y0)
        y_predict = y0 + h * k1              # Euler prediction
        k2 = f(x0 + h, y_predict)            # Corrector slope
        y1 = y0 + (h / 2) * (k1 + k2)        # Improved estimate

        print(f"{x0:8.4f} {y0:15.6f}")

        x0 += h
        y0 = y1

    print(f"\nApproximate value of y({x0:.1f}) = {y0:.6f}")
