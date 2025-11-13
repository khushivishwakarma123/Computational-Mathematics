import math

# Function evaluator
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

# Derivative calculator using small h
def derivative(x, func_str):
    h = 1e-5
    return (f(x + h, func_str) - f(x - h, func_str)) / (2 * h)

# Newton–Raphson Method
def newton_raphson(func_str, x0, tol):
    print("\nIter\t x\t\t f(x)\t\t f'(x)\t\t Next x")
    iter = 1

    while True:
        fx = f(x0, func_str)
        dfx = derivative(x0, func_str)
        
        if dfx == 0:
            print("Error: Derivative is zero. Method fails.")
            return
        
        x1 = x0 - fx / dfx
        print(f"{iter}\t {x0:.5f}\t {fx:.5f}\t {dfx:.5f}\t {x1:.5f}")

        if abs(x1 - x0) < tol:
            break
        
        x0 = x1
        iter += 1

    print(f"\nApproximate root = {x1:.3f} (correct to 3 decimal places)")

# === Main Program ===
print("=== Newton–Raphson Method ===")
func_str = input("Enter the function f(x): ")      # Example: x**3 - 2*x - 5
x0 = float(input("Enter the initial guess: "))     # Example: 2
tol = 0.0001                                       # Accuracy

newton_raphson(func_str, x0, tol)
