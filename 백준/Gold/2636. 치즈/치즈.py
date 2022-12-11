from collections import deque


def bfs():
    q = deque()
    # 매번 bfs를 할때마다 방문처리가 초기화가 되어야하므로 bfs함수에서 visited를 초기화 시켜준다
    visited = [[0] * M for _ in range(N)]
    q.append((0, 0))
    visited[0][0] = 1
    # 녹게 되는 치즈의 양을 의미
    temp = 0
    while q:
        i, j = q.popleft()
        # 치즈를 기준으로 돌지 않고, 공기를 기준으로 돌면서 가장자리의 공기와 접한다면 치즈를 녹았다고 표현한다.
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= nj < M and 0 <= ni < N and visited[ni][nj] == 0:
                # 공기를 기준으로 돌면서 방문하지 않는 공기라면 q에 추가하고 방문처리를 한다.
                # 이렇게 되면 가장자리쪽의 공기만 계속해서 방문처리해주면서 돌게 되고 안쪽은 공기랑은 관련이 없다.
                if arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                # 공기를 기준으로 4방향 탐색을 하다가 치즈를 만나게 되면 녹았다고 표시하고, 방문처리를 통해 재방문을 막는다.
                elif arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    visited[ni][nj] = 1
                    # 녹은 치즈 값 추가하기
                    temp += 1

    return temp


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = []
# 총 걸린 시간 초기화
time = 0
# 총 녹게 되는 치즈가 0일때 까지 계속해서 반복을 하기 위함
while True:
    # bfs를 진행했을 때 리턴되는 총 녹은 치즈의 값을 ans배열에 추가시킴
    cnt = bfs()
    if cnt != 0:          # 녹은 치즈가 있다면 배열에 추가시킴, 녹는데 걸리는 시간을 하나 늘려줌
        ans.append(cnt)
        time += 1
    elif cnt == 0:        # 녹은 치즈가 없다는 뜻은 다 녹았다는 뜻이므로 while문에서 나온다
        break

print(time)
print(ans[-1])