import copy


def check(x, y, direction, room):
    for num in direction:
        ni, nj = x, y
        while True:
            ni += di[num]
            nj += dj[num]
            if 0 <= ni < N and 0 <= nj < M:
                if room[ni][nj] != 6:
                    if room[ni][nj] == 0:
                        room[ni][nj] = "#"
                else:
                    break
            else:
                break


def dfs(room, depth):
    global ans
    if depth == len(cctv):
        temp = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    temp += 1
        ans = min(ans, temp)
        return
    else:
        new_room = copy.deepcopy(room)
        x, y, method = cctv[depth]
        for direction in cctv_directions[method]:
            check(x, y, direction, new_room)
            dfs(new_room, depth + 1)
            new_room = copy.deepcopy(room)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 987654321

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append((i, j, arr[i][j]))

# 0 : 상, 1 : 우, 2 : 하, 3 : 좌
cctv_directions = [
    [],
    [[0], [1], [2], [3]],                           # 1
    [[0, 2], [1, 3]],                               # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],               # 3
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],   # 4
    [[0, 1, 2, 3]]                                  # 5
]

dfs(arr, 0)
print(ans)
