import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
basket = []

for a in range(n + 1):
    basket.append(0)

for b in range(0, m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for c in range(i, j + 1):
        basket[c] = k

for d in range(1, n + 1):
    print(basket[d], end=" ")