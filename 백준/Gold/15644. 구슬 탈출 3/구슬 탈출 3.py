from collections import deque
import sys


def bfs(r_x, r_y, b_x, b_y, ans):
    q = deque()
    q.append((r_x, r_y, b_x, b_y, ans))
    cnt = 0
    while q:
        for _ in range(len(q)):
            r_x, r_y, b_x, b_y, ans = q.popleft()
            if cnt > 10:
                return -1, ''
            if arr[r_x][r_y] == 'O':
                return cnt, ans
            for k in range(4):
                nr_x = r_x
                nr_y = r_y
                while True:
                    nr_x += di[k]
                    nr_y += dj[k]
                    if arr[nr_x][nr_y] == '#':
                        nr_x -= di[k]
                        nr_y -= dj[k]
                        break
                    if arr[nr_x][nr_y] == 'O':
                        break
                nb_x = b_x
                nb_y = b_y
                while True:
                    nb_x += di[k]
                    nb_y += dj[k]
                    if arr[nb_x][nb_y] == '#':
                        nb_x -= di[k]
                        nb_y -= dj[k]
                        break
                    if arr[nb_x][nb_y] == 'O':
                        break
                if arr[nb_x][nb_y] == 'O':
                    continue
                if nr_x == nb_x and nr_y == nb_y:
                    if abs(nr_x - r_x) + abs(nr_y - r_y) > abs(nb_x - b_x) + abs(nb_y - b_y):
                        nr_x -= di[k]
                        nr_y -= dj[k]
                    else:
                        nb_x -= di[k]
                        nb_y -= dj[k]
                if k == 0:
                    q.append((nr_x, nr_y, nb_x, nb_y, ans + "R"))
                elif k == 1:
                    q.append((nr_x, nr_y, nb_x, nb_y, ans + "D"))
                elif k == 2:
                    q.append((nr_x, nr_y, nb_x, nb_y, ans + "L"))
                elif k == 3:
                    q.append((nr_x, nr_y, nb_x, nb_y, ans + "U"))
        cnt += 1
    return -1, ''


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
b_x = b_y = 0
r_x = r_y = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            b_x = i
            b_y = j
        elif arr[i][j] == 'R':
            r_x = i
            r_y = j

result, ans = bfs(r_x, r_y, b_x, b_y, '')
print(result)
if ans:
    print(ans)