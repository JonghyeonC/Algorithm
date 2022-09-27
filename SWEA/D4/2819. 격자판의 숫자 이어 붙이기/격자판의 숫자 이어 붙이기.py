def dfs(i, j, result, c):
    global cnt
    if c == 6:
        answer.add(result)
        return
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                dfs(ni, nj, result + arr[ni][nj], c + 1)


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T + 1):
    N = 4
    arr = [input().split() for _ in range(N)]
    cnt = 0
    answer = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j], 0)
    print(f'#{tc} {len(answer)}')