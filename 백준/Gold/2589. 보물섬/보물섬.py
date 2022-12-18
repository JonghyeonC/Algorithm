# 각 육지에서 도달할 수 있는 다른 육지까지의 최장거리를 구하는 문제
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * L for _ in range(R)]   # 매 bfs문마다 방문처리 초기화가 필요하다.
    visited[i][j] = 1                       # 맨 초기값을 방문처리
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < L and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    temp = 0                                # 각 육지값에서 최대값을 구하기 위한 절차
    for x in range(R):
        for y in range(L):
            temp = max(temp, visited[x][y])
    return temp                             # 최장 거리를 return해준다

# 4방향 탐색
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
R, L = map(int, input().split())       # 세로, 가로
arr = [list(input()) for _ in range(R)]
cnt = 0                                 # bfs의 리턴 값 초기화
ans = 0                                 # 최장 거리를 나타내는 변수값 초기화
for i in range(R):
    for j in range(L):
        if arr[i][j] == 'L':            # 전체 행렬에서 육지인 경우는 모두 검사해야한다.
            cnt = bfs(i, j)             # bfs문에서 각 육지에서 도달할 수 있는 최장거리 값을 받는다.
        ans = max(ans, cnt - 1)         # 현재의 최장 거리와 방금 구한 최대거리 - 1(시작을 1로 했기때문에 1을 빼준다)중에 최대값을 찾는다.

print(ans)
