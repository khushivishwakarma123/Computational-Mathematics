import math

# Function evaluator
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

# Regula Falsi (False Position) Method
def regula_falsi(func_str, a, b, tol):
    if f(a, func_str) * f(b, func_str) > 0:
        print("Invalid interval! f(a) and f(b) must have opposite signs.")
        return
    
    print("\nIter\t a\t b\t Xr\t f(Xr)")
    iter = 1
    Xr_old = a

    while True:
        # Formula for Regula Falsi
        Xr = (a * f(b, func_str) - b * f(a, func_str)) / (f(b, func_str) - f(a, func_str))
        fx = f(Xr, func_str)

        print(f"{iter}\t {a:.3f}\t {b:.3f}\t {Xr:.3f}\t {fx:.3f}")
        
        if abs(fx) < tol or abs(Xr - Xr_old) < tol:
            break

        if f(a, func_str) * fx < 0:
            b = Xr
        else:
            a = Xr

        Xr_old = Xr
        iter += 1

    print(f"\nApproximate root = {Xr:.3f} (correct to 3 decimal places)")

# === Main Program ===
print("=== Regula Falsi Method ===")
func_str = input("Enter the function f(x): ")     # Example: x**3 - 2*x - 5
a = float(input("Enter starting value a: "))      # Example: 2
b = float(input("Enter ending value b: "))        # Example: 3
tol = 0.0001                                      # Accuracy

regula_falsi(func_str, a, b, tol)
