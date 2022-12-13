from collections import deque


def bfs(q):
    # q를 다 입력받았으므로 바로 while문에서 q를 pop한다.
    while q:
        z, i, j = q.popleft()
        for k in range(6):
            nz = z + dz[k]
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= nz < H and 0 <= ni < N and 0 <= nj < M and visited[nz][ni][nj] == 0 and arr[nz][ni][nj] == 0:
                arr[nz][ni][nj] = arr[z][i][j] + 1         # bfs의 특징처럼 한 차례 전체를 사방의 토마토를 다 훑으면 훑게 된 값을 전의 값보다 하나씩 동일하게 만들어준다. 동일한 날에 익은 토마토라는 것을 확인한다.
                q.append((nz, ni, nj))

# 3차원이므로 위아래앞뒤 방향 탐색
dz = [0, 0, 0, 0, -1, 1]
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # 3차원 배열 받을 때는 2차원배열에 차원 하나 더 추가
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque()          # 한번에 익은 토마토를 다 입력받아야 각 익은 토마토의 근처 토마토가 1개씩 익을 수 있다.

day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1 and visited[h][n][m] == 0:
                q.append((h, n, m))            # 익은 토마토를 아예 처음부터 다 q에 입력시킨다.
                visited[h][n][m] = 1

bfs(q)

# 만약에 bfs를 다 돌았음에도 익지 않은 토마토가 있다면 -1을 출력한다.
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                day = -1
# 토마토가 없으면 -1이라고 하므로 최대값을 -2로 초기화
max_value = -2
for h in range(H):
    for n in range(N):
        for m in range(M):
            max_value = max(arr[h][n][m], max_value)         # 토마토가 다 익었다고 했을 때 가장 큰 값이 익을 때까지 걸린 시간이므로 그 값에서 기존의 익은 토마토의 값인 1을 빼준다.

if max_value != 1 and day != -1:    # 최대값이 1이라면 애초부터 다 익은 토마토들만 있었으므로 패스하고 day가 -1인 것은 덜 익은 것이 있으므로 패스
    print(max_value - 1)
elif day == -1:                     # day가 -1이면 덜 익었다는 뜻으므로 -1을 출력하게 한다.
    print(-1)
elif max_value == 1:                # 최대값이 1이라면 애초에 다 익은 토마토들만 있었으므로 그냥 0을 출력시킨다.
    print(0)
