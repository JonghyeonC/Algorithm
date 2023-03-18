import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
basket = [0] * N

for _ in range(M):
    a, b, k = map(int, sys.stdin.readline().rstrip().split())

    for i in range(a - 1, b - 1 + 1):
        basket[i] = k

print(*basket)