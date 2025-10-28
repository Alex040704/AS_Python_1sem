import math

n = int(input())
x = float(input())
total = 0
for k in range(0, n + 1):
    total += ((-1) ** k) * (x ** (2 * k + 1)) / (2 * k + 1)
print(total)
