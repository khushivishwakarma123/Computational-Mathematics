def backward_difference_table(x, y):
    n = len(y)
    diff_table = [y.copy()]

    for i in range(1, n):
        row = []
        for j in range(i, n):
            val = diff_table[i-1][j] - diff_table[i-1][j-1]
            row.append(val)
        diff_table.append(row)

    return diff_table

def display_table(x, diff_table):
    n = len(x)
    print("\nBackward Difference Table:")
    print("x\t" + "\t".join([f"∇^{i}y" for i in range(n)]))

    for i in range(n):
        row = [f"{x[i]:.2f}"]
        for order in range(n):
            idx = i - order
            if order < len(diff_table) and 0 <= idx < len(diff_table[order]):
                row.append(f"{diff_table[order][idx]:.2f}")
            else:
                row.append("")
        print("\t".join(row))

def main():
    n = int(input("Enter the number of data points: "))

    print("Enter x values (equally spaced):")
    x = []
    for i in range(n):
        try:
            val = float(input(f"x[{i}]: "))
            x.append(val)
        except ValueError:
            print("Invalid input for x.")
            return

    h = x[1] - x[0]
    if not all(abs(x[i+1] - x[i] - h) < 1e-5 for i in range(n-1)):
        print("Error: x values are not equally spaced.")
        return

    print("Enter corresponding y values:")
    y = []
    for i in range(n):
        try:
            val = float(input(f"y[{i}]: "))
            y.append(val)
        except ValueError:
            print("Invalid input for y.")
            return

    diff_table = backward_difference_table(x, y)
    display_table(x, diff_table)

if __name__ == "__main__":
    main()
