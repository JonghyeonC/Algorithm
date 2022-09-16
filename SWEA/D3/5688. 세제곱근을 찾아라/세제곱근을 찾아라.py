T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s = 1
    ans = -1
    while s ** 3 <= N:
        if s ** 3 == N:
            ans = s
            break
        else:
            s += 1
    print(f'#{tc} {ans}')