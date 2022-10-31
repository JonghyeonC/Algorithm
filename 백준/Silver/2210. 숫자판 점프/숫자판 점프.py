def dfs(i, j, temp):
    temp += arr[i][j]
    if len(temp) == 6:
        ans.add(temp)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                dfs(ni, nj, temp)


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
arr = [list(input().split()) for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, '')
print(len(ans))