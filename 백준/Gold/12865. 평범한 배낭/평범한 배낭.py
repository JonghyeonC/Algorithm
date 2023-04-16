import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [[0, 0]]
for _ in range(N):
    item.append(list(map(int, input().split())))
arr = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - item[i][0]] + item[i][1])
        else:
            arr[i][j] = arr[i - 1][j]
print(arr[N][K])