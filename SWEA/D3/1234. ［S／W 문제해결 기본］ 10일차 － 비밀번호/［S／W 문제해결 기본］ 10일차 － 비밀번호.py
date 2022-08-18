def check(arr):
    leng = len(arr)
    i = 0
    while True:
        if i == len(arr) - 1:
            break
        if arr[i] == arr[i+1]:
            arr[i:i+2] = ''
            i = 0
        else:
            i += 1
        if arr[0] == 0:
            arr[0] = ''
    return arr

T = 10
for tc in range(1, T+1):
    n, numbers = map(int, input().split())
    arr = list(map(int, str(numbers)))
    print(f'#{tc}', end=' ')
    for i in check(arr):
        print(i, end='')
    print()