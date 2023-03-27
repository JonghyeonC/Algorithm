H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
for line in arr:
    cnt = 0
    flag = 0
    for i in range(W):
        if line[i] == "c":
            cnt = 1
            flag = 1
        elif line[i] == "." and flag == 1:
            line[i] = cnt
            cnt += 1
for i in range(H):
    for j in range(W):
        if arr[i][j] == "c":
            arr[i][j] = 0
        elif arr[i][j] == ".":
            arr[i][j] = -1

for line in arr:
    print(*line)