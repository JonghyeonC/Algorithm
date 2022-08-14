t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_1 = [[0] * n for _ in range(n)]
    arr_2 = [[0] * n for _ in range(n)]
    arr_3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_1[i][j] = arr[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr_2[i][j] = arr_1[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr_3[i][j] = arr_2[n-1-j][i]
    print(f'#{tc}')
    for i in range(n):
        print(''.join(map(str, arr_1[i])), end=' ')
        print(''.join(map(str, arr_2[i])), end=' ')
        print(''.join(map(str, arr_3[i])), end=' ')
        print()