# Simpson's 3/8 Rule for I = ∫(0 to 1) e^(-x^2) dx with n = 6
import math

# Define the function
def f(x):
    return math.exp(-x**2)

# Given limits
a = 0
b = 1
n = 6   # number of subintervals (must be a multiple of 3)

# Step size
h = (b - a) / n

# Compute x values
x = [a + i * h for i in range(n + 1)]

# Compute f(x) values
f_values = [f(xi) for xi in x]

# Display table
print("="*70)
print("Simpson’s 3/8 Rule for I = ∫(0 to 1) e^(-x^2) dx")
print("------------------------------------------------------")
print("i\t x(i)\t\t f(x(i)) = e^(-x^2)")
print("------------------------------------------------------")
for i in range(n + 1):
    print(f"{i}\t {x[i]:.4f}\t\t {f_values[i]:.6f}")
print("------------------------------------------------------")

# Apply Simpson's 3/8 Rule
sum_3 = sum(f_values[i] for i in range(1, n) if i % 3 != 0)
sum_2 = sum(f_values[i] for i in range(3, n, 3))
I = (3*h/8) * (f_values[0] + 3*sum_3 + 2*sum_2 + f_values[-1])

# Step-by-step explanation
print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
print("\nUsing Simpson’s 3/8 Rule:")
print("I = (3h/8) * [f(x0) + 3*(f(x1)+f(x2)+f(x4)+f(x5)+...) + 2*(f(x3)+f(x6)+...) + f(xn)]")
print(f"I = (3*{h}/8) * [{f_values[0]:.4f} + 3*({sum_3:.4f}) + 2*({sum_2:.4f}) + {f_values[-1]:.4f}]")

# Final result
print("------------------------------------------------------")
print(f"Approximate value of the integral I = {I:.6f}")
print("="*70)
