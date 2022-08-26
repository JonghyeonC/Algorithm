T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0]
    dj = [0, 1]
    rows = []
    columns = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                for k in range(2):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]
                    while arr[ni][nj] != 0:
                        if k == 0:
                            ni += 1
                        elif k == 1:
                            nj += 1
                        cnt += 1
                    if k == 0:
                        rows.append(cnt)
                    elif k == 1:
                        columns.append(cnt)
                for a in range(rows[-1]):
                    for b in range(columns[-1]):
                        arr[i+a][j+b] = 0
    for i in range(len(rows)-1):
        min_idx = i
        for j in range(i+1, len(rows)):
            if rows[min_idx] * columns[min_idx] > rows[j] * columns[j]:
                min_idx = j
        rows[min_idx], rows[i] = rows[i], rows[min_idx]
        columns[min_idx], columns[i] = columns[i], columns[min_idx]
    print(f'#{tc} {len(rows)}', end=' ')
    for i in range(len(rows)):
        print(f'{rows[i]} {columns[i]}', end=' ')
    print()