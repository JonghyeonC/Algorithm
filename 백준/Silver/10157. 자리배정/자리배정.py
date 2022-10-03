N, M = map(int, input().split())
C = int(input())

arr = [[0] * N for _ in range(M)]
i = M - 1
j = 0
k = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for num in range(1, N * M + 1):
    arr[i][j] = num
    i = i + di[k]
    j = j + dj[k]

    if not (0 <= i < M and 0 <= j < N and arr[i][j] == 0):
        i -= di[k]
        j -= dj[k]

        k = (k + 1) % 4
        i += di[k]
        j += dj[k]
if C > N * M + 1:
    print(0)
else:
    for x in range(M):
        for y in range(N):
            if arr[x][y] == C:
                print(f'{y + 1} {M - x}')