from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1


# 4방향 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())      # 가로길이, 세로길이, 배추 심은 장소의 갯수
    arr = [[0] * M for _ in range(N)]        # 인접 행렬 초기화
    visited = [[0] * M for _ in range(N)]    # 방문 초기화
    cnt = 0                                  # 지렁이 갯수 초기화
    for _ in range(K):                       
        y, x = map(int, input().split())     # 인접 행렬 값 채우기
        arr[x][y] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:   # 배추가 존재하고 방문하지 않았다면 bfs함수로
                bfs(i, j)
                cnt += 1                                # 연결된 배추의 갯수가 하나의 지렁이 갯수를 의미하므로 매번 bfs함수에 들어갈 때마다 지렁이 갯수 증가시킴
    print(cnt)