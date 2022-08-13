for tc in range(1, 11):
    num = int(input())
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
# 각 행의 합
    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[i][j]

        if answer < total:
            answer = total
# 각 열의 합
    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[j][i]

        if answer < total:
            answer = total

#왼쪽 상단 대각선
    total = 0
    for i in range(n):
        total += arr[i][i]

        if answer < total:
            answer = total

#오른쪽 상단 대각선
    total = 0
    for i in range(n):
        total += arr[i][n-1-i]

        if answer < total:
            answer = total

    print(f'#{tc} {answer}')