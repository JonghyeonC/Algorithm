t = int(input())
for tc in range(1, t+1):
    n = 9
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 1

    # 가로, 세로 확인
    for i in range(n):
        row = [0] * 10
        column = [0] * 10
        for j in range(n):
            if row[arr[i][j]] == 1:
                answer = 0
            else:
                row[arr[i][j]] = 1
            if column[arr[j][i]] == 1:
                answer = 0
            else:
                column[arr[j][i]] = 1
    # 격자 확인
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            matrix = [0] * 10
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if matrix[arr[k][l]] == 1:
                        answer = 0
                    else:
                        matrix[arr[k][l]] = 1

    print(f'#{tc} {answer}')