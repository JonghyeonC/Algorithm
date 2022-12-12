from collections import deque


def bfs(i, j, height):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] > height:
                q.append((ni, nj))
                visited[ni][nj] = 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력된 배열에서 최대 높이를 구해야지 높이에 따른 안전영역의 최대값을 구하는 범위를 제한할 수 있다.
max_value = 0                                # 높이는 1이상 100이하의 정수이므로 최대값을 0으로 초기화한다.
ans = 0
for i in range(N):
    for j in range(N):
        max_value = max(arr[i][j], max_value)

for height in range(max_value + 1):           # 비가 높이의 최대값까지 온다고 가정을 하고 가능한 모든 강수량 체크
    visited = [[0] * N for _ in range(N)]     # 각 높이에 따라서 방문처리를 해야하므로 for문 안에 visited초기화
    cnt = 0                                   # 각 높이에 따라서 안전영역 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visited[i][j] == 0:
                bfs(i, j, height)             # 방문하지 않았고 높이보다 크다면 bfs함수로
                cnt += 1                      # 안전영역의 갯수를 찾는 것으므로 총 bfs문에 들어간 횟수를 구한다.
    ans = max(cnt, ans)                       # 최대값과 구한 갯수를 비교하여 최대 안전영역의 개수를 구한다.
print(ans)
