def convert(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if list_a[x][y] == 0:
                list_a[x][y] = 1
            elif list_a[x][y] == 1:
                list_a[x][y] = 0


N, M = map(int, input().split())
list_a = [list(map(int, input())) for _ in range(N)]
list_b = [list(map(int, input())) for _ in range(N)]

cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if list_a[i][j] != list_b[i][j]:
            cnt += 1
            convert(i, j)


print(-1) if list_a != list_b else print(cnt)