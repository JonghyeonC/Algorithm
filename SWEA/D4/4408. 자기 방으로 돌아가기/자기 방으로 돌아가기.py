T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 201
    for i in range(N):
        a, b = map(int, input().split())
        if a % 2 == 1:
            if (a + 1) == b:
                arr[b//2] += 1
        if a % 2 == 1:
            a = (a + 1) // 2
        else:
            a //= 2
        if b % 2 == 1:
            b = (b + 1) // 2
        else:
            b //= 2
        if b > a:
            for j in range(a, b + 1):
                arr[j] += 1
        elif a > b:
            for j in range(b, a + 1):
                arr[j] += 1
    print(f'#{tc} {max(arr)}')