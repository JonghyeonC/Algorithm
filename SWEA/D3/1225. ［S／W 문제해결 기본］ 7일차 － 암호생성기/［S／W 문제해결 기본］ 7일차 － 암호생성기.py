T = 10
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    while arr[-1] > 0:
        for x in range(1, 6):
            if arr[0] - x <= 0:
                arr.pop(0)
                arr.append(0)
                break
            else:
                arr.append(arr[0] - x)
                arr.pop(0)

    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()