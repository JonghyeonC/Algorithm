def bfs(x, y):
    global N, end_x, end_y
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        if x == end_x and y == end_y:
            return visited[x][y] - 1
        else:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [1, -1, -2, -2, -1, 1, 2, 2]
T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        print(bfs(start_x, start_y))
