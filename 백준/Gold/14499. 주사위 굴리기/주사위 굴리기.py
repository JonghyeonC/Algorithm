N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 6        # 0 : 위, 1 : 밑, 2 : 앞, 3 : 뒤, 4 : 왼, 5 : 오

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
for a in list(map(int, input().split())):
    nx = x + di[a]
    ny = y + dj[a]
    if 0 <= nx < N and 0 <= ny < M:
        if a == 1:
            dice[4], dice[0], dice[5], dice[1] = dice[0], dice[5], dice[1], dice[4]
        elif a == 2:
            dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]
        elif a == 3:
            dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]
        elif a == 4:
            dice[2], dice[0], dice[3], dice[1] = dice[0], dice[3], dice[1], dice[2]

        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[1]
        else:
            arr[nx][ny], dice[1] = 0, arr[nx][ny]
        print(dice[0])
        x, y = nx, ny