t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    vel_s = 0
    distance = 0
    for i in range(n):
        if arr[i][0] == 1:
            vel_s += arr[i][1]
            distance += vel_s
        elif arr[i][0] == 2:
            if vel_s < arr[i][1]:
                vel_s = 0
            else:
                vel_s -= arr[i][1]
            distance += vel_s
        elif arr[i][0] == 0:
            vel_s = vel_s
            distance += vel_s
            continue

    print(f'#{tc} {distance}')