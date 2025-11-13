# Runge-Kutta 4th Order Method (Step-by-Step)
import math

# Differential equation dy/dx = x + y
def f(x, y):
    return x + y

# Exact solution for checking (for dy/dx = x + y, y(0)=1 → y = 2e^x - x - 1)
def exact_solution(x):
    return 2 * math.exp(x) - x - 1

# Initial conditions
x = 0.0
y = 1.0
h = 0.1
steps = int(0.2 / h)   # compute up to x = 0.2

print("====================================================================")
print("         Runge-Kutta 4th order (RK4) step-by-step")
print("====================================================================")
print("Equation: y' = x + y , y(0)=1\n")

print(f"{'Step':>3} | {'x_n':>6} | {'y_n (before)':>16} | {'k1':>7} | {'k2':>7} | {'k3':>7} | {'k4':>7} | {'y_(n+1)':>10}")
print("-"*75)

for i in range(1, steps + 1):
    k1 = f(x, y)
    k2 = f(x + h/2, y + (h/2)*k1)
    k3 = f(x + h/2, y + (h/2)*k2)
    k4 = f(x + h, y + h*k3)

    increment = (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    y_next = y + increment

    print(f"{i:3d} | {x:6.3f} | {y:16.9f} | {k1:7.6f} | {k2:7.6f} | {k3:7.6f} | {k4:7.6f} | {y_next:10.9f}")

    # update for next iteration
    x += h
    y = y_next

print("-"*75)
print(f"Final RK4 approximation: y({x:.3f}) = {y:.9f}")
print(f"Exact value             : y({x:.3f}) = {exact_solution(x):.9f}")
print(f"Absolute error          : {abs(y - exact_solution(x)):.12e}")
