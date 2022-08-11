t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_distance = 987654321
    answer = 0
    for start in range(100):
        if arr[0][start] == 1:
            x = start
            y = 0
            cnt = 0
            while True:
                if x < 99 and arr[y][x+1] == 1:
                    while x < 99 and arr[y][x+1]:
                        x += 1
                        cnt += 1
                    else:
                        y += 1
                elif x > 0 and arr[y][x-1] == 1:
                    while x > 0 and arr[y][x-1]:
                        x -= 1
                        cnt += 1
                    else:
                        y += 1
                elif arr[y+1][x] == 1:
                    y += 1
                if y == 99:
                    if min_distance >= cnt:
                        min_distance = cnt
                        answer = start
                    break

    print(f'#{tc} {answer}')