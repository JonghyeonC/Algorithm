R, C, W = map(int, input().split())

arr = [[0] * (R + W - 1) for _ in range(R + W - 1)]
arr[0][0] = 1
for i in range(1, R + W - 1):
    arr[i][0] = 1
    for j in range(1, i + 1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

ans = 0
for i in range(W):
    for j in range(i + 1):
        ans += arr[i + (R - 1)][j + (C - 1)]

print(ans)