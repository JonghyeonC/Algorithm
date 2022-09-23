def dfs(i, j, result):
    global cnt
    if len(result) == 7:
        if result not in answer:
            answer.append(result)
            return
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                dfs(ni, nj, result + str(arr[ni][nj]))


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    answer = []
    for i in range(N):
        for j in range(N):
            dfs(i, j, str(arr[i][j]))
    print(f'#{tc} {len(answer)}')