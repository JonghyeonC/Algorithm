from collections import deque


def bfs():
    while road:
        for _ in range(len(water)):
            x, y = water.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if arr[nx][ny] == ".":
                        arr[nx][ny] = "*"
                        water.append((nx, ny))

        for _ in range(len(road)):
            i, j = road.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < R and 0 <= nj < C:
                    if arr[ni][nj] == "D":
                        visited[ni][nj] = visited[i][j] + 1
                        return 1
                    if arr[ni][nj] == "." and visited[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1
                        road.append((ni, nj))
    return 0


water = deque()
road = deque()
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
a = b = c = d = 0
end_x, end_y = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "S":
            road.append((i, j))
        elif arr[i][j] == "*":
            water.append((i, j))
        elif arr[i][j] == "D":
            end_x = i
            end_y = j
result = bfs()
if result == 0:
    print("KAKTUS")
else:
    print(visited[end_x][end_y])