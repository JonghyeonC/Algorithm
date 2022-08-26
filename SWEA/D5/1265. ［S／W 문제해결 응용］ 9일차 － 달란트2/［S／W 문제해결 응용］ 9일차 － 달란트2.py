T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = []
    total = 1
    for _ in range(P):
        arr.append(N // P)
    if N - arr[0] * P > 0:
        a = (N - arr[0] * P) // (N - arr[0] * P)
    for i in range(N - arr[0] * P):
        arr[i] += a
    for i in range(P):
        total *= arr[i]
    print(f'#{tc} {total}')