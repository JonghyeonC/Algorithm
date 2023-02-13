T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort()
    standard = arr[0][1]
    i = 1
    cnt = 1
    while i <= N - 1:
        if arr[i][1] < standard:
            standard = arr[i][1]
            cnt += 1
        i += 1
    print(cnt)