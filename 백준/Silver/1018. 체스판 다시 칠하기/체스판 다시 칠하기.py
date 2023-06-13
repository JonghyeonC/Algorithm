import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]
min_cnt = 32
for i in range(N - 7):
    for j in range(M - 7):
        tmp = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 무조건 맨 위가 B가 맞도록 생각하고 풒기
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        tmp += 1
                else:
                    if board[x][y] != 'W':
                        tmp += 1
        min_cnt = min(min_cnt, min(tmp, 64 - tmp))

print(min_cnt)