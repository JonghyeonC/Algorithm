R, C, M = map(int, input().split())
field = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 해당 위치에 (초당 이동하는 칸 수, 이동 방향, 크기)을 입력받는다
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    field[r-1][c-1] = (s, d - 1, z)

shark_ans = 0                                 # 잡은 상어의 크기의 합
                                              
for k in range(C):                            ## 열을 기준으로 한 칸씩 이동하는 것을 구현
    for i in range(R):                        ## 가장 가까운 상어를 잡는다
        if field[i][k]:                       # 입력받은 배열에 값이 존재한다면
            s, d, z = field[i][k]             # 열 기준으로 가장 첫번째로 선택되는 값을 선택하고
            shark_ans += z                    # 상어를 잡고
            field[i][k] = 0                   # 그 상어를 배열에서 삭제시키고
            break                             # 첫번째 상어만 잡으므로 더이상 탐색은 하지 않는다

    new_field = [[0] * C for _ in range(R)]   # 한 칸에 여러 상어가 겹칠 수 있으므로 임시 배열
    for i in range(R):                        ## 상어 이동
        for j in range(C):                    # 완전 탐색시작
            if field[i][j]:                   # 상어가 존재한다면
                x, y = i, j                   # 해당 좌표에서
                s, d, z = field[i][j]         # 해당 좌표에 존재하는 상어의 속도, 방향, 크기
                way = s                       # 이동할 수 있는 칸의 수를 복사해둔다
                while 0 < way:                # 이동을 할 수 있을 때까지
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C:  #  상어가 이동할 때 배열안에 존재한다면
                        x, y = nx, ny         # 이동한 위치를 현재 위치로 치환
                        way -= 1              # 이동할 수 있는 칸의 수를 1개 줄인다
                    else:                     # 배열 안에 존재하지 않는다면
                        if d == 0:            # 각 방향의 반대로 바꾼다
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if new_field[x][y]:                        # 하나의 상어의 이동이 마친 후
                    n_s, n_d, n_z = new_field[x][y]        # 임시 배열에 값이 존재한다면 
                    if z > n_z:                            # 방금 이동이 끝난 크기가 더 크다면
                        new_field[x][y] = (s, d, z)        # 방금 이동한 상어를 임시 배열에 추가
                    else:                                  # 반대라면
                        new_field[x][y] = (n_s, n_d, n_z)  # 기존 상어를 임시 배열에 그대로 둔다
                else:
                    new_field[x][y] = (s, d, z)            # 임시 배열에 값이 없다면 그냥 추가
    for a in range(R):                                   
        for b in range(C):                                 # 1초에 행해지는 모든 이동이 끝나면
            field[a][b] = new_field[a][b]                  # 임시 배열의 값을 진짜 배열로 바꾼다

print(shark_ans)


