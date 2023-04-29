import sys
input = sys.stdin.readline


N, M = map(int, input().split())
name = {}
idx = {}
for i in range(1, N + 1):
    tmp = input().rstrip()
    name[tmp] = i
    idx[i] = tmp
for _ in range(M):
    order = input().rstrip()
    if order.isnumeric():
        print(idx[int(order)])
    else:
        print(name[order])