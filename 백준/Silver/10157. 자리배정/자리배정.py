c, r = map(int, input().split())
n = int(input())
arr = [[0] * c for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
k = 0
x = 0
y = r - 1

for i in range(1, c * r + 1):
    arr[y][x] = i

    x += dx[k]
    y += dy[k]

    if x < 0 or x >= c or y < 0 or y >= r or arr[y][x] != 0:
        x -= dx[k]
        y -= dy[k]

        k = (k + 1) % 4
        x += dx[k]
        y += dy[k]
if n > r * c:
    print(0)
else:
    for i in range(c):
        for j in range(r):
            if n == arr[j][i]:
                print(f'{i+1} {r - j}')