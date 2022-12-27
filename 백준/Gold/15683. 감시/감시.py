import copy


def check(x, y, direction, room):                 # cctv가 확인한 부분을 체크
    for num in direction:
        ni, nj = x, y
        while True:
            ni += di[num]                         # cctv가 확인가능한 방향으로 계속 진행
            nj += dj[num]                         #                 "
            if 0 <= ni < N and 0 <= nj < M:       # 방 안에 있다면
                if room[ni][nj] != 6:             # 벽이 아니라면
                    if room[ni][nj] == 0:         # 확인한 구간이라면
                        room[ni][nj] = "#"        # 확인했다는 표시
                else:
                    break                         # 벽이라면 반복문 탈출, 확인 불필요
            else:
                break                             # 범위 밖이라면 반복문 탈출


def dfs(room, depth):
    global ans
    if depth == len(cctv):                         # 전체 cctv개수만큼 경우를 체크했다면 사각지대의 최소값을 확인한다.
        temp = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    temp += 1
        ans = min(ans, temp)
        return
    else:
        new_room = copy.deepcopy(room)             # 원본을 그대로 두기 위해서 deepcopy  사용
        x, y, method = cctv[depth]                 # 좌표와 cctv의 종류
        for direction in cctv_directions[method]:  # 해당 cctv가 확인가능한 방향에 대해서 하나씩 탐색
            check(x, y, direction, new_room)       # 좌표, 감시 방향, 복사한 방의 배열 // 방에서 체크한 부분을 체크한다.
            dfs(new_room, depth + 1)               # 전체 cctv를 다 검사하기 전까지 하나의 경우에서 연속해서 다른 경우를 체크한다.
            new_room = copy.deepcopy(room)         # 하나의 경우를 다 마무리할 경우 배열을 다시 원본으로 초기화하여 확인한다.


# 0 : 상, 1 : 우, 2 : 하, 3 : 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 987654321                                    # 최소값의 초기화
# 전체 cctv의 목록을 저장한다.
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append((i, j, arr[i][j]))         # 좌표와 해당 cctv의 종류도 같이 저장한다.

# 0 : 상, 1 : 우, 2 : 하, 3 : 좌
cctv_directions = [
    [],
    [[0], [1], [2], [3]],                           # 1, 한 방향
    [[0, 2], [1, 3]],                               # 2, 반대 방향
    [[0, 1], [1, 2], [2, 3], [3, 0]],               # 3, 직각 방향
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],   # 4, 3방향
    [[0, 1, 2, 3]]                                  # 5, 4방향
]

dfs(arr, 0)                                         # 하나의 경우에서 연속해서 진행하기 위해서 dfs 사용
print(ans)
