import sys
from collections import deque


def bfs(q):
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 배열의 범위 안에 있고, 아직 익지 않은 토마토면서 방문한 적이 없다면 q에 추가 하고 방문처리해서 반복실행
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


di = [0, 1, 0, -1]                                                       # 4방향 탐색
dj = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   # 토마토 배열 입력 받음
visited = [[0] * M for _ in range(N)]                                    # 방문 배열 생성


q = deque()                                                              # 처음부터 존재하는 익은 토마토를 다 입력받음
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))                                             # 익은 토마모가 있다면 q에 추가
            visited[i][j] = 1                                            # 재방문을 방지하기 위해서 방문처리
bfs(q)                                                                   # 익은 토마토 배열을 가지고 bfs문 실행

ans = -2                                             # 존재하지 않는 부분은 -1로 두기때문에 최대값을 -2로 초기화하고 진행
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:                          # 토마토가 없는 부분은
            visited[i][j] = -1                       # 방문처리를 -1로 하면서 0인 값으로 나타내지 않게 할려고 한다

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] != 1:    # 방문하지도 않았으면서 토마토가 1이 아닌 것은 익은 토마토가
            ans = -1                                 # bfs를 돌면서 접촉할 수 없었단 뜻이므로 -1을 출력하기 위함

if ans != -1:                                        # 만약 익을 수가 없는 상황이 아니라면
    for i in range(N):
        for j in range(M):
            ans = max(ans, visited[i][j] - 1)        # 방문배열을 확인하면서 초기값이 1이었으므로 배열에서 1을 뺀 값과 현재 최대값을 비교
print(ans)                                           # 애초에 모두 익었으면, 방문배열이 0이었을것으므로 굳이 신경 쓰지 않는다
