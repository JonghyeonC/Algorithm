def diffusion(i, j):
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in cleaner:
            cnt += 1
            temp[ni][nj] += arr[i][j] // 5
    arr[i][j] = arr[i][j] - ((arr[i][j] // 5) * cnt)


# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cleaner = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            cleaner.append((i, j))

for _ in range(T):
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != -1 and arr[i][j] != 0:
                diffusion(i, j)

    for i in range(N):
        for j in range(M):
            arr[i][j] += temp[i][j]

    # for item in arr:
    #     print(*item)
    # print()

    # 반시계
    direction = 1
    i, j = cleaner[0]
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

            direction -= 1
            if direction == -1:
                direction = 3
            ni = i + di[direction]
            nj = j + dj[direction]

        i, j = ni, nj

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

            direction = (direction + 1) % 4
            ni = i + di[direction]
            nj = j + dj[direction]

        i, j = ni, nj

    # for item in arr:
    #     print(*item)
    # print()

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)

# 전체 먼지를 뽑고
# 먼지의 확산을 동시에 진행
# 공기청전기의 윗부분과 아래부분에 따라서 (위:반시계, 밑:시계) 돌면서 먼지를 한칸씩 민다
# 주어진 초만큼 돌고난 뒤의 남은 먼지를 계산한다