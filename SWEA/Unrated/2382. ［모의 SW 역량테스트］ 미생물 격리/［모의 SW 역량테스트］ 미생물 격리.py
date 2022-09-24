T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    micros = {}
    for group in arr:
        micros[(group[0], group[1])] = [[group[2], group[3]]]
    answer = {}
    for _ in range(M):
        next_micros = {}
        for micro in micros:
            i, j = micro[0], micro[1]
            direction = micros[micro][0][1]
            organism = micros[micro][0][0]
            if direction == 1:
                i -= 1
            elif direction == 2:
                i += 1
            elif direction == 3:
                j -= 1
            elif direction == 4:
                j += 1
            if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                organism //= 2
                if direction == 1:
                    direction = 2
                elif direction == 2:
                    direction = 1
                elif direction == 3:
                    direction = 4
                elif direction == 4:
                    direction = 3
            if (i, j) in next_micros:
                next_micros[(i, j)].append([organism, direction])
            else:
                next_micros[(i, j)] = [[organism, direction]]
        for key in next_micros:
            length = len(next_micros[key])
            if length >= 2:
                temp = next_micros[key]
                total = 0
                present_top = temp[0][0]
                n_direction = temp[0][1]
                for i in range(length):
                    total += temp[i][0]
                    if temp[i][0] > present_top:
                        present_top = temp[i][0]
                        n_direction = temp[i][1]
                next_micros[key] = [[total, n_direction]]
        micros = next_micros
    ans = 0
    for i in micros:
        ans += micros[i][0][0]
    print(f'#{tc} {ans}')