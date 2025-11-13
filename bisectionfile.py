import math

# Function evaluator
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

# Bisection Method
def bisection(func_str, a, b, tol):
    if f(a, func_str) * f(b, func_str) > 0:
        print("Invalid interval! f(a) and f(b) must have opposite signs.")
        return
    
    print("\nIter\t a\t b\t Xr\t f(Xr)")
    iter = 1
    
    while (b - a) / 2 > tol:
        Xr = (a + b) / 2
        fx = f(Xr, func_str)
        print(f"{iter}\t {a:.3f}\t {b:.3f}\t {Xr:.3f}\t {fx:.3f}")
        
        if abs(fx) < tol:
            break
        
        if f(a, func_str) * fx < 0:
            b = Xr
        else:
            a = Xr
        
        iter += 1
    
    print(f"\nApproximate root = {Xr:.3f} (correct to 3 decimal places)")

# === Main Program ===
print("=== Bisection Method ===")
func_str = input("Enter the function f(x): ")     # Example: x**3 - 4*x + 1
a = float(input("Enter starting value a: "))      # Example: 0
b = float(input("Enter ending value b: "))        # Example: 1
tol = 0.0001                                      # Accuracy

bisection(func_str, a, b, tol)
