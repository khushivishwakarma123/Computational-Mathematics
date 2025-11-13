# Transportation Problem using Northwest Corner Method

costs = [
    [8, 6, 10],   # from O1 to D1, D2, D3
    [10, 4, 9]    # from O2 to D1, D2, D3
]

supply = [2000, 2500]         # supply for O1, O2
demand = [1500, 2000, 1000]   # demand for D1, D2, D3

alloc = [[0]*3 for _ in range(2)]  # allocation matrix

i = j = 0
while i < 2 and j < 3:
    qty = min(supply[i], demand[j])
    alloc[i][j] = qty
    supply[i] -= qty
    demand[j] -= qty
    if supply[i] == 0 and demand[j] == 0:
        i += 1
        j += 1
    elif supply[i] == 0:
        i += 1
    elif demand[j] == 0:
        j += 1

# Print results
print("Allocation Matrix (O1,O2 vs D1,D2,D3):")
for row in alloc:
    print(row)

total = 0
print("\nAllocations & Costs:")
for i in range(2):
    for j in range(3):
        if alloc[i][j] > 0:
            cost = alloc[i][j] * costs[i][j]
            total += cost
            print(f"O{i+1}->D{j+1}: {alloc[i][j]} units × {costs[i][j]} = {cost}")

print("\nTotal Transportation Cost =", total)
