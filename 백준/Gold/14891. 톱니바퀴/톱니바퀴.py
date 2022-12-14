from collections import deque


def rotate(num, direc):
    gears[num].rotate(direc)


def check_left(num, direc):
    if num == -1:
        return

    if gears[num][2] != gears[num + 1][6]:
        check_left(num - 1, direc * -1)
        gears[num].rotate(direc)
    else:
        return


def check_right(num, direc):
    if num == 4:
        return

    if gears[num - 1][2] != gears[num][6]:
        check_right(num + 1, direc * -1)
        gears[num].rotate(direc)
    else:
        return


gears = []
for _ in range(4):
    gear = deque(map(int, input()))
    gears.append(gear)

N = int(input())

operations = []
for _ in range(N):
    operation = list(map(int, input().split()))
    operations.append(operation)

for operation in operations:
    gear_num, direction = operation
    check_left(gear_num - 2, direction * -1)
    check_right(gear_num, direction * -1)
    rotate(gear_num - 1, direction)

ans = 0
for i in range(4):
    if i == 0:
        ans += gears[i][0] * 1
    elif i == 1:
        ans += gears[i][0] * 2
    elif i == 2:
        ans += gears[i][0] * 4
    elif i == 3:
        ans += gears[i][0] * 8
print(ans)