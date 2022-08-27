T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt > max_val:
                    max_val = cnt
                cnt = 0
        if cnt > max_val:
            max_val = cnt

    for i in range(m):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 0:
                if cnt > max_val:
                    max_val = cnt
                cnt = 0
        if cnt > max_val:
            max_val = cnt

    print(f'#{tc} {max_val}')