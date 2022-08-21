T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == k:
                    answer += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == k:
            answer += 1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 0:
                if cnt == k:
                    answer += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == k:
            answer += 1
    print(f'#{tc} {answer}')