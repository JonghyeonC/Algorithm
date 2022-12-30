def diffusion(i, j):
    cnt = 0                                           # 해당 먼지에서 확산된 범위를 위한 값 초기화
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 범위 안에 있고, 청소기가 아니라면 확산을 실시할 것
        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in cleaner:
            cnt += 1                                  # 확산된 값 증가
            temp[ni][nj] += arr[i][j] // 5            # 기점으로 부터 나누기 5하여 확산 시킨 값만 따로 저장
    arr[i][j] = arr[i][j] - ((arr[i][j] // 5) * cnt)  # 확산된 기점은 확산된 범위 만큼 먼지의 양 // 5를 곱하여 빼줌
    # 이렇게 하는 이유는 기점의 값을 그 자리에서 빼주게 되면 기존의 값에 확산된 먼지의 값이 더해진 상황에서 뺄 수 있어서

# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cleaner = []                                           # 청소기 위치 담을 배열
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            cleaner.append((i, j))                     # 청소기 담기

for _ in range(T):                                     # 주어진 시간 동안 진행
    temp = [[0] * M for _ in range(N)]                 # 매 초마다 먼지가 확산되는 값을 저장
    # 1. 전체 먼지를 훑으면서 확산을 진행
    for i in range(N):
        for j in range(M):
            if arr[i][j] != -1 and arr[i][j] != 0:     # 청소기도 아니고 빈 공간도 아니라면
                diffusion(i, j)                        # 확신 시작

    for i in range(N):
        for j in range(M):
            arr[i][j] += temp[i][j]                    # 확산된 값을 이제 본래의 공간에 더해서 확산되고 빼진 값

    # 2. 위, 아래의 위치에 따라서 방향을 다르게 하면 공기청정기의 영향을 따라 먼지를 위치시킨다
    # 반시계
    direction = 1                                      # 먼저 오른쪽으로 회전시작
    i, j = cleaner[0]                                  # 먼저 들어간 값이 위의 값임
    i, j = i, 1                                        # 청소기는 0번 열에 위치하므로 1번 열부터 청소가 시작
    n_i = i                                            # 기존의 행의 위치는 저장하고 있어야함
    memory = 0                                         # 현재의 값을 저장한 상태로 다음의 위치로 넘어가서 그 위치에 현재의 값을 저장하고, 다시 그 옮겨진 위치의 값을 다시 저장하여 1자리씩 옮긴다
    while True:
        ni = i + di[direction]
        nj = j + dj[direction]

        if ni == n_i and nj == 0:                      # 만약 한바퀴 돌아서 도착한 값이 청소기라면 회전은 마친다
            arr[i][j], memory = memory, arr[i][j]      # 다음에 옮겨지게 되는 위치가 청소기인 것이지, 현재의 위치는 그 전의 먼지의 값을 옮겨져야한다
            break

        arr[i][j], memory = memory, arr[i][j]          # 전의 위치의 값과 현재의 위치의 값을 맞바꿈으로써 1자리씩 옮길 수 있다
        if 0 > ni or ni >= N or 0 > nj or nj >= M:     # 벽을 만나게 되는 경우에는 방향을 바꿔야한다.
            ni = i - di[direction]                     # 옮겨지게 되는 값을 반대로 계산해 정상 상태로 만들어 준다
            nj = j - dj[direction]

            direction -= 1                             # 반시계방향으로 돌아야하므로 -1을 하여 시계방향을 반대로 돈다
            if direction == -1:                        # 0에서 -1을 하게 되면 -1이 되어 그 다음 값을 계산시 -2가 되므로 이를 방지하기 위함
                direction = 3
            ni = i + di[direction]                     # 다시 바뀐 방향으로 다음 위치를 구한다
            nj = j + dj[direction]

        i, j = ni, nj                                  # 다시 회전하기 위해서는 옮겨져야 하는 위치로 현재의 위치를 바꾼다

    # 시계
    direction = 1
    i, j = cleaner[1]
    i, j = i, 1
    n_i = i
    memory = 0
    while True:
        ni = i + di[direction]
        nj = j + dj[direction]

        if ni == n_i and nj == 0:
            arr[i][j], memory = memory, arr[i][j]
            break

        arr[i][j], memory = memory, arr[i][j]
        if 0 > ni or ni >= N or 0 > nj or nj >= M:
            ni = i - di[direction]
            nj = j - dj[direction]

            direction = (direction + 1) % 4             # 주어진 회전 배열이 시계방향이므로 그대로 1을 더하여 방향을 바꿀 수 있다
            ni = i + di[direction]
            nj = j + dj[direction]

        i, j = ni, nj

# 3. 시간만큼 다 확산하고 청소되고 나서 남은 먼지 계산
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            ans += arr[i][j]                             # 미세먼지 존재한다면 총 미세먼지의 값을 구함
print(ans)
