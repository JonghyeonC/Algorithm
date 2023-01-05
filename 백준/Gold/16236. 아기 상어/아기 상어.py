from collections import deque


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
now_x, now_y = 0, 0

# 상어의 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            now_x, now_y = i, j


# 물고기의 거리 파악
def bfs():
    q = deque()
    q.append((now_x, now_y))
    visited = [[-1] * N for _ in range(N)]
    visited[now_x][now_y] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and arr[ni][nj] <= size:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return visited

# print(bfs())
# 먹을 수 있는 물고기 파악
def eat(distance_field):
    x, y = 0, 0
    min_distance = 987654321
    for i in range(N):
        for j in range(N):
            if distance_field[i][j] != -1 and 1 <= arr[i][j] < size:
                if distance_field[i][j] < min_distance:
                    x, y = i, j
                    min_distance = distance_field[x][y]
    if min_distance == 987654321:
        return -10
    else:
        return x, y, min_distance


time = 0
cnt = 0


while True:
    temp = eat(bfs())
    if temp == -10:
        print(time)
        break
    else:
        now_x, now_y = temp[0], temp[1]
        time += temp[2]
        arr[now_x][now_y] = 0
        cnt += 1
        if cnt >= size:
            size += 1
            cnt = 0


# 가장 가까운 거리의 물고기가 많다면 가장 왼쪽꺼
# 자신의 크기와 똑같은 양의 물고기를 먹었다면 크기 + 1
# 먹을 수 있는 물고기가 없다면 끝