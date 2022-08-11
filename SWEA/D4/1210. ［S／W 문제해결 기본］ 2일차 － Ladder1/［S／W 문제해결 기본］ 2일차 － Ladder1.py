t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    #  x가 1인 시작지점을 찾은 후에 내려가는 방식을 채택함
    for start in range(100):
        if arr[0][start] == 1:
            x = start
            y = 0
            while True:
                #  x좌표가 오른쪽 끝이 아니고 오른쪽 값이 1이라면 0이 나올때까지 이동시킴
                #  0이 나오게 되면 밑으로 한칸 내림
                if x < 99 and arr[y][x+1] == 1:
                    while x < 99 and arr[y][x+1]:
                        x += 1
                    else:
                        y += 1
                #  x좌표가 왼쪽 끝이 아니고 왼쪽 값이 1이라면 0이 나올때까지 이동시킴
                #  0이 나오게 되면 밑으로 한 칸 내림
                elif x > 0 and arr[y][x-1] == 1:
                    while x > 0 and arr[y][x-1]:
                        x -= 1
                    else:
                        y += 1
                #  그 외에 밑에 1이 있다면 밑으로 이동
                elif y < 99:
                    y += 1
                #  y좌표 값이 99이면서 해당하는 위치의 값이 2일 경우에 답으로 체크
                if y == 99:
                    if arr[y][x] == 2:
                        answer = start
                    break
    print(f'#{tc} {answer}')