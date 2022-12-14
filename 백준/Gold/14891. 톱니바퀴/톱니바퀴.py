# 인접한 톱니바퀴가 돌아야먄 그 인접한 톱니바퀴의 인접한 톱니바퀴도 돈다 (중요 포인트)
from collections import deque


def rotate(num, direc):
    gears[num].rotate(direc)                   # deque의 rotate함수를 이용해서 양수일 경우 시계방향, 음수일 경우 반시계방향으로 회전한다.


def check_left(num, direc):
    if num == -1:                              # 왼쪽 끝에서 벗어난 경우에는 회전 x
        return

    if gears[num][2] != gears[num + 1][6]:     # 현재 톱니바퀴의 3번째 톱니에서 그 다음 톱니의 7번째 톱니와 비교해서 다르면 회전한다.
        check_left(num - 1, direc * -1)        # 톱니가 회전해야 그 톱니의 인접한 톱니바퀴가 회전할 수 있다
        gears[num].rotate(direc)               # 회전할 수 있는 전체 톱니를 구하고 나서야 방향에 맞게 회전시킨다
    else:
        return


def check_right(num, direc):
    if num == 4:                               # 오른쪽 끝에서 벗어난 경우에는 회전 x
        return

    if gears[num - 1][2] != gears[num][6]:
        check_right(num + 1, direc * -1)
        gears[num].rotate(direc)
    else:
        return


gears = []                                     # 기어를 담을 배열
for _ in range(4):
    gear = deque(map(int, input()))            # deque를 쓰기위해 list대신에 queue를 사용한다
    gears.append(gear)                         # 기어 배열에 입력된 기어를 추가한다

N = int(input())

operations = []
for _ in range(N):
    operation = list(map(int, input().split()))
    operations.append(operation)              # 회전시킨 기어와 방향을 입력받고 작동 배열에 추가시킨다

for operation in operations:
    gear_num, direction = operation
    check_left(gear_num - 2, direction * -1)  # 회전시켜야하는 톱니의 왼쪽을 확인한다. 현재의 톱니는 입력받은 숫자 - 1이다
    check_right(gear_num, direction * -1)     # 회전시켜야하는 톱니의 오른쪽을 확인한다.
    rotate(gear_num - 1, direction)           # 주변 톱니의 회전을 다 검사한 후에 회전시켜야하는 톱니를 회전시킨다.

ans = 0
for i in range(4):                            # 각 톱니의 0번째 기어의 1의 여부에 따라서 1, 2, 4, 8의 값을 더한다.
    if i == 0:
        ans += gears[i][0] * 1
    elif i == 1:
        ans += gears[i][0] * 2
    elif i == 2:
        ans += gears[i][0] * 4
    elif i == 3:
        ans += gears[i][0] * 8
print(ans)
