T = int(input())
for tc in range(1, T+1):
    N = int(input())

    stop = [0] * 1001
    for i in range(N):
        T, S, E = map(int, input().split())
        if T == 1:
            for j in range(S, E+1):
                stop[j] += 1
        elif T == 2:
            stop[S] += 1
            stop[E] += 1
            for j in range(S+1, E):
                if S % 2 == 0:
                    if j % 2 == 0:
                        stop[j] += 1
                elif S % 2 == 1:
                    if j % 2 == 1:
                        stop[j] += 1
        elif T == 3:
            stop[S] += 1
            stop[E] += 1
            for j in range(S+1, E):
                if S % 2 == 0:
                    if j % 4 == 0:
                        stop[j] += 1
                elif S % 2 == 1:
                    if j % 3 == 0 and j % 10 != 0:
                        stop[j] += 1
    print(f'#{tc} {max(stop)}')