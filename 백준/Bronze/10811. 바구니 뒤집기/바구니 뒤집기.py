import sys


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr = arr[:a - 1] + arr[a-1:b][::-1] + arr[b:]
print(*arr)