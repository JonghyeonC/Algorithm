T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()

    cnt = 0
    idx = 0
    for i in range(time[-1] + 1):
        if i != 0:
            if i % M == 0:
                cnt += K
        if i == time[idx]:
            if cnt == 0:
                ans = 'Impossible'
                break
            else:
                cnt -= 1
                idx += 1
        if i == time[-1]:
            if cnt > 0:
                ans = 'Possible'
            else:
                ans = 'Impossible'
    print(f'#{tc} {ans}')