from itertools import combinations
from collections import deque


def bfs(q):
    visited = [[-1] * N for _ in range(N)]              # 바이러스가 퍼지는 시간을 기록할 배열 초기화
    for x, y in q:
        visited[x][y] = 0                               # M개의 바이러스의 좌표를 모두 0으로 초기화시켜서 다른 활성 바이러스에 의해서 활성화가 된 것으로 표현되는 것을 방지하기 위함
    while q:
        i, j = q.popleft()
        for k in range(4):                              # 4방향 탐색을 진행하면서
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == -1:
                q.append((ni, nj))                      # 본 배열에서 벽이 아니고 아직 방문한 적이 없다면 이동이 가능하므로
                visited[ni][nj] = visited[i][j] + 1     # q에 추가하고 시간을 1초 걸린것으로 지속해서 기록한다
    max_v = 0                                           # 방문된 시간에서 가장 최종적으로 걸린 시간을 찾기 위함
    for i in range(N):
        for j in range(N):
            if arr[i][j]:                               # 애초에 벽인 부분과 바이러스가 존재하는 부분은 빈 부분이 아니므로
                continue                                # 빈 칸에 바이러스를 채워졌는지 확인할 필요가 없다
            if visited[i][j] == -1:                     # 방문처리 배열에서 방문이 안된 칸이 있다면 바이러스가 퍼지지 못한 것이므로
                return 987654321                        # 초기값을 리턴하여 모든 빈칸에 바이러스가 퍼지지 못했다는 것을 알린다
            else:
                max_v = max(max_v, visited[i][j])       # 값이 있다면, 해당 조합에서 모든 곳에 도달한 시간을 리턴한다
    return max_v


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 987654321                                           # 최소값 초기화
virus = []                                                # 모든 바이러스의 위치를 담을 배열
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))                          # 배열을 모두 탐색하면서 바이러스의 위치를 모두 담는다

com_viruses = list(combinations(virus, M))                # combination을 활용해 M개의 바이러스의 위치의 조합을 구한다

for virus_list in com_viruses:                            # 각 조합에서
    q = deque()                                           # 각 조합에 존재하는 M개의 위치를 담을 배열을 만들고
    for viruses in virus_list:
        q.append(viruses)                                 # 배열에 M개의 위치를 담고
    ans = min(ans, bfs(q))                                # 최소값과 bfs에서 리턴되는 값 중 최소값을 찾는다
print(ans if ans != 987654321 else -1)                    # 최소값이 초기화상태라면 바이러스가 퍼지지 못한 것이므로 -1출력