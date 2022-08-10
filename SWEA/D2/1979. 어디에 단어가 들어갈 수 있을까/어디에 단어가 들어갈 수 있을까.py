num = int(input())
for tc in range(1, num+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    total = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                if cnt == k:
                    if j == n - 1:
                        total += 1
                        cnt = 0
                    else:
                        if arr[i][j+1] != 1:
                            total += 1
                            cnt = 0
            else:
                cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == k:
                    if j == n - 1:
                        total += 1
                        cnt = 0
                    else:
                        if arr[j+1][i] != 1:
                            total += 1
                            cnt = 0
            else:
                cnt = 0
    print(f'#{tc} {total}')