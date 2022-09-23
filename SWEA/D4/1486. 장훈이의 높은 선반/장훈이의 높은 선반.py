def comb(k, s, r, total):
    global min_V
    if total > min_V:
        return
    if k == r:
        if total >= B:
            if total < min_V:
                min_V = total
        else:
            return
    else:
        for i in range(s, N - r + 1 + k):
            comb(k+1, i+1, r, total + arr[i])


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_V = 987654321
    for r in range(1, N + 1):
        comb(0, 0, r, 0)
    print(f'#{tc} {min_V - B}')