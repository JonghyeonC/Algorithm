arr = [list(map(int, input().split())) for _ in range(5)]


def check():
    lines = 0
    for x in range(5):
        total = 0
        for y in range(5):
            if arr[x][y] == 0:
                total += 1
            if total == 5:
                lines += 1

    for x in range(5):
        total = 0
        for y in range(5):
            if arr[y][x] == 0:
                total += 1
            if total == 5:
                lines += 1

    total = 0
    for x in range(5):
        if arr[x][x] == 0:
            total += 1
        if total == 5:
            lines += 1

    total = 0
    for x in range(5):
        if arr[x][5 - x - 1] == 0:
            total += 1
        if total == 5:
            lines += 1
    return lines


num_list = []
for i in range(5):
    for j in list(map(int, input().split())):
        num_list.append(j)

cnt = 0
answer = []
for k in num_list:
    for i in range(5):
        for j in range(5):
            if k == arr[i][j]:
                arr[i][j] = 0
                cnt += 1
                if check() >= 3:
                    answer.append(cnt)
                    break

for i in range(1):
    print(answer[i])