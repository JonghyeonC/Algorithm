N, m, M, T, R = map(int, input().split())
hr = m
cnt = 0
time = 0
if (M - m) < T:
    print(-1)
else:
    while cnt < N:
        if hr + T <= M:
            hr += T
            cnt += 1
            time += 1
        elif hr + T > M:
            if hr - R < m:
                hr = m
            else:
                hr -= R
            time += 1
    print(time)