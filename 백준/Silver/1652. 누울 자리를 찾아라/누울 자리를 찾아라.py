N = int(input())
arr = [list(input()) for _ in range(N)]
hori = 0
verti = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == "X":
            if cnt >= 2:
                hori += 1
            cnt = 0
        else:
            cnt += 1
    if cnt >= 2:
        hori += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[j][i] == "X":
            if cnt >= 2:
                verti += 1
            cnt = 0
        else:
            cnt += 1
    if cnt >= 2:
        verti += 1
print(hori, verti)