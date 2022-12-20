from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == G:                                # 목표층에 도달했다면 리턴
            return
        for k in dx:                              # 위, 아래 중에 2개의 방향 중에 선택해서 이동
            nx = x + k
            if 1 <= nx <= E and visited[nx] == 0: # 층이 건물 안에 속하고 방문한 적이 없다면 방문
                q.append(nx)
                visited[nx] = visited[x] + 1      # 이동한 층에 지금까지 방문한 횟수를 저장


E, S, G, U, D = map(int, input().split())          # 최고층, 현재층, 목표층, 위로 갈수 있는 높이, 밑으로 갈 수 있는 높이
visited = [0] * (E + 1)                            # 최고층을 포함하는 방문처리 배열
dx = [U, -D]                                       # 위, 아래 이동가능한 2방향 탐색
bfs(S)                                             # 현재층에서 위, 아래 이동해서 목표층에 도달하면 되므로 bfs
if visited[G] == 0:                                # 목표층에 도달한 적이 없다면
    print("use the stairs")
else:                                              # 목표층에 도달했다면
    print(visited[G] - 1)                          # 현재층에서부터 1이 시작됐으므로 -1을 해준다.
