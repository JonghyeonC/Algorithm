from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == G:
            return
        for k in dx:
            nx = x + k
            if 1 <= nx <= E and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1


E, S, G, U, D = map(int, input().split())
visited = [0] * (E + 1)
dx = [U, -D]
bfs(S)
if visited[G] == 0:
    print("use the stairs")
else:
    print(visited[G] - 1)