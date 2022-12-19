N, M, x, y, K = map(int, input().split())  # 좌표를 (r, c)에서 r이 세로를 c가 가로 길이를 가리킨다.
arr = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 6        # 0 : 위, 1 : 밑, 2 : 앞, 3 : 뒤, 4 : 왼, 5 : 오

di = [0, 0, 0, -1, 1]                      # 0은 처음 위치고, 1부터 4까지는 오른쪽, 왼쪽, 앞쪽, 뒤쪽으로 움직인다.
dj = [0, 1, -1, 0, 0]
for a in list(map(int, input().split())):
    nx = x + di[a]
    ny = y + dj[a]
    if 0 <= nx < N and 0 <= ny < M:
        if a == 1:                         # 오른쪽으로 구르면 왼->위, 위->오, 우->밑, 밑->왼
            dice[4], dice[0], dice[5], dice[1] = dice[0], dice[5], dice[1], dice[4]
        elif a == 2:                       # 왼쪽으로 구르면 위->왼, 오->위, 밑->오, 왼->밑
            dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]
        elif a == 3:                       # 앞으로 구르면 위->앞, 뒤->위, 밑->뒤, 앞->밑
            dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]
        elif a == 4:                       # 뒤로 구르면 위->앞, 뒤->위, 밑->뒤, 앞->밑
            dice[2], dice[0], dice[3], dice[1] = dice[0], dice[3], dice[1], dice[2]

        if arr[nx][ny] == 0:               # 지도의 값이 0이라면 주사위 밑의 값이 칸에 복사된다.
            arr[nx][ny] = dice[1]
        else:                              # 지도의 값이 0이 아니라면 지도의 값이 주사위 밑의 값으로 가고, 지도의 값은 0이 된다.
            arr[nx][ny], dice[1] = 0, arr[nx][ny]
        print(dice[0])                     # 주사위의 위값을 출력한다.
        x, y = nx, ny