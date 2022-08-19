T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    numbers = []
    check = {}

    for i in range(1, 5001):
        check[i] = 0

    for _ in range(P):
        numbers.append(int(input()))

    for i in range(N):
        for j in range(arr[i][0], arr[i][1] + 1):
            check[j] += 1

    print(f'#{tc}', end=' ')
    for i in numbers:
        print(check[i], end=' ')
    print()