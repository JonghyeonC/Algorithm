def dfs(cnt):
    global ans, total
    if cnt == 3:                            # 결정된 꽃이 3가지가 되었다면
        ans = min(ans, total)               # 최소값을 구한다
        return
    for i in range(1, N - 1):               # 꽃이 필려면 가쪽에는 씨앗이 심어질 수 없으므로
        for j in range(1, N - 1):
            flag = 0                        # 생서될 수 있는 경우라면 0, 될 수 없다면 1
            for k in range(5):              # 중앙을 포함한 상하좌우 5방향 탐색
                ni = i + di[k]
                nj = j + dj[k]
                if visited[ni][nj] == 1:
                    flag = 1                # 이미 방문된 이력이 있다면 꽃이 필 수 없으므로 제외
            if flag == 0:                   # 필 수 있다면
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 1     # 방문처리를 하고
                    total += arr[ni][nj]    # 소요 비용을 계산
                dfs(cnt + 1)                # 다른 씨앗의 위치를 구하러 재귀식
                for k in range(5):          # 재괴식에서 리턴되었을 때 백트래킹
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 0     # 기존의 방문처리 초기화
                    total -= arr[ni][nj]    # 소요 비용도 초기화


di = [0, 1, 0, -1, 0]
dj = [0, 0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
total = 0                                    # 각 3가지의 꽃이 필때 드는 비용의 합
ans = 987654321                              # 각 비용 중 최솟값을 구하기 위한 초기값
dfs(0)                                       # 재귀식 사용 (백트래킹이 필요하다고 생각해서)
print(ans)
