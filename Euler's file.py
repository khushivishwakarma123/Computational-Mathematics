# Euler's Method in Python

def f(x, y):
    return x + y    # Example differential equation: dy/dx = x + y

# main program
if __name__ == "__main__":
    x0 = 0.0     # initial x
    y0 = 1.0     # initial y
    h = 0.1      # step size
    n = 5        # number of steps

    print("="*70)
    print(f"{'Euler\'s Method Approximation':^70}")
    print("="*70)
    print(f"{'x':>8} {'y':>15}")

    for i in range(n):
        y1 = y0 + h * f(x0, y0)
        print(f"{x0:8.4f} {y0:15.6f}")
        x0 += h
        y0 = y1

    print(f"\nApproximate value of y({x0:.1f}) = {y0:.6f}")
