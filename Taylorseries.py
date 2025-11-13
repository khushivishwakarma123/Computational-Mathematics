# Taylor Series Method (order-5) - clean version (no stray dots)
# NOTE: This example uses a toy ODE where we supply derivatives manually.
# ODE: dy/dx = x^2 - y
# For demonstration we will compute derivatives at x0 by hand-like formulas.

def f(x, y):
    return x**2 - y

# compute derivatives at (x0,y0) up to order 5 for this particular ODE
def derivatives_at(x0, y0):
    # y' = x^2 - y
    y1 = f(x0, y0)
    # y'' = d/dx(x^2 - y) = 2x - y'   (since dy/dx = y')
    y2 = 2*x0 - y1
    # y''' = d/dx(y'') = 2 - y''   (since derivative of -y' is -y'')
    y3 = 2 - y2
    # y^(4) = d/dx(y''') = - y'''  (because derivative of -y'' is -y''')
    y4 = -y3
    # y^(5) = d/dx(y^(4)) = - y^(4)
    y5 = -y4
    return [y0, y1, y2, y3, y4, y5]

def taylor_step(x0, y0, h, order=5):
    derivs = derivatives_at(x0, y0)
    # Taylor series up to given order (0..5)
    y_next = derivs[0]
    factorial = 1
    for k in range(1, order+1):
        factorial *= k
        y_next += (h**k / factorial) * derivs[k]
    return y_next, derivs

if __name__ == "__main__":
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    order = 5

    print("="*70)
    y1, derivs = taylor_step(x0, y0, h, order)

    print(f"Derivatives at x0 = {x0}, y0 = {y0}:")
    print(f" y(0)     = {derivs[0]:.6f}")
    print(f" y'(0)    = {derivs[1]:.6f}")
    print(f" y''(0)   = {derivs[2]:.6f}")
    print(f" y'''(0)  = {derivs[3]:.6f}")
    print(f" y^(4)(0) = {derivs[4]:.6f}")
    print(f" y^(5)(0) = {derivs[5]:.6f}")
    print()
    print(f"Taylor approximation up to order {order}:")
    print(f" y({x0+h}) ≈ {y1:.10f}")
    print(f"Rounded to 4 decimal places: {y1:.4f}")
