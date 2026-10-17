"""Print a multiplication grid from 1 to N"""

n = int(input("Enter the value of N: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:3}", end=" ")
    print()