# Simpson's 1/3 Rule for I = ∫(0 to 1) e^(-x^2) dx with n = 4
import math

# Define the function
def f(x):
    return math.exp(-x**2)

# Given limits
a = 0
b = 1
n = 4   # number of subintervals (must be even)

# Step size
h = (b - a) / n

# Compute x values
x = [a + i * h for i in range(n + 1)]

# Compute f(x) values
f_values = [f(xi) for xi in x]

# Display table
print("="*70)
print("Simpson’s 1/3 Rule for I = ∫(0 to 1) e^(-x^2) dx")
print("------------------------------------------------------")
print("i\t x(i)\t\t f(x(i)) = e^(-x^2)")
print("------------------------------------------------------")
for i in range(n + 1):
    print(f"{i}\t {x[i]:.4f}\t\t {f_values[i]:.6f}")
print("------------------------------------------------------")

# Apply Simpson's 1/3 Rule
I = (h/3) * (f_values[0] + f_values[-1] +
             4 * sum(f_values[i] for i in range(1, n, 2)) +
             2 * sum(f_values[i] for i in range(2, n-1, 2)))

# Step-by-step explanation
print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
print("\nUsing Simpson’s 1/3 Rule:")
print("I = (h/3) * [f(x0) + 4*(f(x1)+f(x3)+...) + 2*(f(x2)+f(x4)+...) + f(xn)]")
print(f"I = ({h}/3) * [{f_values[0]:.4f} + 4*{f_values[1]:.4f} + 2*{f_values[2]:.4f} + "
      f"4*{f_values[3]:.4f} + {f_values[4]:.4f}]")

# Final result
print("------------------------------------------------------")
print(f"Approximate value of the integral I = {I:.6f}")
print("="*70)
