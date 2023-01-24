R, C, M = map(int, input().split())
field = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    field[r-1][c-1] = (s, d - 1, z)

shark_ans = 0

for k in range(C):
    for i in range(R):
        if field[i][k]:
            s, d, z = field[i][k]
            shark_ans += z
            field[i][k] = 0
            break

    new_field = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if field[i][j]:
                x, y = i, j
                s, d, z = field[i][j]
                way = s
                while 0 < way:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C:
                        x, y = nx, ny
                        way -= 1
                    else:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if new_field[x][y]:
                    n_s, n_d, n_z = new_field[x][y]
                    if z > n_z:
                        new_field[x][y] = (s, d, z)
                    else:
                        new_field[x][y] = (n_s, n_d, n_z)
                else:
                    new_field[x][y] = (s, d, z)
    for a in range(R):
        for b in range(C):
            field[a][b] = new_field[a][b]

print(shark_ans)


